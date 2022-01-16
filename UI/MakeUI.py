from PyQt5.QtWidgets import *
from UI import Tab_Item

def Make_Tab(self):
    #탭 생성 및 추가
    tabs = QTabWidget()
    tabs.addTab(self.Tab_Item(Tab_Reinforce()), '강화재료')
    tabs.addTab(self.Tab_Item(Tab_Battle_Item()), '전투용품')
    tabs.addTab(self.Tab_Item(Tab_Life()), '생활')
    tabs.addTab(self.Tab_Item(Tab_Product()), '제작정보')
    self.setCentralWidget(tabs)

class Tab_Reinforce(QWidget):
    #리스트 목록
    def __init__(self):
        super(Tab_Reinforce, self).__init__()
        self.Reinforce = QListWidget()
        self.Reinforce.insertItem(0, '전체')
        self.Reinforce.insertItem(1, '재련 재료')
        self.Reinforce.insertItem(2, '재련 추가 재료')

        self.Reinforce_widget()
        hbox = QHBoxLayout(self)
        hbox.addWidget(self.Reinforce)
        hbox.addWidget(self.Stack)

        self.setLayout(hbox)
        self.Reinforce.currentRowChanged.connect(self.display)
    # item 배치
    def Reinforce_widget(self):
        self.ui_ref_all = QWidget()
        self.ui_ref = QWidget()
        self.ui_ref_add = QWidget()

        UIitem = Tab_Item.Item_Reinforce
        UIitem.UI_Reforging_ALL(self)
        UIitem.UI_Reforging(self)
        UIitem.UI_Reforging_Add(self)

        self.Stack = QStackedWidget(self)
        self.Stack.addWidget(self.ui_ref_all)
        self.Stack.addWidget(self.ui_ref)
        self.Stack.addWidget(self.ui_ref_add)

        return self.Stack

    def display(self, i):
        self.Stack.setCurrentIndex(i)

class Tab_Battle_Item(QWidget):
    def __init__(self):
        super(Tab_Battle_Item, self).__init__()
        self.Battle_Item = QListWidget()
        self.Battle_Item.insertItem(0, '전체')
        self.Battle_Item.insertItem(1, '배틀아이템 - 회복형')
        self.Battle_Item.insertItem(2, '배틀아이템 - 공격형')
        self.Battle_Item.insertItem(3, '배틀아이템 - 기능성')
        self.Battle_Item.insertItem(4, '배틀아이템 - 버프형')

        self.Battle_Item_Widget()

        hbox = QHBoxLayout(self)
        hbox.addWidget(self.Battle_Item)
        hbox.addWidget(self.Stack)

        self.setLayout(hbox)
        self.Battle_Item.currentRowChanged.connect(self.display)

    def Battle_Item_Widget(self):
        self.ui_battle_all = QWidget()
        self.ui_potion = QWidget()
        self.ui_attack = QWidget()
        self.ui_assistance = QWidget()
        self.ui_buff = QWidget()

        UIitem = Tab_Item.Item_Battle
        UIitem.UI_Battle_Item_ALL(self)
        UIitem.UI_Potion(self)
        UIitem.UI_Attack(self)
        UIitem.UI_Assistance(self)
        UIitem.UI_Buff(self)

        self.Stack = QStackedWidget(self)
        self.Stack.addWidget(self.ui_battle_all)
        self.Stack.addWidget(self.ui_potion)
        self.Stack.addWidget(self.ui_attack)
        self.Stack.addWidget(self.ui_assistance)
        self.Stack.addWidget(self.ui_buff)

        return self.Stack

    def display(self, i):
        self.Stack.setCurrentIndex(i)

