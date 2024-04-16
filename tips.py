from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class Tips(QWidget):
    def __init__(self):
        super(Tips, self).__init__()
        self.resize(300, 100)
        
    def initUI(self):
        tips = QLabel()
        tips.setText("Tips: Remember to bring homework at Wednesday's class.")