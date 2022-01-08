from PyQt5.QtWidgets import *

def low0(self):
    self.tableWidget = QTableWidget(self)
    self.tableWidget.setRowCount(53)
    self.tableWidget.setColumnCount(2)

    layout = QFormLayout()
    label1 = QLabel()
    layout.addWidget(label1)
    layout.addWidget(self.tableWidget)

    self.low0.setLayout(layout)

def low1(self):
    self.tableWidget = QTableWidget(self)
    self.tableWidget.setRowCount(21)
    self.tableWidget.setColumnCount(2)

    layout = QFormLayout()
    label1 = QLabel()
    layout.addWidget(label1)
    layout.addWidget(self.tableWidget)

    self.low1.setLayout(layout)

def low2(self):
    self.tableWidget = QTableWidget(self)
    self.tableWidget.setRowCount(32)
    self.tableWidget.setColumnCount(2)

    layout = QFormLayout()
    label1 = QLabel()
    layout.addWidget(label1)
    layout.addWidget(self.tableWidget)

    self.low2.setLayout(layout)