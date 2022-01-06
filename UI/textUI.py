from PyQt5.QtWidgets import *
import main

def low0(self):
    self.tableWidget = QTableWidget()
    self.tableWidget.setRowCount(20)
    self.tableWidget.setColumnCount(4)

    layout = QFormLayout()
    label1 = QLabel()
    label1.setText("low0")
    layout.addWidget(label1)
    layout.addWidget(self.tableWidget)

    self.low0.setLayout(layout)




def low1(self):
    layout = QFormLayout()
    label1 = QLabel()
    label1.setText("low1")
    layout.addWidget(label1)

    self.low1.setLayout(layout)



def low2(self):
    layout = QFormLayout()

    label1 = QLabel()
    label1.setText("low2")

    layout.addWidget(label1)

    self.low2.setLayout(layout)