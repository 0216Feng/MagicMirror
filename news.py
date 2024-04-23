import urllib
import urllib.parse
import urllib.request
import sys
import json
import importlib
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

def getNews():
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
                news_list = []  # 保存多条新闻的列表
                for i in range(5):  # 遍历获取前 5 条新闻
                    if i < len(data):  # 确保索引没有超出新闻数据的范围
                        news_item = "新闻标题：" + data[i]['title'] + "\n" + "新闻时间：" + data[i]['date'] + "\n\n"
                        news_list.append(news_item)

                if news_list:
                    return ''.join(news_list)  # 返回多条新闻的文本
                else:
                    return "未能获取到新闻内容"
        except Exception as e:
            return("解析结果异常：%s" % e)
    else:
        # 网络异常等问题，无法获取返回内容
        return("请求异常")
    
class News(QWidget):
    def __init__(self):
        super(News, self).__init__()
        self.initUI()
        
    def initUI(self):
        self.resize(768, 1200)
        news = QLabel()
        layout = QVBoxLayout()
        news.setText(getNews())
        news.setStyleSheet("color: white; font-size: 20px;")
        self.setLayout(layout)
        layout.addWidget(news)
        
''' if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = News()
    ex.show()
    sys.exit(app.exec_()) '''