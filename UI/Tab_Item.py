from PyQt5.QtWidgets import *
from DB import GetData
from PyQt5.QtCore import Qt
import re
import Function

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

    cost = str(Item_cost(self,Item_name))
    product = str(Product_cost(self, name, number))

    self.label = QTextBrowser(self)
    i = 0
    self.label.append(Item_name + "개 조합법\n")
    for i in range(len(name)):
        self.label.append(name[i]+" "+number[i])

    self.label.append("\n판매가격 : " + cost)
    self.label.append("제작비용 : "+ product)

    benefit = round((float(cost)-float(product)),2)
    self.label.append("\n이득액 :" +str(benefit))

#return 제작품 가격
def Item_cost(self,Item_name):
    ALL_ITEM = GetData.All_Item_Data()
    name = re.findall(r'\D+', Item_name)
    number = re.findall(r'\d+', Item_name)

    for i in range(len(ALL_ITEM)):
        if ALL_ITEM[i][0] == name[0]:
            price = ALL_ITEM[i][1] - Function.Fee(ALL_ITEM[i][1])
            price = round(price * int(number[0]),2)
            return price

#return 조합비용 - 아이템 이름, 아이템 개수 list
def Product_cost(self,Item_name, Item_number):
    ALL_ITEM = GetData.All_Item_Data()
    Len = int(len(Item_name))

    #전체 배열에서 해당하는 위치 가져오기
    num = []
    for j in range(Len-1):
        for i in range(len(ALL_ITEM)):
            if ALL_ITEM[i][0] == Item_name[j]:
                num.append(i)

    price = 0
    for q in range(Len-1):
        price += ALL_ITEM[num[q]][1] * int(Item_number[q])
    price = round(price+int(Item_number[Len-1]), 2)

    return price


#강화재료 table
class Item_Reinforce:
    Reforging = GetData.Reforging_Data()
    Reforging_Add = GetData.Reforging_Add_Data()


    def UI_Reforging_ALL(self):
        SetTableValue_Ex(self,Item_Reinforce.Reforging + Item_Reinforce.Reforging_Add,53,2)
        layout = QFormLayout()
        layout.addWidget(self.tableWidget)

        self.ui_ref_all.setLayout(layout)

    def UI_Reforging(self):
        SetTableValue_Ex(self,Item_Reinforce.Reforging,21,2)
        layout = QFormLayout()
        layout.addWidget(self.tableWidget)

        self.ui_ref.setLayout(layout)

    def UI_Reforging_Add(self):
        SetTableValue_Ex(self,Item_Reinforce.Reforging_Add,32,2)
        layout = QFormLayout()
        layout.addWidget(self.tableWidget)

        self.ui_ref_add.setLayout(layout)


#배틀 아이템 table
class Item_Battle:
    Potion = GetData.Potion_Data()
    Attack = GetData.Attack_Data()
    Assistance = GetData.Assistance_Data()
    Buff = GetData.Buff_Data()
    def UI_Battle_Item_ALL(self):
        SetTableValue_Ex(self,Item_Battle.Potion+Item_Battle.Attack+Item_Battle.Assistance+Item_Battle.Buff,52,2)
        layout = QFormLayout()
        layout.addWidget(self.tableWidget)

        self.ui_battle_all.setLayout(layout)

    def UI_Potion(self):
        SetTableValue_Ex(self,Item_Battle.Potion,4,2)
        layout = QFormLayout()
        layout.addWidget(self.tableWidget)

        self.ui_potion.setLayout(layout)

    def UI_Attack(self):
        SetTableValue_Ex(self,Item_Battle.Attack,23,2)
        layout = QFormLayout()
        layout.addWidget(self.tableWidget)

        self.ui_attack.setLayout(layout)

    def UI_Assistance(self):
        SetTableValue_Ex(self,Item_Battle.Assistance,18,2)
        layout = QFormLayout()
        layout.addWidget(self.tableWidget)

        self.ui_assistance.setLayout(layout)

    def UI_Buff(self):
        SetTableValue_Ex(self,Item_Battle.Buff,7,2)
        layout = QFormLayout()
        layout.addWidget(self.tableWidget)

        self.ui_buff.setLayout(layout)

