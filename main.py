import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from UI import textUI

'''
#selenium 사용하기위한 webdriver옵션 세팅
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--de')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
caps = DesiredCapabilities().CHROME
caps["pageLoadStrategy"]="none"

driver = webdriver.Chrome('chromedriver',options=chrome_options)

#사이트 접속
driver.get(
    'https://member.onstove.com/auth/login?inflow_path=lost_ark&game_no=45&redirect_url=https%3a%2f%2flostark.game.onstove.com%2fMarket')
driver.maximize_window()
login_x_path = '/html/body/div[1]/div[2]/div/fieldset[1]/div[4]/button'

#로그인
ID = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/fieldset[1]/div[1]/div[1]/input')
ID.clear()
ID.send_keys('starmine325@gmail.com')
PW = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/fieldset[1]/div[1]/div[2]/input')
PW.clear()
PW.send_keys('starmine97@')
driver.find_element_by_xpath(login_x_path).click()

#wait 개선예정
driver.implicitly_wait(10)
driver.find_element_by_xpath('/html/body/div[2]/div/main/div/div[3]/div[1]/ul/li[8]/a').click()
'''


# DB갱신코드

# 위젯
# Speical_Item


class Special_Item(QWidget):
    a = 0

    def __init__(self):
        super(Special_Item, self).__init__()

        self.potion = QListWidget()
        self.potion.insertItem(0, '포션1')
        self.potion.insertItem(1, '포션1')
        self.potion.insertItem(2, '포션1')
        self.potion.itemClicked.connect(self.clicked)

        self.potion2 = QListWidget()
        self.potion2.insertItem(0, '포션2')
        self.potion2.insertItem(1, '포션2')
        self.potion2.insertItem(2, '포션2')

        self.potion3 = QListWidget()
        self.potion3.insertItem(0, '포션3')
        self.potion3.insertItem(1, '포션3')
        self.potion3.insertItem(2, '포션3')

        self.low0 = QWidget()
        self.low1 = QWidget()
        self.low2 = QWidget()

        textUI.low0(self)
        textUI.low1(self)
        textUI.low2(self)

        self.Stack = QStackedWidget(self)
        self.Stack.addWidget(self.low0)
        self.Stack.addWidget(self.low1)
        self.Stack.addWidget(self.low2)

        hbox = QHBoxLayout(self)
        hbox.addWidget(self.potion)
        hbox.addWidget(self.potion2)
        hbox.addWidget(self.potion3)
        hbox.addWidget(self.Stack)

        self.setLayout(hbox)
        self.potion.currentRowChanged.connect(self.display)
        self.setGeometry(300, 50, 10, 10)
        self.show()

    def clicked(self):
        cur = self.potion.currentRow()
        if(cur==1):
            self.set_potion(1)
        else:
            self.set_potion(0)
        print(cur)

    def set_potion(self,i):
        if(i==1):
            self.potion2.setVisible(False)
        else:
            self.potion2.setVisible(True)


    def display(self, i):
        self.Stack.setCurrentIndex(i)


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.make_tap()

    def initUI(self):
        # UI 기본
        self.setWindowIcon(QIcon('lostark.jpg'))
        self.setWindowTitle('제작효율')
        self.setGeometry(100, 100, 1000, 500)
        # 하단 날짜 출력
        self.date = QDate.currentDate()
        self.statusBar().showMessage(self.date.toString(Qt.DefaultLocaleLongDate))

    def make_tap(self):
        # QWidget 적용
        tabs = QTabWidget()
        tabs.addTab(self.Tab_Special_Item(), '포션')
        tabs.addTab(self.Tab_Special_Item(), '특수 아이템')
        tabs.addTab(self.Tab_Special_Item(), '공격 아이템')
        tabs.addTab(self.Tab_Special_Item(), '전투보조 아이템')
        self.setCentralWidget(tabs)

    def Tab_Special_Item(self):
        wg = Special_Item()
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











