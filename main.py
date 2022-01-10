import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from Exchange import Battle_Item, Life, Reinforce
from UI import Tab_Item, MakeTab

'''
#selenium 사용하기위한 webdriver옵션 세팅
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument("disable-gpu")
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
driver.implicitly_wait(10)
driver.find_element_by_xpath('/html/body/div[2]/div/main/div/div[3]/div[1]/ul/li[8]/a').click()

# DB갱신

Battle_Item.ExPotion(driver)
Battle_Item.ExBuff(driver)
Battle_Item.ExAttack(driver)
Battle_Item.ExAssistance(driver)
Life.ExPlant(driver)
Life.ExLogging(driver)
Life.ExMining(driver)
Life.ExHunting(driver)
Life.ExFishing(driver)
Life.ExArchaeology(driver)
Reinforce.ExReforging(driver)
Reinforce.ExReforging_Add(driver)
'''
print("start")



# 위젯]
class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        MakeTab.Make_Tab(self)

    def initUI(self):
        # UI 기본
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











