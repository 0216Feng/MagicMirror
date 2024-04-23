import requests
import json
from xpinyin import Pinyin
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

# 通过IP获取中文城市名称的拼音
request = requests.get('http://myip.ipip.net/json').json()
if request['data']['location'][2] == '' :
    city = request['data']['location'][1]
else:
    city = request['data']['location'][2]
city_pinyin = Pinyin().get_pinyin(city).replace('-', '')

# 根据城市名称获取当地的天气数据和建议数据
weather_url = 'https://api.seniverse.com/v3/weather/now.json?key=SK4YZCVJgN8brFS0x&location=%s&language=zh-Hans&unit=c' % city_pinyin
suggesion_url = 'https://api.seniverse.com/v3/life/suggestion.json?key=SK4YZCVJgN8brFS0x&location=%s&language=zh-Hans' % city_pinyin
weather_response = requests.get(weather_url)
suggesion_url = requests.get(suggesion_url)
weather_data = json.loads(weather_response.text)
suggestion_data = json.loads(suggesion_url.text)

#提取天气数据和建议数据
city_name = weather_data['results'][0]['location']['name']
weather = weather_data['results'][0]['now']['text']
temperature = weather_data['results'][0]['now']['temperature']
update_time = weather_data['results'][0]['last_update'][:-6].replace('T', ' ')
uv = suggestion_data['results'][0]['suggestion']['uv']['brief']
dressing = suggestion_data['results'][0]['suggestion']['dressing']['brief']
sport = suggestion_data['results'][0]['suggestion']['sport']['brief']

# 天气对应图标
match weather:
    case '晴':
        weather_icon = './black_v4/black_v4/1000@1x.png'
    case '阴':
        weather_icon = './black_v4/black_v4/1003@1x.png' 
    case '多云':
        weather_icon = './black_v4/black_v4/1001@1x.png'
    case '晴间多云':
        weather_icon = './black_v4/black_v4/1004@1x.png'
    case '阵雨':
        weather_icon = './black_v4/black_v4/2020@1x.png'
    case '雷阵雨':
        weather_icon = './black_v4/black_v4/2022@1x.png'
    case '小雨':
        weather_icon = './black_v4/black_v4/2000@1x.png'
    case '中雨':
        weather_icon = './black_v4/black_v4/2002@1x.png'
    case '大雨':
        weather_icon = './black_v4/black_v4/2004@1x.png'
    case '暴雨':
        weather_icon = './black_v4/black_v4/2006@1x.png'
    case '大暴雨' | '特大暴雨':
        weather_icon = './black_v4/black_v4/2008@1x.png'
    case '风' | '大风':
        weather_icon = './black_v4/black_v4/4000@1x.png'
    case '飓风' | '热带风暴':
        weather_icon = './black_v4/black_v4/4021@1x.png'
    case '雾':
        weather_icon = './black_v4/black_v4/5000@1x.png'
    case '霾':
        weather_icon = './black_v4/black_v4/5020@1x.png' 

class Weather(QWidget):
    def __init__(self):
        super(Weather, self).__init__()
        self.setStyleSheet("background-color: black;")
        self.resize(768, 200)
        self.initUI()

    def initUI(self):
        # 设置网格布局
        layout = QGridLayout()
        self.setLayout(layout)
        # 新建天气信息和图标的标签
        weatherInfo = QLabel(self)
        weatherIcon = QLabel(self)
        # 设置天气信息和图标的样式
        weatherInfo.setStyleSheet("color: white; font-size: 25px;")
        icon = QPixmap(weather_icon)
        info = city_name + '\n' + temperature + '°C' + '\n' + weather + '\n' + '上次更新时间：' + update_time + '\n\n' + '紫外线指数：' + uv + '\n' + '穿衣指数：' + dressing + '\n' + '运动建议：' + sport
        weatherIcon.setPixmap(icon)
        weatherInfo.setText(info)
        # 设置天气信息和图标的显示效果和位置
        weatherInfo.setScaledContents(True)
        weatherInfo.adjustSize()
        weatherInfo.setAlignment(Qt.AlignCenter)
        layout.addWidget(weatherIcon, 2, 4, 1, 1)
        layout.addWidget(weatherInfo, 2, 1, 9, 9)
    
''' if __name__ == '__main__':
    app = QApplication(sys.argv)
    weather = Weather()
    weather.show()
    sys.exit(app.exec_()) '''
        



    