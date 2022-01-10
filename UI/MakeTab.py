from PyQt5.QtWidgets import *
from UI import Tab_Item

def Make_Tab(self):
    # QWidget 적용
    tabs = QTabWidget()
    tabs.addTab(self.Tab_Item(Tab_Reinforce()), '강화재료')
    tabs.addTab(self.Tab_Item(Tab_Battle_Item()), '전투용품')
    tabs.addTab(self.Tab_Item(Tab_Life()), '생활')
    # tabs.addTab(self.Tab_Item(), '제작')
    self.setCentralWidget(tabs)

class Tab_Reinforce(QWidget):
    def __init__(self):
        super(Tab_Reinforce, self).__init__()
        self.Reinforce = QListWidget()
        self.Reinforce.resize(300,500)
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
        self.setGeometry(300, 50, 10, 10)
        self.show()

    def display(self, i):
        self.Stack.setCurrentIndex(i)

class Tab_Battle_Item(QWidget):
    def __init__(self):
        super(Tab_Battle_Item, self).__init__()
        self.battle_item = QListWidget()
        self.battle_item.resize(300,500)
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
        self.setGeometry(300, 50, 10, 10)
        self.show()

    def display(self, i):
        self.Stack.setCurrentIndex(i)

class Tab_Life(QWidget):
    def __init__(self):
        super(Tab_Life, self).__init__()
        self.Life = QListWidget()
        self.Life.resize(300,500)
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
        self.setGeometry(300, 50, 10, 10)
        self.show()

    def display(self, i):
        self.Stack.setCurrentIndex(i)