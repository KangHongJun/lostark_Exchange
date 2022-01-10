from PyQt5.QtWidgets import *
from DB import GetData

Reforging = GetData.Reforging_Data()
Reforging_Add = GetData.Reforging_Add_Data()
Potion = GetData.Potion_Data()
Buff = GetData.Buff_Data()
Attack = GetData.Attack_Data()
Assistance = GetData.Assistance_Data()

Plant = GetData.Plant_Data()
Logging = GetData.Logging_Data()
Mining = GetData.Mining_Data()
Hunting = GetData.Hunting_Data()
Fishing = GetData.Fishing_Data()
Archaeology = GetData.Archaeology_Data()

def SetTableValue_Ex(self,list,row,col):
    self.tableWidget = QTableWidget(self)
    self.tableWidget.setRowCount(row)
    self.tableWidget.setColumnCount(col)
    column_headers = ['아이템명', '가격']
    self.tableWidget.setHorizontalHeaderLabels(column_headers)
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
        SetTableValue_Ex(self,Reforging + Reforging_Add,53,2)
        layout = QFormLayout()
        layout.addWidget(self.tableWidget)

        self.ui_ref_all.setLayout(layout)

    def UI_Reforging(self):
        SetTableValue_Ex(self,Reforging,21,2)
        layout = QFormLayout()
        layout.addWidget(self.tableWidget)

        self.ui_ref.setLayout(layout)

    def UI_Reforging_Add(self):
        SetTableValue_Ex(self,Reforging_Add,32,2)
        layout = QFormLayout()
        layout.addWidget(self.tableWidget)

        self.ui_ref_add.setLayout(layout)

class Item_Battle:
    def UI_Battle_Item_ALL(self):
        SetTableValue_Ex(self,Potion+Attack+Assistance+Buff,52,2)
        layout = QFormLayout()
        layout.addWidget(self.tableWidget)

        self.ui_battle_all.setLayout(layout)

    def UI_Potion(self):
        SetTableValue_Ex(self,Potion,4,2)
        layout = QFormLayout()
        layout.addWidget(self.tableWidget)

        self.ui_potion.setLayout(layout)

    def UI_Attack(self):
        SetTableValue_Ex(self,Attack,23,2)
        layout = QFormLayout()
        layout.addWidget(self.tableWidget)

        self.ui_attack.setLayout(layout)

    def UI_Assistance(self):
        SetTableValue_Ex(self,Assistance,18,2)
        layout = QFormLayout()
        layout.addWidget(self.tableWidget)

        self.ui_assistance.setLayout(layout)

    def UI_Buff(self):
        SetTableValue_Ex(self,Buff,7,2)
        layout = QFormLayout()
        layout.addWidget(self.tableWidget)

        self.ui_buff.setLayout(layout)

class Item_Life:
    def UI_Life_ALL(self):
        SetTableValue_Ex(self,Plant+Logging+Mining+Hunting+Fishing+Archaeology,35,2)
        layout = QFormLayout()
        layout.addWidget(self.tableWidget)

        self.ui_life_all.setLayout(layout)

    def UI_Plant(self):
        SetTableValue_Ex(self,Plant,6,2)
        layout = QFormLayout()
        layout.addWidget(self.tableWidget)

        self.ui_plant.setLayout(layout)

    def UI_Logging(self):
        SetTableValue_Ex(self,Logging,3,2)
        layout = QFormLayout()
        layout.addWidget(self.tableWidget)

        self.ui_logging.setLayout(layout)

    def UI_Mining(self):
        SetTableValue_Ex(self,Mining,3,2)
        layout = QFormLayout()
        layout.addWidget(self.tableWidget)

        self.ui_mining.setLayout(layout)

    def UI_Hunting(self):
        SetTableValue_Ex(self,Hunting,5,2)
        layout = QFormLayout()
        layout.addWidget(self.tableWidget)

        self.ui_hunting.setLayout(layout)

    def UI_Fishing(self):
        SetTableValue_Ex(self,Fishing,5,2)
        layout = QFormLayout()
        layout.addWidget(self.tableWidget)

        self.ui_fishing.setLayout(layout)

    def UI_Archaeology(self):
        SetTableValue_Ex(self,Archaeology,4,2)
        layout = QFormLayout()
        layout.addWidget(self.tableWidget)

        self.ui_archaeology.setLayout(layout)




