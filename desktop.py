import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from course import Course
from weather import Weather
from selfcare import SelfCare
import qdarkstyle

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        
        # 设置窗口大小
        self.setGeometry(400, 0, 768, 1366) #屏幕竖屏分辨率为768*1366
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
        # 创建个人护理产品组件
        self.selfcare = SelfCare()
        # 设置垂直布局
        self.initUI()
    
    def showTime(self):        
        # 获取当前时间
        time = QDateTime.currentDateTime()
        # 设置时间格式
        timeDisplay = time.toString("hh:mm:ss \n yyyy-MM-dd dddd")
        # 在Label上显示时间
        self.time.setText(timeDisplay)
        self.time.setFont(QFont("Arial", 20))
         
    def initUI(self):
        # 设置垂直布局
        self.layout = QVBoxLayout()
        # 时间组件居中
        self.time.setAlignment(Qt.AlignCenter | Qt.AlignCenter)
        # 添加组件到布局
        self.layout.addWidget(self.time)
        self.layout.addWidget(self.weather)
        self.layout.addWidget(self.course) 
        self.layout.addWidget(self.selfcare)
        self.layout.setSpacing(20)   
        # 设置主窗口的布局
        mainWidget = QWidget()
        mainWidget.setLayout(self.layout)
        self.setCentralWidget(mainWidget)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='pyqt5'))
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
