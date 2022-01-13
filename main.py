import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from UI import MakeUI
import Function

# 위젯
class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        MakeUI.Make_Tab(self)
        Function.UpdataDB()

    def initUI(self):
        # UI 초기화
        self.setWindowIcon(QIcon('lostark.jpg'))
        self.setWindowTitle('거래소')
        self.setGeometry(100, 100, 800, 500)
        # 하단 날짜 출력
        self.date = QDate.currentDate()
        self.statusBar().showMessage(self.date.toString(Qt.DefaultLocaleLongDate))

    def Tab_Item(self,tab):
        wg = tab
        self.setCentralWidget(wg)

        hbox = QHBoxLayout()
        hbox.addWidget(wg)

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