#생활 재료 table
class Item_Life:
    Plant = GetData.Plant_Data()
    Logging = GetData.Logging_Data()
    Mining = GetData.Mining_Data()
    Hunting = GetData.Hunting_Data()
    Fishing = GetData.Fishing_Data()
    Archaeology = GetData.Archaeology_Data()

    def UI_Life_ALL(self):
        SetTableValue_Ex(self,Item_Life.Plant+Item_Life.Logging+Item_Life.Mining+Item_Life.Hunting+Item_Life.Fishing+Item_Life.Archaeology,35,2)
        layout = QFormLayout()
        layout.addWidget(self.tableWidget)

        self.ui_life_all.setLayout(layout)

    def UI_Plant(self):
        SetTableValue_Ex(self,Item_Life.Plant,6,2)
        layout = QFormLayout()
        layout.addWidget(self.tableWidget)

        self.ui_plant.setLayout(layout)

    def UI_Logging(self):
        SetTableValue_Ex(self,Item_Life.Logging,3,2)
        layout = QFormLayout()
        layout.addWidget(self.tableWidget)

        self.ui_logging.setLayout(layout)

    def UI_Mining(self):
        SetTableValue_Ex(self,Item_Life.Mining,3,2)
        layout = QFormLayout()
        layout.addWidget(self.tableWidget)

        self.ui_mining.setLayout(layout)

    def UI_Hunting(self):
        SetTableValue_Ex(self,Item_Life.Hunting,5,2)
        layout = QFormLayout()
        layout.addWidget(self.tableWidget)

        self.ui_hunting.setLayout(layout)

    def UI_Fishing(self):
        SetTableValue_Ex(self,Item_Life.Fishing,5,2)
        layout = QFormLayout()
        layout.addWidget(self.tableWidget)

        self.ui_fishing.setLayout(layout)

    def UI_Archaeology(self):
        SetTableValue_Ex(self,Item_Life.Archaeology,4,2)
        layout = QFormLayout()
        layout.addWidget(self.tableWidget)

        self.ui_archaeology.setLayout(layout)


#제작 UI
class Product_Potion:
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


