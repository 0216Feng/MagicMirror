from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sqlite3

# 连接数据库
database = sqlite3.connect('database.db')
query = "SELECT * FROM tipsInfo"
result = database.execute(query)
# 读取数据
tipsInfo = []
for row in result.fetchall():
    tipsInfo.append({'title': row[2], 'text': row[3], 'time': row[1]})

#tipsComponet = {'title': "School", 'text': "Tips: Remember to bring homework at Wednesday's Artificial Intelligence class.", 'time':"2024-04-15 14:00:00"}

class Tips(QWidget):
    def __init__(self):
        super(Tips, self).__init__()
        self.resize(768, 200)
        self.initUI()
        
    def initUI(self):
        # 创建备忘录标签并设置水平布局
        tips = QLabel()
        layout = QHBoxLayout()
        # 设置提示信息
        tipsText = ""
        for i in range(len(tipsInfo)):
            if i != len(tipsInfo) - 1:
                tipsText += tipsInfo[i]['title'] + "\n" + tipsInfo[i]['text'] + "\n" + tipsInfo[i]['time'] + "\n\n"
            else:
                tipsText += tipsInfo[i]['title'] + "\n" + tipsInfo[i]['text'] + "\n" + tipsInfo[i]['time']
        tips.setText(tipsText)
        tips.setStyleSheet("color: white; font-size: 25px;")
        # 设置自动换行
        tips.setWordWrap(True) 
        # 备忘录加入布局
        self.setLayout(layout)
        layout.addWidget(tips)