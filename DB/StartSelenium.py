from DB import SaveData
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities

#DB갱신
def UpdataDB():
    # selenium 사용하기위한 webdriver옵션 세팅
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument("disable-gpu")
    chrome_options.add_argument('--de')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    caps = DesiredCapabilities().CHROME
    caps["pageLoadStrategy"] = "none"
    driver = webdriver.Chrome('chromedriver', options=chrome_options)

    # 사이트 접속
    driver.get('https://member.onstove.com/auth/login?inflow_path=lost_ark&game_no'
               '=45&redirect_url=https%3a%2f%2flostark.game.onstove.com%2fMarket')
    driver.maximize_window()
    login_x_path = '/html/body/div[1]/div[2]/div/fieldset[1]/div[4]/button'

    # 로그인
    ID = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/fieldset[1]/div[1]/div[1]/input')
    ID.clear()
    ID.send_keys('starmine325@gmail.com')
    PW = driver.find_element_by_xpath('/html/body/div[1]/div[2]/div/fieldset[1]/div[1]/div[2]/input')
    PW.clear()
    PW.send_keys('starmine97@')
    driver.find_element_by_xpath(login_x_path).click()
    driver.implicitly_wait(10)
    driver.find_element_by_xpath('/html/body/div[2]/div/main/div/div[3]/div[1]/ul/li[8]/a').click()






    #DB갱신
    Reinforce=SaveData.Reinforce
    Reinforce.ExReforging(driver,"./Reinforce.db")
    Reinforce.ExReforging_Add(driver,"./Reinforce.db")

    Battle_Item = SaveData.Battle_Item
    Battle_Item.ExPotion(driver,"./Battle_Item.db")
    Battle_Item.ExBuff(driver,"./Battle_Item.db")
    Battle_Item.ExAttack(driver,"./Battle_Item.db")
    Battle_Item.ExAssistance(driver,"./Battle_Item.db")

    Life = SaveData.Life
    Life.ExPlant(driver,"./Life.db")
    Life.ExLogging(driver,"./Life.db")
    Life.ExMining(driver,"./Life.db")
    Life.ExHunting(driver,"./Life.db")
    Life.ExFishing(driver,"./Life.db")
    Life.ExArchaeology(driver,"./Life.db")