class Product_Attack:
    def Flash(self):
        Item_name = "섬광 수류탄3"
        resipe = "화려한 버섯3싱싱한 버섯12투박한 버섯24철광석5조합비15"
        SetProduct(self, Item_name, resipe)
        layout = QFormLayout()
        layout.addWidget(self.label)

        self.flash.setLayout(layout)

    def Flame(self):
        Item_name = "화염 수류탄3"
        resipe = "화려한 버섯3싱싱한 버섯12부드러운 목재3투박한 버섯24조합비15"
        SetProduct(self, Item_name, resipe)

        layout = QFormLayout()
        layout.addWidget(self.label)

        self.flame.setLayout(layout)

    def Cold_Air(self):
        Item_name = "냉기 수류탄3"
        resipe = "화려한 버섯3싱싱한 버섯12투박한 버섯24철광석5조합비15"
        SetProduct(self, Item_name, resipe)
        layout = QFormLayout()
        layout.addWidget(self.label)

        self.cold_air.setLayout(layout)

    def Electric(self):
        Item_name = "전기 수류탄3"
        resipe = "화려한 버섯3싱싱한 버섯12투박한 버섯24철광석5조합비15"
        SetProduct(self, Item_name, resipe)
        layout = QFormLayout()
        layout.addWidget(self.label)

        self.electric.setLayout(layout)

    def Dark(self):
        Item_name = "암흑 수류탄3"
        resipe = "화려한 버섯3싱싱한 버섯12부드러운 목재3투박한 버섯24조합비15"
        SetProduct(self, Item_name, resipe)
        layout = QFormLayout()
        layout.addWidget(self.label)

        self.dark.setLayout(layout)

    def Corrosion(self):
        Item_name = "부식 폭탄3"
        resipe = "화려한 버섯4싱싱한 버섯12묵직한 철광석6투박한 버섯32조합비15"
        SetProduct(self, Item_name, resipe)
        layout = QFormLayout()
        layout.addWidget(self.label)

        self.corrosion.setLayout(layout)

    def Thunder(self):
        Item_name = "천둥 물약3"
        resipe = "화사한 들꽃4수줍은 들꽃16희귀한 유물5들꽃32조합비15"
        SetProduct(self, Item_name, resipe)
        layout = QFormLayout()
        layout.addWidget(self.label)

        self.thunder.setLayout(layout)

    def Tornado(self):
        Item_name = "회오리 수류탄3"
        resipe = "화려한 버섯3싱싱한 버섯12부드러운 목재3투박한 버섯24조합비15"
        SetProduct(self, Item_name, resipe)
        layout = QFormLayout()
        layout.addWidget(self.label)

        self.tornado.setLayout(layout)

    def Clay(self):
        Item_name = "점토 수류탄3"
        resipe = "화려한 버섯3싱싱한 버섯12투박한 버섯24철광석5조합비15"
        SetProduct(self, Item_name, resipe)
        layout = QFormLayout()
        layout.addWidget(self.label)

        self.clay.setLayout(layout)

    def Sleeping(self):
        Item_name = "수면 폭탄3"
        resipe = "화려한 버섯3싱싱한 버섯12투박한 버섯32철광석10조합비15"
        SetProduct(self, Item_name, resipe)
        layout = QFormLayout()
        layout.addWidget(self.label)

        self.sleeping.setLayout(layout)

    def Holy(self):
        Item_name = "성스러운 폭탄3"
        resipe = "화려한 버섯3싱싱한 버섯12투박한 버섯24철광석3조합비15"
        SetProduct(self, Item_name, resipe)
        layout = QFormLayout()
        layout.addWidget(self.label)

        self.holy.setLayout(layout)

    def Destruction(self):
        Item_name = "파괴 폭탄3"
        resipe = "화려한 버섯4싱싱한 버섯12투박한 버섯32묵직한 철광석6조합비15"
        SetProduct(self, Item_name, resipe)
        layout = QFormLayout()
        layout.addWidget(self.label)

        self.destruction.setLayout(layout)

    def SFlash(self):
        Item_name = "빛나는 섬광 수류탄2"
        resipe = "섬광 수류탄3화려한 버섯4조합비15"
        SetProduct(self, Item_name, resipe)
        layout = QFormLayout()
        layout.addWidget(self.label)

        self.sflash.setLayout(layout)

    def SFlame(self):
        Item_name = "빛나는 화염 수류탄2"
        resipe = "화염 수류탄3화려한 버섯4조합비15"
        SetProduct(self, Item_name, resipe)
        layout = QFormLayout()
        layout.addWidget(self.label)

        self.sflame.setLayout(layout)

    def SCold_Air(self):
        Item_name = "빛나는 냉기 수류탄2"
        resipe = "냉기 수류탄3화려한 버섯4조합비15"
        SetProduct(self, Item_name, resipe)
        layout = QFormLayout()
        layout.addWidget(self.label)

        self.scold_air.setLayout(layout)

    def SElectric(self):
        Item_name = "빛나는 전기 수류탄2"
        resipe = "전기 수류탄3화려한 버섯4조합비15"
        SetProduct(self, Item_name, resipe)
        layout = QFormLayout()
        layout.addWidget(self.label)

        self.selectric.setLayout(layout)

    def SClay(self):
        Item_name = "빛나는 점토 수류탄2"
        resipe = "점토 수류탄3화려한 버섯4조합비15"
        SetProduct(self, Item_name, resipe)
        layout = QFormLayout()
        layout.addWidget(self.label)

        self.sclay.setLayout(layout)

    def STornado(self):
        Item_name = "빛나는 회오리 수류탄2"
        resipe = "회오리 수류탄3화려한 버섯4조합비15"
        SetProduct(self, Item_name, resipe)
        layout = QFormLayout()
        layout.addWidget(self.label)

        self.stornado.setLayout(layout)

    def SDark(self):
        Item_name = "빛나는 암흑 수류탄2"
        resipe = "암흑 수류탄3화려한 버섯4조합비15"
        SetProduct(self, Item_name, resipe)
        layout = QFormLayout()
        layout.addWidget(self.label)

        self.sdark.setLayout(layout)

    def SSleeping(self):
        Item_name = "빛나는 수면 폭탄2"
        resipe = "수면 폭탄3화려한 버섯2조합비15"
        SetProduct(self, Item_name, resipe)
        layout = QFormLayout()
        layout.addWidget(self.label)

        self.ssleeping.setLayout(layout)

    def SDestruction(self):
        Item_name = "빛나는 파괴 폭탄2"
        resipe = "파괴 폭탄3화려한 버섯2조합비15"
        SetProduct(self, Item_name, resipe)
        layout = QFormLayout()
        layout.addWidget(self.label)

        self.sdestruction.setLayout(layout)

    def SCorrosion(self):
        Item_name = "빛나는 부식 폭탄2"
        resipe = "부식 폭탄3화려한 버섯2조합비15"
        SetProduct(self, Item_name, resipe)
        layout = QFormLayout()
        layout.addWidget(self.label)

        self.scorrosion.setLayout(layout)

    def SHoly(self):
        Item_name = "빛나는 성스러운 폭탄2"
        resipe = "성스러운 폭탄3화려한 버섯2조합비15"
        SetProduct(self, Item_name, resipe)
        layout = QFormLayout()
        layout.addWidget(self.label)

        self.sholy.setLayout(layout)

