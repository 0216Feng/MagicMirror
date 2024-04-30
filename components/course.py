from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sqlite3
import sys

# 连接数据库
database = sqlite3.connect('database.db')
query = "SELECT * FROM courseInfo"
result = database.execute(query)
# 读取数据
courseInfo = []
for row in result.fetchall():
    courseInfo.append({'courseName': row[1], 'time': row[2], 'location': row[3], 'week': row[4]})

#课表信息
'''courseInfo = [
                {'courseName': '人机交互', 'time': '9:00-11:50', 'location': 'C305', 'week': '星期一'},
                {'courseName': '计算机网络', 'time': '12:30-15:20', 'location': 'C309', 'week': '星期一'},
                {'courseName': '软件项目管理', 'time': '15:30-18:20', 'location': 'B401', 'week': '星期二'},
                {'courseName': '人工智能', 'time': '9:00-11:50', 'location': 'B602', 'week': '星期三'},
                {'courseName': '计算机网络实验', 'time': '12:30-15:20', 'location': 'C408', 'week': '星期四'}
             ]'''
# 星期对应表格的行数，时间对应表格的列数
weekdays = {'星期一': 0, '星期二': 1, '星期三': 2, '星期四': 3, '星期五': 4, '星期六': 5, '星期日': 6}
timeFrame = {'9:00-11:50': 0, '12:30-15:20': 1, '15:30-18:20': 2, '19:00-21:50': 3}
# 提取课表信息中的日期和时间
date = [] 
time = [] 
for i in range(len(courseInfo)):
    date.append(weekdays[courseInfo[i]['week']])
    time.append(timeFrame[courseInfo[i]['time']])

class Update(QObject):
    update_data = pyqtSignal()
    def __init__(self):
        super(Update, self).__init__()
        # 创建一个定时器，每隔一定时间检查数据库数据变化
        self.timer = QTimer()
        self.timer.timeout.connect(self.checkDatabase)
        self.timer.start(5000)  # 每隔5秒检查一次     
        
    def checkDatabase(self):
        global courseInfo, date, time
        # 连接数据库
        database = sqlite3.connect('database.db')
        query = "SELECT * FROM courseInfo"
        result = database.execute(query)
        # 读取数据
        temp = []
        temp_date = []
        temp_time = [] 
        for row in result.fetchall():
            temp.append({'courseName': row[1], 'time': row[2], 'location': row[3], 'week': row[4]})  
        for i in range(len(temp)):
            temp_date.append(weekdays[temp[i]['week']])
            temp_time.append(timeFrame[temp[i]['time']]) 
        if temp != courseInfo:  
            courseInfo = temp
            date.clear()  # 清空原有数据
            time.clear()  # 清空原有数据
            date.extend(temp_date)  # 将新的日期数据添加到date中
            time.extend(temp_time)  # 将新的时间数据添加到time中
            self.update_data.emit()
            

class Course(QWidget):
    def __init__(self):
        super(Course, self).__init__()
        self.resize(768, 300)
        self.initUI()
        self.update = Update()
        self.update.update_data.connect(self.updateTable)
            
    def initUI(self):
        table = QTableWidget()
        layout = QHBoxLayout()
        table.setRowCount(4)
        table.setColumnCount(5)
        layout.addWidget(table)
        # 设置表头(行为日期，列为时间)
        table.setHorizontalHeaderLabels(['星期一', '星期二', '星期三', '星期四', '星期五'])
        table.setVerticalHeaderLabels(['9:00-11:50', '12:30-15:20', '15:30-18:20', '19:00-21:50'])
        table.horizontalHeader().setStyleSheet("QHeaderView::section{font:12pt 'Arial';color: white;};") # 设置表头字体和颜色
        table.verticalHeader().setStyleSheet("QHeaderView::section{font:12pt 'Arial';color: white;};")
        # 自动调整行高
        table.resizeRowsToContents()
        # 自动换行
        table.setWordWrap(True)
        # 填充课表信息
        for i in range(len(courseInfo)):
            table.setItem(time[i], date[i], QTableWidgetItem(courseInfo[i]['courseName'] + '\n' + courseInfo[i]['location']))
            table.item(time[i], date[i]).setTextAlignment(Qt.AlignCenter) # 设置单元格居中
        table.setStyleSheet("color: white; font-size: 20px;")
        # 自动调整行高列宽
        table.resizeRowsToContents()
        table.resizeColumnsToContents()
        table.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setLayout(layout)
        
    def updateTable(self):
        # 获取表格
        table = self.layout().itemAt(0).widget()
        # 清空表格
        for i in range(table.rowCount()):
            for j in range(table.columnCount()):
                table.setItem(i, j, QTableWidgetItem())
        # 填充课表信息
        for i in range(len(courseInfo)):
            table.setItem(time[i], date[i], QTableWidgetItem(courseInfo[i]['courseName'] + '\n' + courseInfo[i]['location']))
            table.item(time[i], date[i]).setTextAlignment(Qt.AlignCenter) # 设置单元格居中

''' if __name__ == '__main__':
    app = QApplication(sys.argv)
    table = Course()
    table.show()
    sys.exit(app.exec_()) '''