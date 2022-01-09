from PyQt5.QtWidgets import *
from DB import GetData

Reforging = GetData.Reforging_Data()
Reforging_Add = GetData.Reforging_Add_Data()

def SetTableValue(self,list):
    i = 0
    for col, row in list:
        row = str(row)
        name = QTableWidgetItem(col)
        price = QTableWidgetItem(row)
        self.tableWidget.setItem(i, 0, name)
        self.tableWidget.setItem(i, 1, price)
        i = i + 1

class Item_Reinfoece:
    def UI_Reforging_ALL(self):
        self.tableWidget = QTableWidget(self)
        self.tableWidget.setRowCount(53)
        self.tableWidget.setColumnCount(2)
        column_headers = ['아이템명', '가격']
        self.tableWidget.setHorizontalHeaderLabels(column_headers)

        SetTableValue(self,Reforging + Reforging_Add)

        layout = QFormLayout()
        label1 = QLabel()
        layout.addWidget(label1)
        layout.addWidget(self.tableWidget)

        self.ui_ref_all.setLayout(layout)

    def UI_Reforging(self):
        self.tableWidget = QTableWidget(self)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(21)
        column_headers = ['아이템명','가격']
        self.tableWidget.setHorizontalHeaderLabels(column_headers)

        SetTableValue(self,Reforging)

        layout = QFormLayout()
        label1 = QLabel()
        layout.addWidget(label1)
        layout.addWidget(self.tableWidget)

        self.ui_ref.setLayout(layout)

    def UI_Reforging_Add(self):
        self.tableWidget = QTableWidget(self)
        self.tableWidget.setRowCount(32)
        self.tableWidget.setColumnCount(2)
        column_headers = ['아이템명', '가격']
        self.tableWidget.setHorizontalHeaderLabels(column_headers)

        SetTableValue(self,Reforging_Add)

        layout = QFormLayout()
        label1 = QLabel()
        layout.addWidget(label1)
        layout.addWidget(self.tableWidget)

        self.ui_ref_add.setLayout(layout)


class Item_Battle_Item:
    def UI_Battle_Item_ALL(self):
        self.tableWidget = QTableWidget(self)
        self.tableWidget.setRowCount(53)
        self.tableWidget.setColumnCount(2)
        column_headers = ['아이템명', '가격']
        self.tableWidget.setHorizontalHeaderLabels(column_headers)

        SetTableValue(self,Reforging + Reforging_Add)

        layout = QFormLayout()
        label1 = QLabel()
        layout.addWidget(label1)
        layout.addWidget(self.tableWidget)

        self.ui_battle_all.setLayout(layout)

    def UI_Potion(self):
        self.tableWidget = QTableWidget(self)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(21)
        column_headers = ['아이템명','가격']
        self.tableWidget.setHorizontalHeaderLabels(column_headers)

        SetTableValue(self,Reforging)

        layout = QFormLayout()
        label1 = QLabel()
        layout.addWidget(label1)
        layout.addWidget(self.tableWidget)

        self.ui_potion.setLayout(layout)

    def UI_Buff(self):
        self.tableWidget = QTableWidget(self)
        self.tableWidget.setRowCount(32)
        self.tableWidget.setColumnCount(2)
        column_headers = ['아이템명', '가격']
        self.tableWidget.setHorizontalHeaderLabels(column_headers)

        SetTableValue(self,Reforging_Add)

        layout = QFormLayout()
        label1 = QLabel()
        layout.addWidget(label1)
        layout.addWidget(self.tableWidget)

        self.ui_buff.setLayout(layout)


