from PyQt5.QtWidgets import *
from DB import GetData
from PyQt5.QtCore import Qt
import re
import Function

#데이터 가져오기
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

Reinforce = Reforging + Reforging_Add
Life = Plant + Logging + Mining + Hunting + Fishing + Archaeology
Battle_Item = Potion + Buff + Attack + Assistance

ALL_ITEM = Reinforce + Life + Battle_Item

#거래소
def SetTableValue_Ex(self,list,row,col):
    #테이블 생성
    self.tableWidget = QTableWidget(self)
    self.tableWidget.setRowCount(row)
    self.tableWidget.setColumnCount(col)
    column_headers = ['아이템명', '가격']
    self.tableWidget.setHorizontalHeaderLabels(column_headers)
    #QTableWidgetItem에 아이템정보 삽입
    i = 0
    for col, row in list:
        name = QTableWidgetItem(col)
        price = QTableWidgetItem()
        price.setData(Qt.DisplayRole,row)
        self.tableWidget.setItem(i, 0, name)
        self.tableWidget.setItem(i, 1, price)
        i = i + 1

#제작정보
def SetProduct(self,Item_name,Item_resipe):
    #조합법의 이름 및 숫자 구분하여 저장
    name = re.findall(r'\D+', Item_resipe)
    number = re.findall(r'\d+', Item_resipe)
    product = str(Product_cost(self, name, number))
    cost = str(Item_cost(self,Item_name))
    fee = Function.Fee(int(cost))

    self.label = QTextBrowser(self)
    i = 0
    self.label.append(Item_name + "개 조합법\n")
    for i in range(len(name)):
        self.label.append(name[i]+" "+number[i])

    self.label.append("\n판매가격 : " + cost)
    self.label.append("제작비용 : "+ product)

    benefit = round((float(cost)-float(product)-float(fee)),2)
    self.label.append("\n이득액 :" +str(benefit))

#return 제작품 가격
def Item_cost(self,Item_name):
    name = re.findall(r'\D+', Item_name)
    number = re.findall(r'\d+', Item_name)

    for i in range(len(ALL_ITEM)):
        if ALL_ITEM[i][0] == name[0]:
            price = ALL_ITEM[i][1] * int(number[0])
            return(price)

#return 조합비용
def Product_cost(self,Item_name, Item_number):
    Len = int(len(Item_name))

    #전체 배열에서 해당하는 위치 가져오기
    num = []
    for j in range(Len):
        for i in range(len(ALL_ITEM)):
            if ALL_ITEM[i][0] == Item_name[j]:
                num.append(i)

    price = 0
    for q in range(Len-1):
        price += ALL_ITEM[num[q]][1] * int(Item_number[q])
    price = round(price+int(Item_number[Len-1]), 2)

    return (price)


#강화재료 table
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

#배틀 아이템 table
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

#생활 재료 table
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


#제작 UI
class Product:
    #Potion
    def Healing(self):
        Item_name = "회복약3"
        resipe = "수줍은 들꽃5들꽃10조합비0"
        SetProduct(self, Item_name, resipe)
        layout = QFormLayout()
        layout.addWidget(self.label)

        self.healing.setLayout(layout)

    def Rare_Healing(self):
        Item_name = "고급 회복약3"
        resipe = "수줍은 들꽃9들꽃18조합비15"
        SetProduct(self, Item_name, resipe)
        layout = QFormLayout()
        layout.addWidget(self.label)

        self.rare_healing.setLayout(layout)

    def Spirit_Healing(self):
        Item_name = "정령의 회복약3"
        resipe = "화사한 들꽃6수줍은 들꽃24들꽃48조합비30"
        SetProduct(self, Item_name, resipe)
        layout = QFormLayout()
        layout.addWidget(self.label)

        self.spirit_healing.setLayout(layout)

    def SSpirit_Healing(self):
        Item_name = "빛나는 정령의 회복약2"
        resipe = "정령의 회복약3화사한 들꽃8조합비30"
        SetProduct(self, Item_name, resipe)
        layout = QFormLayout()
        layout.addWidget(self.label)

        self.sspirit_healing.setLayout(layout)



    def Flash(self):
        Item_name = "섬광 수류탄3"
        resipe = "화려한 버섯3싱싱한 버섯12투박한 버섯24조합비10"
        SetProduct(self,Item_name,resipe)
        layout = QFormLayout()
        layout.addWidget(self.label)

        self.flash.setLayout(layout)

    def Flash2(self):
        Item_name = "섬광 수류탄3"
        resipe = "화려한 버섯5싱싱한 버섯12투박한 버섯24조합비10"
        SetProduct(self, Item_name, resipe)

        layout = QFormLayout()
        layout.addWidget(self.label)

        self.flash2.setLayout(layout)

    def Flash3(self):
        Item_name = "섬광 수류탄3"
        resipe = "화려한 버섯3싱싱한 버섯12투박한 버섯24조합비10"
        SetProduct(self, Item_name, resipe)
        layout = QFormLayout()
        layout.addWidget(self.label)

        self.flash3.setLayout(layout)