class Tab_Life(QWidget):
    def __init__(self):
        super(Tab_Life, self).__init__()
        self.Life = QListWidget()
        self.Life.insertItem(0, '전체')
        self.Life.insertItem(1, '식물채집')
        self.Life.insertItem(2, '벌목')
        self.Life.insertItem(3, '채광')
        self.Life.insertItem(4, '수렵')
        self.Life.insertItem(5, '낚시')
        self.Life.insertItem(6, '고고학')

        self.Life_Widget()

        hbox = QHBoxLayout(self)
        hbox.addWidget(self.Life)
        hbox.addWidget(self.Stack)

        self.setLayout(hbox)
        self.Life.currentRowChanged.connect(self.display)

    def Life_Widget(self):
        self.ui_life_all = QWidget()
        self.ui_plant = QWidget()
        self.ui_logging = QWidget()
        self.ui_mining = QWidget()
        self.ui_hunting = QWidget()
        self.ui_fishing = QWidget()
        self.ui_archaeology = QWidget()

        UIitem = Tab_Item.Item_Life
        UIitem.UI_Life_ALL(self)
        UIitem.UI_Plant(self)
        UIitem.UI_Logging(self)
        UIitem.UI_Mining(self)
        UIitem.UI_Hunting(self)
        UIitem.UI_Fishing(self)
        UIitem.UI_Archaeology(self)

        self.Stack = QStackedWidget(self)
        self.Stack.addWidget(self.ui_life_all)
        self.Stack.addWidget(self.ui_plant)
        self.Stack.addWidget(self.ui_logging)
        self.Stack.addWidget(self.ui_mining)
        self.Stack.addWidget(self.ui_hunting)
        self.Stack.addWidget(self.ui_fishing)
        self.Stack.addWidget(self.ui_archaeology)

        return self.Stack

    def display(self, i):
        self.Stack.setCurrentIndex(i)