class Product_Assist:
    def Signal_Gun(self):
        Item_name = "신호탄3"
        resipe = "자연산 진주20들꽃35조합비0"
        SetProduct(self, Item_name, resipe)
        layout = QFormLayout()
        layout.addWidget(self.label)

        self.signal_gun.setLayout(layout)

    def SSignal_Gun(self):
        Item_name = "빛나는 신호탄2"
        resipe = "신호탄3수줍은 들꽃20조합비5"
        SetProduct(self, Item_name, resipe)
        layout = QFormLayout()
        layout.addWidget(self.label)

        self.ssignal_gun.setLayout(layout)

    def All_purpose(self):
        Item_name = "만능 물약3"
        resipe = "화려한 버섯4싱싱한 버섯16투박한 버섯32희귀한 유물5조합비15"
        SetProduct(self, Item_name, resipe)
        layout = QFormLayout()
        layout.addWidget(self.label)

        self.all_purpose.setLayout(layout)

    def Scarecrow(self):
        Item_name = "도발 허수아비3"
        resipe = "화려한 버섯3싱싱한 버섯15목재13조합비15"
        SetProduct(self, Item_name, resipe)
        layout = QFormLayout()
        layout.addWidget(self.label)

        self.scarecrow.setLayout(layout)

    def Bonfire(self):
        Item_name = "모닥불3"
        resipe = "화려한 버섯3싱싱한 버섯15목재12조합비15"
        SetProduct(self, Item_name, resipe)
        layout = QFormLayout()
        layout.addWidget(self.label)

        self.bonfire.setLayout(layout)

    def Camouflage(self):
        Item_name = "위장 로브3"
        resipe = "질긴가죽22싱싱한 버섯22투박한 버섯35조합비15"
        SetProduct(self, Item_name, resipe)
        layout = QFormLayout()
        layout.addWidget(self.label)

        self.camouflage.setLayout(layout)

    def Amulet(self):
        Item_name = "성스러운 부적3"
        resipe = "화려한 버섯3싱싱한 버섯18투박한 버섯30조합비15"
        SetProduct(self, Item_name, resipe)
        layout = QFormLayout()
        layout.addWidget(self.label)

        self.amulet.setLayout(layout)

    def Spell(self):
        Item_name = "정비소 이동 포탈 주문서3"
        resipe = "화려한 버섯4싱싱한 버섯12투박한 버섯32묵직한 철광석6조합비15"
        SetProduct(self, Item_name, resipe)
        layout = QFormLayout()
        layout.addWidget(self.label)

        self.spell.setLayout(layout)

    def Pheromones(self):
        Item_name = "페로몬 폭탄3"
        resipe = "화려한 버섯4싱싱한 버섯12투박한 버섯32묵직한 철광석6조합비15"
        SetProduct(self, Item_name, resipe)
        layout = QFormLayout()
        layout.addWidget(self.label)

        self.pheromones.setLayout(layout)

    def SAll_purpose(self):
        Item_name = "빛나는 만능 물약2"
        resipe = "만능 물약3화려한 버섯10조합비15"
        SetProduct(self, Item_name, resipe)
        layout = QFormLayout()
        layout.addWidget(self.label)

        self.sall_purpose.setLayout(layout)

    def SCamouflage(self):
        Item_name = "빛나는 위장 로브2"
        resipe = "위장 로브3화려한 버섯9조합비15"
        SetProduct(self, Item_name, resipe)
        layout = QFormLayout()
        layout.addWidget(self.label)

        self.scamouflage.setLayout(layout)

    def SBonfire(self):
        Item_name = "빛나는 모닥불2"
        resipe = "모닥불3화려한 버섯6조합비15"
        SetProduct(self, Item_name, resipe)
        layout = QFormLayout()
        layout.addWidget(self.label)

        self.sbonfire.setLayout(layout)

    def SScarecrow(self):
        Item_name = "빛나는 도발 허수아비2"
        resipe = "도발 허수아비3화려한 버섯7조합비15"
        SetProduct(self, Item_name, resipe)
        layout = QFormLayout()
        layout.addWidget(self.label)

        self.sscarecrow.setLayout(layout)

    def SAmulet(self):
        Item_name = "빛나는 성스러운 부적2"
        resipe = "성스러운 부적3화려한 버섯3조합비15"
        SetProduct(self, Item_name, resipe)
        layout = QFormLayout()
        layout.addWidget(self.label)

        self.samulet.setLayout(layout)

    def Hiding(self):
        Item_name = "은신 로브3"
        resipe = "화려한 버섯5싱싱한 버섯15투박한 버섯35단단한 철광석2질긴가죽2조합비30"
        SetProduct(self, Item_name, resipe)
        layout = QFormLayout()
        layout.addWidget(self.label)

        self.hiding.setLayout(layout)

    def Trumpet(self):
        Item_name = "루테란의 나팔3"
        resipe = "화사한 들꽃4수줍은 들꽃20들꽃40단단한 철광석2철광석2조합비30"
        SetProduct(self, Item_name, resipe)
        layout = QFormLayout()
        layout.addWidget(self.label)

        self.trumpet.setLayout(layout)

    def Static_time(self):
        Item_name = "시간 정지 물약3"
        resipe = "화사한 들꽃5수줍은 들꽃20들꽃40튼튼한 목재2희귀한 유물2조합비30"
        SetProduct(self, Item_name, resipe)
        layout = QFormLayout()
        layout.addWidget(self.label)

        self.static_time.setLayout(layout)

    def SHiding(self):
        Item_name = "빛나는 은신 로브2"
        resipe = "은신 로브3화려한 버섯9조합비15"
        SetProduct(self, Item_name, resipe)
        layout = QFormLayout()
        layout.addWidget(self.label)

        self.shiding.setLayout(layout)


