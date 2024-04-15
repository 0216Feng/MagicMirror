import sys
from flask import Flask, request
from PyQt5.QtWidgets import *
import datetime
#@app.route('/course', methods=['GET', 'POST'])
#courseInfo = request.form.get('MakeupInfo')

#护肤品信息
makeupInfo = [
                {'brand': '海洋至尊', 'type': '洗面奶', 'expire': '2027-01-31'},
                {'brand': 'iLab', 'type': '面霜', 'expire': '2025-05-25'},
                {'brand': '科颜氏', 'type': '爽肤水', 'expire': '2025-01-01'},
                {'brand': '科颜氏', 'type': '面膜', 'expire': '2025-01-01'},
             ]

# 计算距离过期时间
def get_expire_date(date_str):
    expire_date = datetime.datetime.strptime(date_str, '%Y-%m-%d')
    today = datetime.datetime.now()
    delta = expire_date - today
    return delta.days

class Makeup(QWidget):
    def __init__(self):
        super(Makeup, self).__init__()
        self.setGeometry(40, 40, 768, 400)
        self.initUI()
        
    def initUI(self):
        table = QTableWidget()
        layout = QHBoxLayout()
        table.setRowCount(len(makeupInfo))
        table.setColumnCount(3)
        layout.addWidget(table)
        table.setHorizontalHeaderLabels(['品牌', '类型', '距离过期还有'])
        table.verticalHeader().setVisible(False)
        for i in range(len(makeupInfo)):
            table.setItem(i, 0, QTableWidgetItem(makeupInfo[i]['brand']))
            table.setItem(i, 1, QTableWidgetItem(makeupInfo[i]['type']))
            table.setItem(i, 2, QTableWidgetItem(str(get_expire_date(makeupInfo[i]['expire'])) + '天'))
        table.setStyleSheet("color: white;")
        self.setLayout(layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    table = Makeup()
    table.show()
    sys.exit(app.exec_())