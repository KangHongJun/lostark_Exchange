from PyQt5.QtWidgets import *
from UI import Tab_Item


def Make_Tab(self):
    # QWidget 적용
    tabs = QTabWidget()
    tabs.addTab(self.Tab_Item(Tab_Reinforce()), '강화재료')
    #   tabs.addTab(self.Tab_Special_Item(), '전투용품')
    #  tabs.addTab(self.Tab_Special_Item(), '생활')
    # tabs.addTab(self.Tab_Special_Item(), '제작')
    self.setCentralWidget(tabs)

class Tab_Reinforce(QWidget):
    a = 0
    def __init__(self):
        super(Tab_Reinforce, self).__init__()
        self.potion = QListWidget()
        self.potion.resize(300,500)
        self.potion.insertItem(0, '전체')
        self.potion.insertItem(1, '재련 재료')
        self.potion.insertItem(2, '재련 추가 재료')

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
        hbox.addWidget(self.potion)
        hbox.addWidget(self.Stack)

        self.setLayout(hbox)
        self.potion.currentRowChanged.connect(self.display)
        self.setGeometry(300, 50, 10, 10)
        self.show()

    def display(self, i):
        self.Stack.setCurrentIndex(i)

class Tab_Battle_Item(QWidget):
    a = 0
    def __init__(self):
        super(Tab_Battle_Item, self).__init__()
        self.potion = QListWidget()
        self.potion.resize(300,500)
        self.potion.insertItem(0, '전체')
        self.potion.insertItem(1, '배틀아이템 - 회복형')
        self.potion.insertItem(2, '배틀아이템 - 공격형')
        self.potion.insertItem(3, '배틀아이템 - 기능성')
        self.potion.insertItem(4, '배틀아이템 - 버프형')


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
        hbox.addWidget(self.potion)
        hbox.addWidget(self.Stack)

        self.setLayout(hbox)
        self.potion.currentRowChanged.connect(self.display)
        self.setGeometry(300, 50, 10, 10)
        self.show()

    def display(self, i):
        self.Stack.setCurrentIndex(i)