class Product_Buff:
    def Flag(self):
        Item_name = "진군의 깃발3"
        resipe = "화려한 버섯4자연산 진주8투박한 버섯38조합비15"
        SetProduct(self, Item_name, resipe)
        layout = QFormLayout()
        layout.addWidget(self.label)

        self.flag.setLayout(layout)

    def Protection(self):
        Item_name = "보호 물약3"
        resipe = "화려한 버섯4싱싱한 버섯16투박한 버섯32희귀한 유물5조합비15"
        SetProduct(self, Item_name, resipe)
        layout = QFormLayout()
        layout.addWidget(self.label)

        self.protection.setLayout(layout)

    def Quick(self):
        Item_name = "신속 로브3"
        resipe = "질긴가죽17수줍은 들꽃17들꽃27조합비15"
        SetProduct(self, Item_name, resipe)
        layout = QFormLayout()
        layout.addWidget(self.label)

        self.quick.setLayout(layout)

    def SProtection(self):
        Item_name = "빛나는 보호 물약2"
        resipe = "보호 물약3화려한 버섯10조합비15"
        SetProduct(self, Item_name, resipe)
        layout = QFormLayout()
        layout.addWidget(self.label)

        self.sprotection.setLayout(layout)

    def SQuick(self):
        Item_name = "빛나는 신속 로브2"
        resipe = "신속 로브3화려한 버섯3조합비15"
        SetProduct(self, Item_name, resipe)
        layout = QFormLayout()
        layout.addWidget(self.label)

        self.squick.setLayout(layout)

    def Arousal(self):
        Item_name = "각성 물약3"
        resipe = "화려한 버섯5싱싱한 버섯20투박한 버섯40튼튼한 목재2희귀한 유물4조합비30"
        SetProduct(self, Item_name, resipe)
        layout = QFormLayout()
        layout.addWidget(self.label)

        self.arousal.setLayout(layout)

    def Atropine(self):
        Item_name = "아드로핀 물약3"
        resipe = "화사한 들꽃6수줍은 들꽃24들꽃48단단한 철광석2희귀한 유물2조합비30"
        SetProduct(self, Item_name, resipe)
        layout = QFormLayout()
        layout.addWidget(self.label)

        self.atropine.setLayout(layout)


