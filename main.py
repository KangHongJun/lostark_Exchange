import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from UI import MakeUI
from DB import StartSelenium

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        #UI 생성 - 탭
        MakeUI.Make_Tab(self)
        #selenium사용하여 DB업데이트
        StartSelenium.UpdataDB()

    def initUI(self):
        # 기본 UI설정
        self.setWindowIcon(QIcon('lostark.jpg'))
        self.setWindowTitle('Exchange')
        self.setGeometry(100, 100, 800, 500)
        # 하단 날짜 출력
        self.date = QDate.currentDate()
        self.statusBar().showMessage(self.date.toString(Qt.DefaultLocaleLongDate))

    def Tab_Item(self,tab):
        self.setCentralWidget(tab)

        hbox = QHBoxLayout()
        hbox.addWidget(tab)

        vbox = QVBoxLayout()
        vbox.addLayout(hbox)

        tab = QWidget()
        tab.setLayout(vbox)
        return tab

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main()
    ex.show()
    sys.exit(app.exec_())








