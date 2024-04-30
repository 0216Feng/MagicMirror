from Lib.SlidingStackedWidget import SlidingStackedWidget
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import os

class Gallery(QWidget):
    def __init__(self, parent=None):
        super(Gallery, self).__init__(parent)
        self.setWindowTitle("Gallery")
        
        # 新建一个堆叠窗口
        stackedWidget = SlidingStackedWidget(self)
        self.stackedWidget = stackedWidget
        # 设置布局
        layout = QHBoxLayout()
        layout.addWidget(stackedWidget)
        self.setLayout(layout)
        # 添加图片页面
        for name in os.listdir('./assets'):
            label = QLabel(self.stackedWidget)
            label.setScaledContents(True)
            label.setPixmap(QPixmap('./assets/' + name))
            label.setScaledContents(True) # 图片自适应大小
            label.setMaximumSize(768, 400) # 限制图片最大尺寸
            self.stackedWidget.addWidget(label)
        # 设置自动播放(可调整间隔时间，10000ms=10s，以此类推)    
        self.stackedWidget.autoStart(10000)
            
''' if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Gallery()
    w.show()
    sys.exit(app.exec_()) '''