class Product_Special:
    #수렵
    def Low_Ounion_H(self):
        Item_name = "하급 오레하 융화 재료30"
        resipe = "오레하 생고기9질긴가죽36두툼한 생고기72조합비203"
        SetProduct(self, Item_name, resipe)
        layout = QFormLayout()
        layout.addWidget(self.label)

        self.low_ounion_h.setLayout(layout)

    def Mid_Ounion_H(self):
        Item_name = "중급 오레하 융화 재료30"
        resipe = "오레하 생고기10질긴가죽40두툼한 생고기80조합비205"
        SetProduct(self, Item_name, resipe)
        layout = QFormLayout()
        layout.addWidget(self.label)

        self.mid_ounion_h.setLayout(layout)

    def High_Ounion_H(self):
        Item_name = "상급 오레하 융화 재료20"
        resipe = "오레하 생고기16질긴가죽64두툼한 생고기128조합비250"
        SetProduct(self, Item_name, resipe)
        layout = QFormLayout()
        layout.addWidget(self.label)

        self.high_ounion_h.setLayout(layout)
    # 낚시
    def Low_Ounion_F(self):
        Item_name = "하급 오레하 융화 재료30"
        resipe = "오레하 태양잉어9자연산 진주36생선72조합비203"
        SetProduct(self, Item_name, resipe)
        layout = QFormLayout()
        layout.addWidget(self.label)

        self.low_ounion_f.setLayout(layout)

    def Mid_Ounion_F(self):
        Item_name = "중급 오레하 융화 재료30"
        resipe = "오레하 태양잉어10자연산 진주40생선80조합비205"
        SetProduct(self, Item_name, resipe)
        layout = QFormLayout()
        layout.addWidget(self.label)

        self.mid_ounion_f.setLayout(layout)

    def High_Ounion_F(self):
        Item_name = "상급 오레하 융화 재료20"
        resipe = "오레하 태양잉어16자연산 진주64생선128조합비250"
        SetProduct(self, Item_name, resipe)
        layout = QFormLayout()
        layout.addWidget(self.label)

        self.high_ounion_f.setLayout(layout)
    #고고학
    def Low_Ounion_A(self):
        Item_name = "하급 오레하 융화 재료30"
        resipe = "오레하 유물7희귀한 유물28고대 유물56조합비203"
        SetProduct(self, Item_name, resipe)
        layout = QFormLayout()
        layout.addWidget(self.label)

        self.low_ounion_a.setLayout(layout)

    def Mid_Ounion_A(self):
        Item_name = "중급 오레하 융화 재료30"
        resipe = "오레하 유물8희귀한 유물26고대 유물64조합비205"
        SetProduct(self, Item_name, resipe)
        layout = QFormLayout()
        layout.addWidget(self.label)

        self.mid_ounion_a.setLayout(layout)

    def High_Ounion_A(self):
        Item_name = "상급 오레하 융화 재료20"
        resipe = "오레하 유물16희귀한 유물29고대 유물94조합비250"
        SetProduct(self, Item_name, resipe)
        layout = QFormLayout()
        layout.addWidget(self.label)

        self.high_ounion_a.setLayout(layout)






