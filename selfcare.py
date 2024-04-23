from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import datetime
import sqlite3
import sys

# 连接数据库
database = sqlite3.connect('database.db')
query = "SELECT * FROM careInfo"
result = database.execute(query)
# 读取数据
careInfo = []
for row in result.fetchall():
    careInfo.append({'brand': row[1], 'type': row[2], 'expire': row[3]})

#个人护理产品信息
'''Info = [
            {'brand': '海洋至尊', 'type': '洗面奶', 'expire': '2027-02-27'},
            {'brand': 'iLab', 'type': '面霜', 'expire': '2025-05-25'},
            {'brand': '科颜氏', 'type': '爽肤水', 'expire': '2025-01-01'},
            {'brand': '科颜氏', 'type': '面膜', 'expire': '2025-01-01'}
        ]'''

# 计算距离过期时间
def get_expire_date(date_str):
    expire_date = datetime.datetime.strptime(date_str, '%Y-%m-%d')
    today = datetime.datetime.now()
    delta = expire_date - today
    return delta.days

class Update(QObject):
    update_data = pyqtSignal()
    def __init__(self):
        super(Update, self).__init__()
        # 创建一个定时器，每隔一定时间检查数据库数据变化
        self.timer = QTimer()
        self.timer.timeout.connect(self.checkDatabase)
        self.timer.start(5000)  # 每隔5秒检查一次     
        
    def checkDatabase(self):
        global careInfo
        # 连接数据库
        database = sqlite3.connect('database.db')
        query = "SELECT * FROM careInfo"
        result = database.execute(query)
        # 读取数据
        temp = []
        for row in result.fetchall():
            temp.append({'brand': row[1], 'type': row[2], 'expire': row[3]}) 
        if temp != careInfo:  
            careInfo = temp
            self.update_data.emit()

class SelfCare(QWidget):
    def __init__(self):
        super(SelfCare, self).__init__()
        self.resize(768, 400)
        self.initUI()
        self.update = Update()
        self.update.update_data.connect(self.updateData)
        
    def initUI(self):
        # 设置水平布局
        table = QTableWidget()
        layout = QHBoxLayout()
        # 设置表格行列数
        table.setRowCount(len(careInfo))
        table.setColumnCount(3)
        layout.addWidget(table)
        # 设置表头
        table.setHorizontalHeaderLabels(['品牌', '类型', '距离过期还有'])
        table.horizontalHeader().setStyleSheet("QHeaderView::section{font:12pt 'Arial';color: white;};") # 设置表头字体和颜色
        table.verticalHeader().setVisible(False)
        # 设置单元格内容
        for i in range(len(careInfo)):
            table.setItem(i, 0, QTableWidgetItem(careInfo[i]['brand']))
            table.item(i, 0).setTextAlignment(Qt.AlignCenter) # 设置单元格居中
            table.setItem(i, 1, QTableWidgetItem(careInfo[i]['type']))
            table.item(i, 1).setTextAlignment(Qt.AlignCenter) # 设置单元格居中
            table.setItem(i, 2, QTableWidgetItem(str(get_expire_date(careInfo[i]['expire'])) + '天'))
            table.item(i, 2).setTextAlignment(Qt.AlignCenter) # 设置单元格居中
        table.setStyleSheet("color: white; font-size: 20px;")
        table.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setLayout(layout)
        
    def updateData(self):
        # 获取表格
        table = self.layout().itemAt(0).widget()
        # 更新行数
        table.setRowCount(len(careInfo))
        # 清空表格
        for i in range(table.rowCount()):
            for j in range(table.columnCount()):
                table.setItem(i, j, QTableWidgetItem())
        # 填充日程表信息
        for i in range(len(careInfo)):
            table.setItem(i, 0, QTableWidgetItem(careInfo[i]['brand']))
            table.item(i, 0).setTextAlignment(Qt.AlignCenter) # 设置单元格居中
            table.setItem(i, 1, QTableWidgetItem(careInfo[i]['type']))
            table.item(i, 1).setTextAlignment(Qt.AlignCenter) # 设置单元格居中
            table.setItem(i, 2, QTableWidgetItem(str(get_expire_date(careInfo[i]['expire'])) + '天'))
            table.item(i, 2).setTextAlignment(Qt.AlignCenter) # 设置单元格居中

''' if __name__ == '__main__':
    app = QApplication(sys.argv)
    table = SelfCare()
    table.show()
    sys.exit(app.exec_()) '''