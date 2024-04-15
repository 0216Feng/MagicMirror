import sys
from flask import Flask, request
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

#@app.route('/course', methods=['GET', 'POST'])
#courseInfo = request.form.get('courseInfo')

#课表信息
courseInfo = [
                {'courseName': '人机交互', 'time': '9:00-11:50', 'location': 'C305', 'week': '星期一'},
                {'courseName': '计算机网络', 'time': '12:30-15:20', 'location': 'C309', 'week': '星期一'},
                {'courseName': '软件项目管理', 'time': '15:30-18:20', 'location': 'C305', 'week': '星期二'},
                {'courseName': '人工智能', 'time': '9:00-11:50', 'location': 'C309', 'week': '星期三'},
                {'courseName': '计算机网络实验', 'time': '12:30-15:20', 'location': 'C305', 'week': '星期四'},
             ]
# 星期对应表格的行数，时间对应表格的列数
weekdays = {'星期一': 0, '星期二': 1, '星期三': 2, '星期四': 3, '星期五': 4, '星期六': 5, '星期日': 6}
timeFrame = {'9:00-11:50': 0, '12:30-15:20': 1, '15:30-18:20': 2, '19:00-21:50': 3}
# 提取课表信息中的日期和时间
date = [0] * len(courseInfo)
time = [0] * len(courseInfo)
for i in range(len(courseInfo)):
    date[i] = weekdays[courseInfo[i]['week']]
    time[i] = timeFrame[courseInfo[i]['time']]

class Course(QWidget):
    def __init__(self):
        super(Course, self).__init__()
        self.setGeometry(40, 40, 768, 400)
        self.initUI()
        
    def initUI(self):
        table = QTableWidget()
        layout = QHBoxLayout()
        table.setRowCount(4)
        table.setColumnCount(7)
        layout.addWidget(table)
        table.setHorizontalHeaderLabels(['星期一', '星期二', '星期三', '星期四', '星期五', '星期六', '星期日'])
        table.setVerticalHeaderLabels(['9:00-11:50', '12:30-15:20', '15:30-18:20', '19:00-21:50'])
        # 自动调整行高
        table.resizeRowsToContents()
        # 自动换行
        table.setWordWrap(True)
        # 填充课表信息
        for i in range(len(courseInfo)):
            table.setItem(date[i], time[i], QTableWidgetItem(courseInfo[i]['courseName'] + '\n' + courseInfo[i]['location']))
        #table.setStyleSheet("color: white;")
        # 自动调整列宽
        table.resizeRowsToContents()
        
        self.setLayout(layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    table = Course()
    table.show()
    sys.exit(app.exec_())