from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sqlite3
import sys

# 连接数据库
database = sqlite3.connect('database.db')
query = "SELECT * FROM scheduleInfo"
result = database.execute(query)
# 读取数据
dailyInfo = []
for row in result.fetchall():
    dailyInfo.append({'affair': row[1], 'time': row[2], 'location': row[3], 'description': row[4]})
    
class Update(QObject):
    update_data = pyqtSignal()
    def __init__(self):
        super(Update, self).__init__()
        # 创建一个定时器，每隔一定时间检查数据库数据变化
        self.timer = QTimer()
        self.timer.timeout.connect(self.checkDatabase)
        self.timer.start(5000)  # 每隔5秒检查一次     
        
    def checkDatabase(self):
        global dailyInfo
        # 连接数据库
        database = sqlite3.connect('database.db')
        query = "SELECT * FROM scheduleInfo"
        result = database.execute(query)
        # 读取数据
        temp = []
        for row in result.fetchall():
            temp.append({'affair': row[1], 'time': row[2], 'location': row[3], 'description': row[4]})
        if temp != dailyInfo:  
            dailyInfo = temp
            self.update_data.emit()

class Daily(QWidget):
    def __init__(self):
        super(Daily, self).__init__()
        self.resize(768, 400)
        self.initUI()
        self.update = Update()
        self.update.update_data.connect(self.updateTable)
        
    def initUI(self):
        table = QTableWidget()
        layout = QHBoxLayout()
        table.setRowCount(len(dailyInfo))
        table.setColumnCount(4)
        layout.addWidget(table)
        # 设置表头(行为日期，列为时间)
        table.setHorizontalHeaderLabels(['事务', '时间', '地点', '描述'])
        table.horizontalHeader().setStyleSheet("QHeaderView::section{font:12pt 'Arial';color: white;};") # 设置表头字体和颜色
        table.verticalHeader().setVisible(False)
        # 自动调整行高
        table.resizeRowsToContents()
        # 自动换行
        table.setWordWrap(True)
        # 填充日程表信息
        for i in range(len(dailyInfo)):
            table.setItem(i, 0, QTableWidgetItem(dailyInfo[i]['affair']))
            table.item(i, 0).setTextAlignment(Qt.AlignCenter) # 设置单元格居中
            table.setItem(i, 1, QTableWidgetItem(dailyInfo[i]['time']))
            table.item(i, 1).setTextAlignment(Qt.AlignCenter) # 设置单元格居中
            table.setItem(i, 2, QTableWidgetItem(dailyInfo[i]['location']))
            if table.item(i, 2) is not None:
                table.item(i, 2).setTextAlignment(Qt.AlignCenter) # 设置单元格居中
            table.setItem(i, 3, QTableWidgetItem(dailyInfo[i]['description']))
            if table.item(i, 3) is not None:
                table.item(i, 3).setTextAlignment(Qt.AlignCenter) # 设置单元格居中
        # 设置字体大小和颜色
        table.setStyleSheet("color: white; font-size: 20px;")
        # 自动调整行高列宽
        table.resizeRowsToContents()
        table.resizeColumnsToContents()
        self.setLayout(layout)
    
    def updateTable(self):
        # 获取表格
        table = self.layout().itemAt(0).widget()
        # 更新行数
        table.setRowCount(len(dailyInfo))
        # 清空表格
        for i in range(table.rowCount()):
            for j in range(table.columnCount()):
                table.setItem(i, j, QTableWidgetItem())
        # 填充日程表信息
        for i in range(len(dailyInfo)):
            table.setItem(i, 0, QTableWidgetItem(dailyInfo[i]['affair']))
            table.item(i, 0).setTextAlignment(Qt.AlignCenter) # 设置单元格居中
            table.setItem(i, 1, QTableWidgetItem(dailyInfo[i]['time']))
            table.item(i, 1).setTextAlignment(Qt.AlignCenter) # 设置单元格居中
            table.setItem(i, 2, QTableWidgetItem(dailyInfo[i]['location']))
            if table.item(i, 2) is not None: # 防止空单元格报错
                table.item(i, 2).setTextAlignment(Qt.AlignCenter) # 设置单元格居中
            table.setItem(i, 3, QTableWidgetItem(dailyInfo[i]['description']))
            if table.item(i, 3) is not None: # 防止空单元格报错
                table.item(i, 3).setTextAlignment(Qt.AlignCenter) # 设置单元格居中

''' if __name__ == '__main__':
    app = QApplication(sys.argv)
    table = Daily()
    table.show()
    sys.exit(app.exec_()) '''
