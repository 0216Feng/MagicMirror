import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from course import Course
from weather import Weather
from selfcare import SelfCare
from daily import Daily
from tips import Tips
from news import News
from gallery import Gallery
import qdarkstyle
import sqlite3

# 连接数据库
database = sqlite3.connect('database.db')
query = "SELECT * FROM statusInfo"
result = database.execute(query)
# 读取数据
statusInfo = []
for row in result.fetchall():
    statusInfo.append({'component': row[0], 'status': row[1]})

class Update(QObject):
    update_data = pyqtSignal()
    def __init__(self):
        super(Update, self).__init__()
        # 创建一个定时器，每隔一定时间检查数据库数据变化
        self.timer = QTimer()
        self.timer.timeout.connect(self.checkDatabase)
        self.timer.start(5000)  # 每隔5秒检查一次     
        
    def checkDatabase(self):
        global statusInfo
        database = sqlite3.connect('database.db')
        query = "SELECT * FROM statusInfo"
        result = database.execute(query)
        # 读取数据
        temp = []
        for row in result.fetchall():
            temp.append({'component': row[0], 'status': row[1]})       
        if temp != statusInfo:  
            statusInfo = temp
            self.update_data.emit()   
    
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        
        # 设置窗口大小
        self.setGeometry(0, 0, 768, 1366) #屏幕竖屏分辨率为768*1366
        # 设置窗口背景颜色
        self.setStyleSheet("background-color: black;")
        # 无边框
        self.setWindowFlags(
            Qt.Window | Qt.FramelessWindowHint | Qt.WindowSystemMenuHint | Qt.WindowMinimizeButtonHint | Qt.WindowMaximizeButtonHint)

        # 创建一个QLabel控件用于显示时间
        self.time = QLabel(self)
        self.time.resize(400, 100)
        self.time.setStyleSheet("color: white; font-size: 30px;")
        # 每秒刷新一次时间
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start()
        # 显示时间
        self.showTime()
        # 创建天气组件
        self.weather = Weather()
        # 创建课程表组件
        self.course = Course()
        self.course.setMinimumSize(768, 300)
        # 创建个人护理产品组件
        self.selfcare = SelfCare()
        self.selfcare.setMinimumSize(768, 200)
        # 创建备忘录组件
        self.tips = Tips()
        # 创建日程表组件
        self.daily = Daily()
        self.daily.setMinimumSize(768, 300)
        # 创建新闻组件
        self.news = News() 
        # 创建相册组件
        self.gallery = Gallery()
        self.gallery.setMaximumSize(768,432)    
        # 检查数据库数据变化并更新UI
        self.initUI()
        self.update = Update()
        self.update.update_data.connect(self.updateUI)
                 
    
    def showTime(self):        
        # 获取当前时间
        time = QDateTime.currentDateTime()
        # 设置时间格式
        timeDisplay = time.toString("hh:mm:ss \n yyyy-MM-dd dddd")
        # 在Label上显示时间
        self.time.setText(timeDisplay)
         
    def initUI(self):
        # 设置垂直布局
        self.layout = QVBoxLayout()
        # 时间组件居中
        self.time.setAlignment(Qt.AlignCenter | Qt.AlignCenter)
        # 根据后台返回的状态信息，添加组件到布局
        self.layout.addWidget(self.time)
        self.layout.addWidget(self.weather)
        self.layout.setSpacing(20)   
        self.setLayout()
        # 设置主窗口的布局
        mainWidget = QWidget()
        mainWidget.setLayout(self.layout)
        self.setCentralWidget(mainWidget)
        
    def setLayout(self):
        if statusInfo[1]['status'] == 1:
            self.layout.addWidget(self.news)
        if statusInfo[2]['status'] == 1: 
            self.layout.addWidget(self.course)
        if statusInfo[3]['status'] == 1: 
            self.layout.addWidget(self.daily)
        if statusInfo[5]['status'] == 1: 
            self.layout.addWidget(self.selfcare)
        if statusInfo[4]['status'] == 1:
            self.layout.addWidget(self.tips)
        if statusInfo[6]['status'] == 1:
            self.layout.addWidget(self.gallery)
            
    def updateUI(self):
        print(statusInfo)
        # 移除原有的组件
        if statusInfo[2]['status'] == 0:
            self.layout.removeWidget(self.course)
            self.course.setParent(None)
        if statusInfo[3]['status'] == 0:
            self.layout.removeWidget(self.daily)
            self.daily.setParent(None)
        if statusInfo[5]['status'] == 0:
            self.layout.removeWidget(self.selfcare)
            self.selfcare.setParent(None)
        if statusInfo[4]['status'] == 0:
            self.layout.removeWidget(self.tips)
            self.tips.setParent(None)
        if statusInfo[1]['status'] == 0:
            self.layout.removeWidget(self.news)
            self.news.setParent(None)
        if statusInfo[6]['status'] == 0:
            self.layout.removeWidget(self.gallery)
            self.gallery.setParent(None)
        # 重新设置布局
        self.layout.addStretch(1)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0) 
        self.setLayout() 
        mainWidget = QWidget()
        mainWidget.setLayout(self.layout)
        self.setCentralWidget(mainWidget)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='pyqt5'))
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
