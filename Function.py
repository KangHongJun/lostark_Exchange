from Exchange import Battle_Item, Life, Reinforce
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities


#selenium 사용하기위한 webdriver옵션 세팅
def UpdataDB():
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
    driver.get(
        'https://member.onstove.com/auth/login?inflow_path=lost_ark&game_no=45&redirect_url=https%3a%2f%2flostark.game.onstove.com%2fMarket')
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

#수수료 계산
def Fee(value):
    if (value == 1):
      return 0
    elif (value < 20):
      return 1
    elif ((value * 0.05) % 10 != 0):
      value = float(value * 0.05) + 1
      return float(value)
    elif ((value * 0.05) % 10 == 0):
      return float(value * 0.05)

#크롤링 데이터 None체크 후 return
def check(value):
    if value is None:
        value = 0
        return value
    else:
        # ','이 포함 됐다면 ',' 제거
        if( ',' in value.text):
            value = value.text
            value = value.replace(",","")
            value = int(value)
            return value
        else:
            value = int(value.text)
            return value