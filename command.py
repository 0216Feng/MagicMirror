from assistant.record import listen, RequestApi
from assistant.voiceassistant import SparkGPT
import datetime
import sqlite3
import json

api = RequestApi(appid="", secret_key="", upload_file_path=r"output.wav")
while True:
    if(listen()):
        text = api.get_result()
        if(text != ''):
            assistant = SparkGPT()
            answer = assistant.ask(text, flow_print=False, is_history = False, callback_func = None)
            print(answer)
            answer = answer.replace("'", '"')
            answer_json = json.loads(answer)
            component = answer_json.get("组件")
            operation = answer_json.get("操作")
            confidence = answer_json.get("置信度")  
            if confidence < 0.5:
                print("置信度不足，请重新说一遍")
            else:
                match component:
                    case '课程表': 
                        match operation:
                            case '开启': 
                                database = sqlite3.connect('database.db')
                                query = "UPDATE statusInfo SET State = 1 WHERE Item = 'Course'"
                                database.execute(query)
                                database.commit()
                                print("课程表开启成功")
                            case '关闭': 
                                database = sqlite3.connect('database.db')
                                query = "UPDATE statusInfo SET State = 0 WHERE Item = 'Course'"
                                database.execute(query)
                                database.commit()
                                print("课程表关闭成功")
                            case '新增内容': 
                                database = sqlite3.connect('database.db')
                                query = "SELECT MAX(CID) + 1 FROM courseInfo"
                                cid = database.execute(query).fetchone()
                                if cid[0] is None:
                                    cid = 1
                                else:
                                    cid = cid[0]
                                query = "INSERT INTO courseInfo (CID, Name, Time, Location, Week, Description) VALUES (?,?,?,?,?,?)" 
                                params = (cid, answer_json['详情']['课程名称'], answer_json['详情']['时间段'], answer_json['详情']['地点'], answer_json['详情']['星期'], "")
                                database.execute(query, params)
                                database.commit()
                                print("新增课程成功")
                            case '删除内容': 
                                database = sqlite3.connect('database.db')
                                query = "DELETE FROM courseInfo WHERE Name =?"
                                params = (answer_json['详情']['课程名称'])
                                database.execute(query, params)
                                database.commit()
                                print("删除课程成功")
                    
                    case '日程表':
                        match operation:
                            case '开启': 
                                database = sqlite3.connect('database.db')
                                query = "UPDATE statusInfo SET State = 1 WHERE Item = 'Schedule'"
                                database.execute(query)
                                database.commit()
                                print("日程表开启成功")
                            case '关闭': 
                                database = sqlite3.connect('database.db')
                                query = "UPDATE statusInfo SET State = 0 WHERE Item = 'Schedule'"
                                database.execute(query)
                                database.commit()
                                print("日程表关闭成功")
                            case '新增内容': 
                                database = sqlite3.connect('database.db')
                                query = "SELECT MAX(SID) + 1 FROM scheduleInfo"
                                sid = database.execute(query).fetchone()
                                if sid[0] is None:
                                    sid = 1
                                else:
                                    sid = sid[0]
                                query = "INSERT INTO scheduleInfo (SID, Name, Time, Location, Description) VALUES (?,?,?,?,?)"
                                params = (sid, answer_json['详情']['事务'], answer_json['详情']['时间'], answer_json['详情']['地点'], "")
                                database.execute(query, params)
                                database.commit()
                                print("新增日程成功")
                            case '删除内容': 
                                database = sqlite3.connect('database.db')
                                query = "DELETE FROM scheduleInfo WHERE (Name =? AND Time =?)" 
                                params = (answer_json['详情']['事务'], answer_json['详情']['时间'])
                                database.execute(query, params)
                                database.commit()
                                print("删除日程成功")
                                
                    case '个人护理产品':
                        match operation:
                            case '开启': 
                                database = sqlite3.connect('database.db')
                                query = "UPDATE statusInfo SET State = 1 WHERE Item = 'Care'"
                                database.execute(query)
                                database.commit()
                                print("个人护理产品开启成功")
                            case '关闭': 
                                database = sqlite3.connect('database.db')
                                query = "UPDATE statusInfo SET State = 0 WHERE Item = 'Care'"
                                database.execute(query)
                                database.commit()
                                print("个人护理产品关闭成功")
                            case '新增内容': 
                                database = sqlite3.connect('database.db')
                                query = "SELECT MAX(BID) + 1 FROM careInfo"
                                bid = database.execute(query).fetchone()
                                if bid[0] is None:
                                    bid = 1
                                else:
                                    bid = bid[0]
                                query = "INSERT INTO careInfo (PID, Brand, Type, Expire, Description) VALUES (?,?,?)"
                                params = (bid, answer_json['详情']['品牌'], answer_json['详情']['类型'], answer_json['详情']['保质期'], "")
                                database.execute(query, params)
                                database.commit()
                                print("新增个人护理产品成功")
                            case '删除内容': 
                                database = sqlite3.connect('database.db')
                                query = "DELETE FROM careInfo WHERE (Brand =?) AND (Name =?)"
                                params = (answer_json['详情']['品牌'],answer_json['详情']['类型'])
                                database.execute(query, params)
                                database.commit()
                                print("删除个人护理产品成功")
                                
                    case '备忘录':
                        match operation:
                            case '开启': 
                                database = sqlite3.connect('database.db')
                                query = "UPDATE statusInfo SET State = 1 WHERE Item = 'Tips'"
                                database.execute(query)
                                database.commit()
                                print("备忘录开启成功")
                            case '关闭': 
                                database = sqlite3.connect('database.db')
                                query = "UPDATE statusInfo SET State = 0 WHERE Item = 'Tips'"
                                database.execute(query)
                                database.commit()
                                print("备忘录关闭成功")
                            case '新增内容': 
                                database = sqlite3.connect('database.db')
                                query = "SELECT MAX(TID) + 1 FROM tipsInfo"
                                tid = database.execute(query).fetchone()
                                if tid[0] is None:
                                    tid = 1
                                else:
                                    tid = tid[0]
                                time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                                query = "INSERT INTO tipsInfo (TID, Published, Title, Description) VALUES (?,?,?,?)"
                                params = (tid, time, answer_json['详情']['标题'], answer_json['详情']['内容'])
                                database.execute(query, params)
                                database.commit()
                                print("新增备忘录成功")
                            case '删除内容': 
                                database = sqlite3.connect('database.db')
                                query = "DELETE FROM tipsInfo WHERE (Title =? AND Time =?)"
                                params = (answer_json['详情']['标题'], answer_json['详情']['时间'])
                                database.execute(query, params)
                                database.commit()
                                print("删除备忘录成功")
                                
                    case '新闻':
                        match operation:
                            case '开启': 
                                database = sqlite3.connect('database.db')
                                query = "UPDATE statusInfo SET State = 1 WHERE Item = 'News'"
                                database.execute(query)
                                database.commit()
                                print("新闻开启成功")
                            case '关闭': 
                                database = sqlite3.connect('database.db')
                                query = "UPDATE statusInfo SET State = 0 WHERE Item = 'News'"
                                database.execute(query)
                                database.commit()
                                print("新闻关闭成功")
                                
                    case '相册':
                        match operation:
                            case '开启': 
                                database = sqlite3.connect('database.db')
                                query = "UPDATE statusInfo SET State = 1 WHERE Item = 'Gallery'"
                                database.execute(query)
                                database.commit()
                                print("相册开启成功")
                            case '关闭': 
                                database = sqlite3.connect('database.db')
                                query = "UPDATE statusInfo SET State = 0 WHERE Item = 'Gallery'"
                                database.execute(query)
                                database.commit()
                                print("相册关闭成功")
