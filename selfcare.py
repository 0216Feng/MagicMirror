from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import datetime
from flask import Flask, request

#@app.route('/course', methods=['GET', 'POST'])
#courseInfo = request.form.get('MakeupInfo')

#个人护理产品信息
Info = [
                {'brand': '海洋至尊', 'type': '洗面奶', 'expire': '2027-02-27'},
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

class SelfCare(QWidget):
    def __init__(self):
        super(SelfCare, self).__init__()
        self.resize(768, 200)
        self.initUI()
        
    def initUI(self):
        # 设置水平布局
        table = QTableWidget()
        layout = QHBoxLayout()
        # 设置表格行列数
        table.setRowCount(len(Info))
        table.setColumnCount(3)
        layout.addWidget(table)
        # 设置表头
        table.setHorizontalHeaderLabels(['品牌', '类型', '距离过期还有'])
        table.horizontalHeader().setStyleSheet("QHeaderView::section{font:12pt 'Arial';color: white;};") # 设置表头字体和颜色
        table.verticalHeader().setVisible(False)
        # 设置单元格内容
        for i in range(len(Info)):
            table.setItem(i, 0, QTableWidgetItem(Info[i]['brand']))
            table.item(i, 0).setTextAlignment(Qt.AlignCenter) # 设置单元格居中
            table.setItem(i, 1, QTableWidgetItem(Info[i]['type']))
            table.item(i, 1).setTextAlignment(Qt.AlignCenter) # 设置单元格居中
            table.setItem(i, 2, QTableWidgetItem(str(get_expire_date(Info[i]['expire'])) + '天'))
            table.item(i, 2).setTextAlignment(Qt.AlignCenter) # 设置单元格居中
        table.setStyleSheet("color: white; font-size: 20px;")
        self.setLayout(layout)

''' if __name__ == '__main__':
    app = QApplication(sys.argv)
    table = SelfCare()
    table.show()
    sys.exit(app.exec_()) '''