import pyaudio, wave
import numpy as np
import os
import base64
import hashlib
import hmac
import json
import time
import requests
import urllib

# https://blog.csdn.net/qq_51116518/article/details/129467182
def listen():
    temp = 20
    CHUNK = 1024 
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 16000 #采样率
    WAVE_OUTPUT_FILENAME = 'output.wav'

    mindb=8000    #录音音量阈值，大于则开始录音，否则结束(麦克风噪音较大，可以适当调大)
    delayTime=5  #音量小于阈值5秒后自动终止
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)
    print("开始计时")

    frames = []
    flag = False            # 开始录音节点
    stat = True				#判断是否继续录音
    stat2 = False			#判断声音小于阈值

    tempnum = 0				#tempnum、tempnum2、tempnum3为时间
    tempnum2 = 0

    while stat:
        data = stream.read(CHUNK,exception_on_overflow = False)
        frames.append(data)
        audio_data = np.frombuffer(data, dtype=np.short)
        volume = np.max(audio_data)
        if volume > mindb and flag==False:
            flag =True
            
            print("开始录音")
            tempnum2=tempnum

        if flag:

            if(volume < mindb and stat2==False):
                stat2 = True
                tempnum2 = tempnum
                print("声音小，且之前是是大的或刚开始，记录当前点")
            if(volume> mindb):
                stat2 =False
                tempnum2 = tempnum
                #刷新

            if(tempnum > tempnum2 + delayTime*15 and stat2==True):
                print("间隔%.2lfs后开始检测是否还是小声"%delayTime)
                if(stat2 and temp < mindb):
                    stat = False
                    #还是小声，则stat=True
                    print("low")
                else:
                    stat2 = False
                    print("high")


        print(str(volume)  +  "      " +  str(tempnum))
        tempnum = tempnum + 1
        if tempnum > 250:	#超时直接退出(16秒左右)
            stat = False
    print("录音结束")

    stream.stop_stream()
    stream.close()
    p.terminate()
    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()
    return True   

listen()

# https://xfyun-doc.xfyun.cn/static/16735945125044764/lfasr_new_python_demo.zip
lfasr_host = 'https://raasr.xfyun.cn/v2/api'
# 请求的接口名
api_upload = '/upload'
api_get_result = '/getResult'

class RequestApi(object):
    def __init__(self, appid, secret_key, upload_file_path):
        self.appid = appid
        self.secret_key = secret_key
        self.upload_file_path = upload_file_path
        self.ts = str(int(time.time()))
        self.signa = self.get_signa()

    def get_signa(self):
        appid = self.appid
        secret_key = self.secret_key
        m2 = hashlib.md5()
        m2.update((appid + self.ts).encode('utf-8'))
        md5 = m2.hexdigest()
        md5 = bytes(md5, encoding='utf-8')
        # 以secret_key为key, 上面的md5为msg， 使用hashlib.sha1加密结果为signa
        signa = hmac.new(secret_key.encode('utf-8'), md5, hashlib.sha1).digest()
        signa = base64.b64encode(signa)
        signa = str(signa, 'utf-8')
        return signa


    def upload(self):
        print("上传部分：")
        upload_file_path = self.upload_file_path
        file_len = os.path.getsize(upload_file_path)
        file_name = os.path.basename(upload_file_path)

        param_dict = {}
        param_dict['appId'] = self.appid
        param_dict['signa'] = self.signa
        param_dict['ts'] = self.ts
        param_dict["fileSize"] = file_len
        param_dict["fileName"] = file_name
        param_dict["duration"] = "200"
        print("upload参数：", param_dict)
        data = open(upload_file_path, 'rb').read(file_len)

        response = requests.post(url =lfasr_host + api_upload+"?"+urllib.parse.urlencode(param_dict),
                                headers = {"Content-type":"application/json"},data=data)
        print("upload_url:",response.request.url)
        result = json.loads(response.text)
        print("upload resp:", result)
        return result


    def get_result(self):
        uploadresp = self.upload()
        orderId = uploadresp['content']['orderId']
        param_dict = {}
        param_dict['appId'] = self.appid
        param_dict['signa'] = self.signa
        param_dict['ts'] = self.ts
        param_dict['orderId'] = orderId
        param_dict['resultType'] = "transfer,predict"
        print("")
        print("查询部分：")
        print("get result参数：", param_dict)
        status = 3
        # 建议使用回调的方式查询结果，查询接口有请求频率限制
        while status == 3:
            response = requests.post(url=lfasr_host + api_get_result + "?" + urllib.parse.urlencode(param_dict),
                                     headers={"Content-type": "application/json"})
            # print("get_result_url:",response.request.url)
            result = json.loads(response.text)
            #print(result)
            status = result['content']['orderInfo']['status']
            print("status=",status)
            if status == 4:
                break
            time.sleep(5)
        
        orderResult = result['content']['orderResult']
        result_json = json.loads(orderResult)
        sentences = []
        lattices = result_json['lattice']
        for lattice in lattices:
            json_1best = lattice['json_1best']
            st = json.loads(json_1best)['st']
            rt = st['rt']
            for r in rt:
                ws = r['ws']
                for w in ws:
                    cw = w['cw']
                    for cw_item in cw:
                        sentences.append(cw_item['w'])
        # 拼接成完整句子
        complete_sentence = ''.join(sentences)
        print("get_result text:", complete_sentence)
        return complete_sentence
 
 
'''if __name__ == '__main__':
    api = RequestApi(appid="9de35c86", secret_key="ce48950bb9ce8acde19dd90e9d1b8657", upload_file_path=r"test.wav")
    while True:
        listen()
        if(listen()):
            api.get_result()'''