class Tab_Product(QWidget):
    def __init__(self):
        super(Tab_Product, self).__init__()
        self.product = QListWidget()
        self.product.insertItem(0, '배틀 아이템 - 회복형')
        self.product.insertItem(1, '배틀 아이템 - 공격형')
        self.product.insertItem(2, '배틀 아이템 - 기능성')
        self.product.insertItem(3, '배틀 아이템 - 버프형')
        self.product.insertItem(4, '특수 아이템')
        self.product.itemClicked.connect(self.clicked)

        self.potion()
        self.attack()
        self.assist()
        self.buff()
        self.special()

        self.Stack_Product = QStackedWidget(self)

        hbox = QHBoxLayout(self)
        hbox.addWidget(self.product)
        hbox.addWidget(self.potion)
        hbox.addWidget(self.attack)
        hbox.addWidget(self.assist)
        hbox.addWidget(self.buff)
        hbox.addWidget(self.special)

        hbox.addWidget(self.Stack_Potion)
        hbox.addWidget(self.Stack_Attack)
        hbox.addWidget(self.Stack_Assist)
        hbox.addWidget(self.Stack_Buff)
        hbox.addWidget(self.Stack_Special)


        self.attack.setVisible(False)
        self.assist.setVisible(False)
        self.buff.setVisible(False)
        self.special.setVisible(False)

        self.Stack_Attack.setVisible(False)
        self.Stack_Assist.setVisible(False)
        self.Stack_Buff.setVisible(False)
        self.Stack_Special.setVisible(False)

        self.setLayout(hbox)
        self.product.currentRowChanged.connect(self.display)

    def potion(self):
        self.potion = QListWidget()
        self.potion.insertItem(0, '회복약')
        self.potion.insertItem(1, '고급 회복약')
        self.potion.insertItem(2, '정령의 회복약')
        self.potion.insertItem(3, '빛나는 정령의 회복약')

        self.potion_Widget()

        self.potion.currentRowChanged.connect(self.display_potion)

        return self.potion

    def attack(self):
        self.attack = QListWidget()
        self.attack.insertItem(0, '섬광 수류탄')
        self.attack.insertItem(1, '화염 수류탄')
        self.attack.insertItem(2, '냉기 수류탄')
        self.attack.insertItem(3, '전기 수류탄')
        self.attack.insertItem(4, '암흑 수류탄')
        self.attack.insertItem(5, '부식 수류탄')
        self.attack.insertItem(6, '천둥 물약')
        self.attack.insertItem(7, '회오리 수류탄')
        self.attack.insertItem(8, '점토 수류탄')
        self.attack.insertItem(9, '수면 수류탄')
        self.attack.insertItem(10, '성스러운 폭탄')
        self.attack.insertItem(11, '파괴 폭탄')
        self.attack.insertItem(12, '빛나는 섬광 수류탄')
        self.attack.insertItem(13, '빛나는 화염 수류탄')
        self.attack.insertItem(14, '빛나는 냉기 수류탄')
        self.attack.insertItem(15, '빛나는 전기 수류탄')
        self.attack.insertItem(16, '빛나는 점토 수류탄')
        self.attack.insertItem(17, '빛나는 회오리 수류탄')
        self.attack.insertItem(18, '빛나는 암흑 수류탄')
        self.attack.insertItem(19, '빛나는 수면 폭탄')
        self.attack.insertItem(20, '빛나는 파괴 폭탄')
        self.attack.insertItem(22, '빛나는 부식 폭탄')
        self.attack.insertItem(23, '빛나는 성스러운 폭탄')

        self.attack_Widget()
        self.attack.currentRowChanged.connect(self.display_attack)

        return self.attack

    def assist(self):
        self.assist = QListWidget()
        self.assist.insertItem(0, '신호탄')
        self.assist.insertItem(1, '빛나는 신호탄')
        self.assist.insertItem(2, '만능 물약')
        self.assist.insertItem(3, '도발 허수아비')
        self.assist.insertItem(4, '모닥불')
        self.assist.insertItem(5, '위장 로브')
        self.assist.insertItem(6, '성스러운 부적')
        self.assist.insertItem(7, '정비소 이동 포탈 주문서')
        self.assist.insertItem(8, '페로몬 폭탄')
        self.assist.insertItem(9, '빛나는 만능 물약')
        self.assist.insertItem(10, '빛나는 위장 로브')
        self.assist.insertItem(11, '빛나는 모닥불')
        self.assist.insertItem(12, '빛나는 도발 허수아비')
        self.assist.insertItem(13, '빛나는 성스러운 부적')
        self.assist.insertItem(14, '은신 로브')
        self.assist.insertItem(15, '루테란의 나팔')
        self.assist.insertItem(16, '시간 정지 물약')
        self.assist.insertItem(17, '빛나는 은신 로브')


        self.assist_Widget()
        self.assist.currentRowChanged.connect(self.display_assist)

        return self.assist

    def buff(self):
        self.buff = QListWidget()
        self.buff.insertItem(0, '진군의 깃발')
        self.buff.insertItem(1, '보호 물약')
        self.buff.insertItem(2, '신속 로브')
        self.buff.insertItem(3, '빛나는 보호 물약')
        self.buff.insertItem(4, '빛나는 신속 로브')
        self.buff.insertItem(5, '각성 물약')
        self.buff.insertItem(6, '아드로핀 물약')

        self.buff_Widget()
        self.buff.currentRowChanged.connect(self.display_buff)

        return self.buff

    def special(self):
        self.special = QListWidget()
        self.special.insertItem(0, '하급 오레하 융화 재료 - 수렵')
        self.special.insertItem(1, '중급 오레하 융화 재료 - 수렵')
        self.special.insertItem(2, '상급 오레하 융화 재료 - 수렵')
        self.special.insertItem(3, '하급 오레하 융화 재료 - 낚시')
        self.special.insertItem(4, '중급 오레하 융화 재료 - 낚시')
        self.special.insertItem(5, '상급 오레하 융화 재료 - 낚시')
        self.special.insertItem(6, '하급 오레하 융화 재료 - 고고학')
        self.special.insertItem(7, '중급 오레하 융화 재료 - 고고학')
        self.special.insertItem(8, '상급 오레하 융화 재료 - 고고학')

        self.special_Widget()
        self.special.currentRowChanged.connect(self.display_special)

        return self.special

    def clicked(self):
        cur = self.product.currentRow()
        self.potion.setVisible(False)
        self.attack.setVisible(False)
        self.assist.setVisible(False)
        self.buff.setVisible(False)
        self.special.setVisible(False)

        self.Stack_Potion.setVisible(False)
        self.Stack_Attack.setVisible(False)
        self.Stack_Assist.setVisible(False)
        self.Stack_Buff.setVisible(False)
        self.Stack_Special.setVisible(False)

        if cur == 0:
            self.potion.setVisible(True)
            self.Stack_Potion.setVisible(True)
        elif cur == 1:
            self.attack.setVisible(True)
            self.Stack_Attack.setVisible(True)
        elif cur == 2:
            self.assist.setVisible(True)
            self.Stack_Assist.setVisible(True)
        elif cur == 3:
            self.buff.setVisible(True)
            self.Stack_Buff.setVisible(True)
        elif cur == 4:
            self.special.setVisible(True)
            self.Stack_Special.setVisible(True)



    def potion_Widget(self):
        self.healing = QWidget()
        self.rare_healing = QWidget()
        self.spirit_healing = QWidget()
        self.sspirit_healing = QWidget()

        UIitem = Tab_Item.Product_Potion
        UIitem.Healing(self)
        UIitem.Rare_Healing(self)
        UIitem.Spirit_Healing(self)
        UIitem.SSpirit_Healing(self)

        self.Stack_Potion = QStackedWidget(self)
        self.Stack_Potion.addWidget(self.healing)
        self.Stack_Potion.addWidget(self.rare_healing)
        self.Stack_Potion.addWidget(self.spirit_healing)
        self.Stack_Potion.addWidget(self.sspirit_healing)

        return self.Stack_Potion

    def attack_Widget(self):
        self.flash = QWidget()
        self.flame = QWidget()
        self.cold_air = QWidget()
        self.electric = QWidget()
        self.dark = QWidget()
        self.corrosion = QWidget()
        self.thunder = QWidget()
        self.tornado = QWidget()
        self.clay = QWidget()
        self.sleeping = QWidget()
        self.holy = QWidget()
        self.destruction = QWidget()
        self.sflash = QWidget()
        self.sflame = QWidget()
        self.scold_air = QWidget()
        self.selectric = QWidget()
        self.sclay = QWidget()
        self.stornado = QWidget()
        self.sdark = QWidget()
        self.ssleeping = QWidget()
        self.sdestruction = QWidget()
        self.scorrosion = QWidget()
        self.sholy = QWidget()

        UIitem = Tab_Item.Product_Attack
        UIitem.Flash(self)
        UIitem.Flame(self)
        UIitem.Cold_Air(self)
        UIitem.Electric(self)
        UIitem.Dark(self)
        UIitem.Corrosion(self)
        UIitem.Thunder(self)
        UIitem.Tornado(self)
        UIitem.Clay(self)
        UIitem.Sleeping(self)
        UIitem.Holy(self)
        UIitem.Destruction(self)
        UIitem.SFlash(self)
        UIitem.SFlame(self)
        UIitem.SCold_Air(self)
        UIitem.SElectric(self)
        UIitem.SClay(self)
        UIitem.STornado(self)
        UIitem.SDark(self)
        UIitem.SSleeping(self)
        UIitem.SDestruction(self)
        UIitem.SCorrosion(self)
        UIitem.SHoly(self)

        self.Stack_Attack = QStackedWidget(self)
        self.Stack_Attack.addWidget(self.flash)
        self.Stack_Attack.addWidget(self.flame)
        self.Stack_Attack.addWidget(self.cold_air)
        self.Stack_Attack.addWidget(self.electric)
        self.Stack_Attack.addWidget(self.dark)
        self.Stack_Attack.addWidget(self.corrosion)
        self.Stack_Attack.addWidget(self.thunder)
        self.Stack_Attack.addWidget(self.tornado)
        self.Stack_Attack.addWidget(self.clay)
        self.Stack_Attack.addWidget(self.sleeping)
        self.Stack_Attack.addWidget(self.holy)
        self.Stack_Attack.addWidget(self.destruction)
        self.Stack_Attack.addWidget(self.sflash)
        self.Stack_Attack.addWidget(self.sflame)
        self.Stack_Attack.addWidget(self.scold_air)
        self.Stack_Attack.addWidget(self.selectric)
        self.Stack_Attack.addWidget(self.sclay)
        self.Stack_Attack.addWidget(self.stornado)
        self.Stack_Attack.addWidget(self.sdark)
        self.Stack_Attack.addWidget(self.ssleeping)
        self.Stack_Attack.addWidget(self.sdestruction)
        self.Stack_Attack.addWidget(self.scorrosion)
        self.Stack_Attack.addWidget(self.sholy)

        return self.Stack_Attack

    def assist_Widget(self):
        self.signal_gun = QWidget()
        self.ssignal_gun = QWidget()
        self.all_purpose = QWidget()
        self.scarecrow = QWidget()
        self.bonfire = QWidget()
        self.camouflage = QWidget()
        self.amulet = QWidget()
        self.spell = QWidget()
        self.pheromones = QWidget()
        self.sall_purpose = QWidget()
        self.scamouflage = QWidget()
        self.sbonfire = QWidget()
        self.sscarecrow = QWidget()
        self.samulet = QWidget()
        self.hiding = QWidget()
        self.trumpet = QWidget()
        self.static_time = QWidget()
        self.shiding = QWidget()

        UIitem = Tab_Item.Product_Assist
        UIitem.Signal_Gun(self)
        UIitem.SSignal_Gun(self)
        UIitem.All_purpose(self)
        UIitem.Scarecrow(self)
        UIitem.Bonfire(self)
        UIitem.Camouflage(self)
        UIitem.Amulet(self)
        UIitem.Spell(self)
        UIitem.Pheromones(self)
        UIitem.SAll_purpose(self)
        UIitem.SCamouflage(self)
        UIitem.SBonfire(self)
        UIitem.SScarecrow(self)
        UIitem.SAmulet(self)
        UIitem.Hiding(self)
        UIitem.Trumpet(self)
        UIitem.Static_time(self)
        UIitem.SHiding(self)

        self.Stack_Assist = QStackedWidget(self)
        self.Stack_Assist.addWidget(self.signal_gun)
        self.Stack_Assist.addWidget(self.ssignal_gun)
        self.Stack_Assist.addWidget(self.all_purpose)
        self.Stack_Assist.addWidget(self.scarecrow)
        self.Stack_Assist.addWidget(self.bonfire)
        self.Stack_Assist.addWidget(self.camouflage)
        self.Stack_Assist.addWidget(self.amulet)
        self.Stack_Assist.addWidget(self.spell)
        self.Stack_Assist.addWidget(self.pheromones)
        self.Stack_Assist.addWidget(self.sall_purpose)
        self.Stack_Assist.addWidget(self.scamouflage)
        self.Stack_Assist.addWidget(self.sbonfire)
        self.Stack_Assist.addWidget(self.sscarecrow)
        self.Stack_Assist.addWidget(self.samulet)
        self.Stack_Assist.addWidget(self.hiding)
        self.Stack_Assist.addWidget(self.trumpet)
        self.Stack_Assist.addWidget(self.static_time)
        self.Stack_Assist.addWidget(self.shiding)

        return self.Stack_Assist

    def buff_Widget(self):
        self.flag = QWidget()
        self.protection = QWidget()
        self.quick = QWidget()
        self.sprotection = QWidget()
        self.squick = QWidget()
        self.arousal = QWidget()
        self.atropine = QWidget()

        UIitem = Tab_Item.Product_Buff
        UIitem.Flag(self)
        UIitem.Protection(self)
        UIitem.Quick(self)
        UIitem.SProtection(self)
        UIitem.SQuick(self)
        UIitem.Arousal(self)
        UIitem.Atropine(self)

        self.Stack_Buff = QStackedWidget(self)
        self.Stack_Buff.addWidget(self.flag)
        self.Stack_Buff.addWidget(self.protection)
        self.Stack_Buff.addWidget(self.quick)
        self.Stack_Buff.addWidget(self.sprotection)
        self.Stack_Buff.addWidget(self.squick)
        self.Stack_Buff.addWidget(self.arousal)
        self.Stack_Buff.addWidget(self.atropine)

        return self.Stack_Buff

    def special_Widget(self):
        self.low_ounion_h = QWidget()
        self.mid_ounion_h = QWidget()
        self.high_ounion_h = QWidget()
        self.low_ounion_f = QWidget()
        self.mid_ounion_f = QWidget()
        self.high_ounion_f = QWidget()
        self.low_ounion_a = QWidget()
        self.mid_ounion_a = QWidget()
        self.high_ounion_a = QWidget()

        UIitem = Tab_Item.Product_Special
        UIitem.Low_Ounion_H(self)
        UIitem.Mid_Ounion_H(self)
        UIitem.High_Ounion_H(self)
        UIitem.Low_Ounion_F(self)
        UIitem.Mid_Ounion_F(self)
        UIitem.High_Ounion_F(self)
        UIitem.Low_Ounion_A(self)
        UIitem.Mid_Ounion_A(self)
        UIitem.High_Ounion_A(self)

        self.Stack_Special = QStackedWidget(self)
        self.Stack_Special.addWidget(self.low_ounion_h)
        self.Stack_Special.addWidget(self.mid_ounion_h)
        self.Stack_Special.addWidget(self.high_ounion_h)
        self.Stack_Special.addWidget(self.low_ounion_f)
        self.Stack_Special.addWidget(self.mid_ounion_f)
        self.Stack_Special.addWidget(self.high_ounion_f)
        self.Stack_Special.addWidget(self.low_ounion_a)
        self.Stack_Special.addWidget(self.mid_ounion_a)
        self.Stack_Special.addWidget(self.high_ounion_a)

        return self.Stack_Special




    def display(self, i):
        self.Stack_Product.setCurrentIndex(i)

    def display_potion(self, i):
        self.Stack_Potion.setCurrentIndex(i)

    def display_attack(self, i):
        self.Stack_Attack.setCurrentIndex(i)

    def display_assist(self, i):
        self.Stack_Assist.setCurrentIndex(i)

    def display_buff(self, i):
        self.Stack_Buff.setCurrentIndex(i)

    def display_special(self, i):
        self.Stack_Special.setCurrentIndex(i)