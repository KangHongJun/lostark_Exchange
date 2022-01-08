from PyQt5.QtWidgets import *
import Function

Reforging = Function.Reforging_Data()
Reforging_Add = Function.Reforging_Add_Data()

def SetTable(self,list):
    i = 0
    for col, row in list:
        row = str(row)
        name = QTableWidgetItem(col)
        price = QTableWidgetItem(row)
        self.tableWidget.setItem(i, 0, name)
        self.tableWidget.setItem(i, 1, price)
        i = i + 1

def low0(self):
    self.tableWidget = QTableWidget(self)
    self.tableWidget.setRowCount(53)
    self.tableWidget.setColumnCount(2)
    column_headers = ['아이템명', '가격']
    self.tableWidget.setHorizontalHeaderLabels(column_headers)

    SetTable(self,Reforging + Reforging_Add)

    layout = QFormLayout()
    label1 = QLabel()
    layout.addWidget(label1)
    layout.addWidget(self.tableWidget)

    self.low0.setLayout(layout)

def low1(self):
    self.tableWidget = QTableWidget(self)
    self.tableWidget.setColumnCount(2)
    self.tableWidget.setRowCount(21)
    column_headers = ['아이템명','가격']
    self.tableWidget.setHorizontalHeaderLabels(column_headers)

    SetTable(self,Reforging)

    layout = QFormLayout()
    label1 = QLabel()
    layout.addWidget(label1)
    layout.addWidget(self.tableWidget)

    self.low1.setLayout(layout)

def low2(self):
    self.tableWidget = QTableWidget(self)
    self.tableWidget.setRowCount(32)
    self.tableWidget.setColumnCount(2)
    column_headers = ['아이템명', '가격']
    self.tableWidget.setHorizontalHeaderLabels(column_headers)

    SetTable(self,Reforging_Add)

    layout = QFormLayout()
    label1 = QLabel()
    layout.addWidget(label1)
    layout.addWidget(self.tableWidget)

    self.low2.setLayout(layout)