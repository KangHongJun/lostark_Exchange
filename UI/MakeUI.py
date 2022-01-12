from PyQt5.QtWidgets import *
from UI import Tab_Item

def Make_Tab(self):
    # QWidget 적용
    tabs = QTabWidget()
    tabs.addTab(self.Tab_Item(Tab_Reinforce()), '강화재료')
    tabs.addTab(self.Tab_Item(Tab_Battle_Item()), '전투용품')
    tabs.addTab(self.Tab_Item(Tab_Life()), '생활')
    tabs.addTab(self.Tab_Item(Tab_Product()), '제작정보')
    self.setCentralWidget(tabs)

class Tab_Reinforce(QWidget):
    def __init__(self):
        super(Tab_Reinforce, self).__init__()
        self.Reinforce = QListWidget()
        self.Reinforce.insertItem(0, '전체')
        self.Reinforce.insertItem(1, '재련 재료')
        self.Reinforce.insertItem(2, '재련 추가 재료')

        self.ui_ref_all = QWidget()
        self.ui_ref = QWidget()
        self.ui_ref_add = QWidget()

        UIitem = Tab_Item.Item_Reinfoece
        UIitem.UI_Reforging_ALL(self)
        UIitem.UI_Reforging(self)
        UIitem.UI_Reforging_Add(self)

        self.Stack = QStackedWidget(self)
        self.Stack.addWidget(self.ui_ref_all)
        self.Stack.addWidget(self.ui_ref)
        self.Stack.addWidget(self.ui_ref_add)

        hbox = QHBoxLayout(self)
        hbox.addWidget(self.Reinforce)
        hbox.addWidget(self.Stack)

        self.setLayout(hbox)
        self.Reinforce.currentRowChanged.connect(self.display)

    def display(self, i):
        self.Stack.setCurrentIndex(i)

class Tab_Battle_Item(QWidget):
    def __init__(self):
        super(Tab_Battle_Item, self).__init__()
        self.battle_item = QListWidget()
        self.battle_item.insertItem(0, '전체')
        self.battle_item.insertItem(1, '배틀아이템 - 회복형')
        self.battle_item.insertItem(2, '배틀아이템 - 공격형')
        self.battle_item.insertItem(3, '배틀아이템 - 기능성')
        self.battle_item.insertItem(4, '배틀아이템 - 버프형')


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

        hbox = QHBoxLayout(self)
        hbox.addWidget(self.battle_item)
        hbox.addWidget(self.Stack)

        self.setLayout(hbox)
        self.battle_item.currentRowChanged.connect(self.display)

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

        hbox = QHBoxLayout(self)
        hbox.addWidget(self.Life)
        hbox.addWidget(self.Stack)

        self.setLayout(hbox)
        self.Life.currentRowChanged.connect(self.display)

    def display(self, i):
        self.Stack.setCurrentIndex(i)

class Tab_Product(QWidget):
    a = 0
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

        self.Stack = QStackedWidget(self)

        hbox = QHBoxLayout(self)
        hbox.addWidget(self.product)
        hbox.addWidget(self.potion)
        hbox.addWidget(self.attack)
        hbox.addWidget(self.assist)
        hbox.addWidget(self.buff)
        hbox.addWidget(self.special)
        # hbox.addWidget(self.Stack)
        hbox.addWidget(self.Stack2)

        self.attack.setVisible(False)
        self.assist.setVisible(False)
        self.buff.setVisible(False)
        self.special.setVisible(False)

        self.setLayout(hbox)
        self.product.currentRowChanged.connect(self.display)
        #self.show()

    def potion(self):
        self.potion = QListWidget()
        self.potion.insertItem(0, '회복약')
        self.potion.insertItem(1, '고급 회복약')
        self.potion.insertItem(2, '정령의 회복약')
        self.potion.insertItem(2, '빛나는 정령의 회복약')

        self.healing = QWidget()
        self.rare_healing = QWidget()
        self.spirit_healing = QWidget()
        self.sspirit_healing = QWidget()

        UIitem = Tab_Item.Product
        UIitem.Healing(self)
        UIitem.Rare_Healing(self)
        UIitem.Spirit_Healing(self)
        UIitem.SSpirit_Healing(self)

        self.Stack2 = QStackedWidget(self)
        self.Stack2.addWidget(self.healing)
        self.Stack2.addWidget(self.rare_healing)
        self.Stack2.addWidget(self.spirit_healing)
        self.Stack2.addWidget(self.sspirit_healing)
        self.potion.currentRowChanged.connect(self.display2)

        return self.potion

    def attack(self):
        self.attack = QListWidget()
        self.attack.insertItem(0, '공격1')
        self.attack.insertItem(1, '공격2')
        self.attack.insertItem(2, '공격격')

        return self.attack

    def assist(self):
        self.assist = QListWidget()
        self.assist.insertItem(0, '기능')
        self.assist.insertItem(1, '기능')
        self.assist.insertItem(2, '기능')

        return self.assist

    def buff(self):
        self.buff = QListWidget()
        self.buff.insertItem(0, 'buff')
        self.buff.insertItem(1, 'buff')
        self.buff.insertItem(2, 'buff')

        return self.buff

    def special(self):
        self.special = QListWidget()
        self.special.insertItem(0, '특수1')
        self.special.insertItem(1, '특수2')
        self.special.insertItem(2, '특수3')

        return self.special

    def clicked(self):
        cur = self.product.currentRow()
        if cur == 0:
            self.potion.setVisible(True)
            self.attack.setVisible(False)
            self.assist.setVisible(False)
            self.buff.setVisible(False)
            self.special.setVisible(False)
        elif cur == 1:
            self.potion.setVisible(False)
            self.attack.setVisible(True)
            self.assist.setVisible(False)
            self.buff.setVisible(False)
            self.special.setVisible(False)
        elif cur == 2:
            self.potion.setVisible(False)
            self.attack.setVisible(False)
            self.assist.setVisible(True)
            self.buff.setVisible(False)
            self.special.setVisible(False)
        elif cur == 3:
            self.potion.setVisible(False)
            self.attack.setVisible(False)
            self.assist.setVisible(False)
            self.buff.setVisible(True)
            self.special.setVisible(False)
        elif cur == 4:
            self.potion.setVisible(False)
            self.attack.setVisible(False)
            self.assist.setVisible(False)
            self.buff.setVisible(False)
            self.special.setVisible(True)


    def display(self, i):
        self.Stack.setCurrentIndex(i)

    def display2(self, i):
        self.Stack2.setCurrentIndex(i)