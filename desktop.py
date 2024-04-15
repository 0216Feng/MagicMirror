import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from course import Course
from weather import Weather
from makeup import Makeup

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        
        # 设置窗口大小
        self.setGeometry(100, 100, 768, 1366)
        # 设置窗口背景颜色
        self.setStyleSheet("background-color: black;")
        # 无边框
        self.setWindowFlags(
            Qt.Window | Qt.FramelessWindowHint | Qt.WindowSystemMenuHint | Qt.WindowMinimizeButtonHint | Qt.WindowMaximizeButtonHint)

        # 创建一个QLabel控件用于显示时间
        self.time = QLabel(self)
        self.time.setGeometry(20, 20, 400, 100)
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
        # 设置垂直布局
        self.initUI()
    
    def showTime(self):        
        # 获取当前时间
        time = QDateTime.currentDateTime()
        # 设置时间格式
        timeDisplay = time.toString("hh:mm:ss \n yyyy-MM-dd dddd")
        # 在Label上显示时间
        self.time.setText(timeDisplay)
         
    def initUI(self):
        layout = QVBoxLayout()
        layout.addWidget(self.time, stretch=1, alignment=Qt.AlignCenter | Qt.AlignCenter)
        layout.addWidget(self.weather, stretch=1, alignment=Qt.AlignCenter | Qt.AlignCenter)
        layout.addWidget(self.course, stretch=1, alignment=Qt.AlignCenter | Qt.AlignCenter) 
        layout.setSpacing(20)   
        self.setLayout(layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
