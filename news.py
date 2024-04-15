import urllib
import urllib.parse
import urllib.request
import sys
import json
import importlib

importlib.reload(sys)

url = 'http://v.juhe.cn/toutiao/index'

params = {
    "type": "top",  # 头条类型,top(头条，默认),shehui(社会),guonei(国内),guoji(国际),yule(娱乐),tiyu(体育)junshi(军事),keji(科技),caijing(财经),shishang(时尚)
    "key": "f9e9b410f2e16165b65ee6b0cd667332",  # API接口请求Key
}
query = urllib.parse.urlencode(params).encode('utf-8')

request = urllib.request.Request(url, data=query)
response = urllib.request.urlopen(request)
content = response.read()
if (content):
    try:
        result = json.loads(content)
        error_code = result['error_code']
        if (error_code == 0):
            data = result['result']['data']
            for i in data:
                # 更多字段可参考接口文档 https://www.juhe.cn/docs/api/id/235
                print("新闻标题：%s\n新闻时间：%s\n新闻链接：%s\n\n" % (i['title'], i['date'], i['url']))
        else:
            print("请求失败:%s %s" % (result['error_code'], result['reason']))
    except Exception as e:
        print("解析结果异常：%s" % e)
else:
    # 网络异常等问题，无法获取返回内容
    print("请求异常")