import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities

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

#DB갱신코드

#위젯
# Speical_Item
class Special_Item(QWidget):
    def __init__(self):
        super(Special_Item, self).__init__()

        self.leftlist = QListWidget()
        self.leftlist.insertItem(0, '하급-수렵')
        self.leftlist.insertItem(1, '중급-수렵')
        self.leftlist.insertItem(2, '상급-수렵')
        self.leftlist.insertItem(3, '하급-낚시')
        self.leftlist.insertItem(4, '중급-낚시')
        self.leftlist.insertItem(5, '상급-낚시')
        self.leftlist.insertItem(6, '하급-고고학')
        self.leftlist.insertItem(7, '중급-고고학')
        self.leftlist.insertItem(8, '상급-고고학')

        self.h_low = QWidget()
        layout = QFormLayout()

        label1 = QLabel()
        label1.setText("하급 오레하 융화재료x30\n")

        label2 = QLabel()
        label2.setText("오레하 두툼한 생고기x9")

        label3 = QLabel()
        label3.setText("두툼한 생고기x72")

        label4 = QLabel()
        label4.setText("질긴 가죽x36")

        label5 = QLabel()
        label5.setText("203골드")

        layout.addWidget(label1)
        layout.addWidget(label2)
        layout.addWidget(label3)
        layout.addWidget(label4)
        layout.addWidget(label5)

        self.h_low.setLayout(layout)

        self.Stack = QStackedWidget(self)
        self.Stack.addWidget(self.h_low)

        hbox = QHBoxLayout(self)
        hbox.addWidget(self.leftlist)
        hbox.addWidget(self.Stack)


        self.setLayout(hbox)
        self.leftlist.currentRowChanged.connect(self.display)
        self.setGeometry(300, 50, 10, 10)
        self.setWindowTitle('StackedWidget demo')
        self.show()

    def display(self, i):
        self.Stack.setCurrentIndex(i)

class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.make_tap()

    def initUI(self):
        # UI 기본
        self.setWindowIcon(QIcon('lostark.jpg'))
        self.setWindowTitle('제작효율')
        self.setGeometry(100, 100, 1000, 500)

        # 하단에 날짜 출력
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

    def Tab_Potion(self):
        wg = Special_Item()
        self.setCentralWidget(wg)

        hbox = QHBoxLayout()
        hbox.addWidget(wg)

        vbox = QVBoxLayout()
        vbox.addLayout(hbox)

        tab = QWidget()
        tab.setLayout(vbox)
        return tab

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

    def Tab_Attack_Item(self):
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
    ex = MyApp()
    ex.show()

    sys.exit(app.exec_())













