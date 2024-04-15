import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class Mytable(QWidget):
    def __init__(self) -> None:
        super(Mytable, self).__init__()
        self.setGeometry(400, 200, 1200, 600)
        self.tables()
        self.initUI()

    def tables(self):
        # 创建tableWidget，设置行、列数
        self.tbwidget = QTableWidget()
        self.tbwidget.setRowCount(3)
        self.tbwidget.setColumnCount(4)

        # 设置表格属性
        # 调整列和行的大小
        self.tbwidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tbwidget.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
        # 垂直表头不显示
        self.tbwidget.verticalHeader().setVisible(False)

        # 隐藏滚动条
        self.tbwidget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tbwidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        # set table header
        list_title = ['Name', 'Gender', 'age', 'Deptment']
        self.tbwidget.setHorizontalHeaderLabels(list_title)

        # Give data to cells of 1st row
        self.tbwidget.setItem(0, 0, QTableWidgetItem("John"))
        self.tbwidget.setItem(0, 1, QTableWidgetItem("男"))
        self.tbwidget.setItem(0, 2, QTableWidgetItem("24"))
        self.tbwidget.setItem(0, 3, QTableWidgetItem("销售部"))
        # Give data to cells of 2nd row
        self.tbwidget.setItem(1, 0, QTableWidgetItem("Mary"))
        self.tbwidget.setItem(1, 1, QTableWidgetItem("女"))
        self.tbwidget.setItem(1, 2, QTableWidgetItem("29"))
        self.tbwidget.setItem(1, 3, QTableWidgetItem("财务部"))
        # Give data to cells of 3rd row
        self.tbwidget.setItem(2, 0, QTableWidgetItem("王勇"))
        self.tbwidget.setItem(2, 1, QTableWidgetItem("男"))
        self.tbwidget.setItem(2, 2, QTableWidgetItem("30"))
        self.tbwidget.setItem(2, 3, QTableWidgetItem("运营部"))

    def initUI(self):
        # Create layout elements
        self.vbox_0 = QVBoxLayout()
        self.vbox_1 = QVBoxLayout()
        self.hbox_1 = QHBoxLayout()

        # set vbox_1 layout
        self.vbox_1.addWidget(self.tbwidget)

        # set hbox_1 layer
        label_1 = QLabel('OK')
        label_2 = QLabel('Cancel')
        self.hbox_1.addWidget(label_1, alignment=Qt.AlignCenter)
        self.hbox_1.addWidget(label_2, alignment=Qt.AlignCenter)

        # set base layout vbox_0
        self.vbox_0.addLayout(self.vbox_1)
        self.vbox_0.addLayout(self.hbox_1)

        # Apply vobox_0 into mainWindow
        self.setLayout(self.vbox_0)


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_gui()
        self.setGeometry(400, 150, 800, 300)

    def init_gui(self):
        """主窗口显示自定义MyTable Widget
        Notice: 
            不能使用主窗口layout， 否则 table 显示不出来
        Stpes:
            (1) 创建 mytable 实例, 用 setCentralWidgets 设置为窗口的中心控件
            (2) 创建 布局变量，分配给 mytable
            (3) 创建 主窗口的控件，加入 layout 
            (4) mainwindow 不需要指定布局方式,由 myTable完成
        """
        self.mytable = Mytable()
        self.layout = QVBoxLayout()
        self.setCentralWidget(self.mytable)
        self.mytable.setLayout(self.layout)

        self.textbox = QLineEdit('please into text')
        self.echo_label = QLabel('评论')
        self.echo_label.setBuddy(self.textbox)

        # 将窗口控件加入 mytable 的布局
        self.hbox_win = QHBoxLayout()
        self.hbox_win.addWidget(
            self.echo_label)
        self.hbox_win.addWidget(
            self.textbox)
        self.mytable.layout().addLayout(self.hbox_win)

        # self.mytable.layout().addWidget(self.echo_label)
        # self.mytable.layout().addWidget(self.textbox)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())