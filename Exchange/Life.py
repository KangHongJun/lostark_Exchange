from bs4 import BeautifulSoup
import sqlite3
import Function

con = sqlite3.connect("./Life.db")
cursor = con.cursor()

def ExPlant(driver):
   Purl = 'https://lostark.game.onstove.com/Market/List_v2?firstCategory=90000' \
           '&secondCategory=90200&characterClass=&tier=0&grade=99&itemName=&pageNo=1&isInit=false&sortType=1&_=1623805762402'

   driver.get(Purl)
   html = driver.page_source
   soup = BeautifulSoup(html, 'html.parser')

   # 들꽃
   Flower = soup.select_one('#tbodyItemList > tr:nth-child(1) > td:nth-child(4) > div > em')
   Flower = Function.check(Flower) / 100

   # 수줍은 들꽃
   Shy_flower = soup.select_one('#tbodyItemList > tr:nth-child(3) > td:nth-child(4) > div > em')
   Shy_flower = Function.check(Shy_flower) / 10

   # 화사한 들꽃
   Bright_flower = soup.select_one('#tbodyItemList > tr:nth-child(5) > td:nth-child(4) > div > em')
   Bright_flower = Function.check(Bright_flower) / 10

   # 투박한 버섯
   Coarse_mushroom = soup.select_one('#tbodyItemList > tr:nth-child(2) > td:nth-child(4) > div > em')
   Coarse_mushroom = Function.check(Coarse_mushroom) / 100

   # 싱싱한 버섯
   Fresh_mushroom = soup.select_one('#tbodyItemList > tr:nth-child(4) > td:nth-child(4) > div > em')
   Fresh_mushroom = Function.check(Fresh_mushroom) / 10

   # 화려한 버섯
   Fancy_mushroom = soup.select_one('#tbodyItemList > tr:nth-child(6) > td:nth-child(4) > div > em')
   Fancy_mushroom = Function.check(Fancy_mushroom) / 10

   cursor.execute("UPDATE Plant SET Price = ? WHERE NAME = '들꽃'", (Flower,))
   cursor.execute("UPDATE Plant SET Price = ? WHERE NAME = '수줍은 들꽃'", (Shy_flower,))
   cursor.execute("UPDATE Plant SET Price = ? WHERE NAME = '화사한 들꽃'", (Bright_flower,))
   cursor.execute("UPDATE Plant SET Price = ? WHERE NAME = '투박한 버섯'", (Coarse_mushroom,))
   cursor.execute("UPDATE Plant SET Price = ? WHERE NAME = '싱싱한 버섯'", (Fresh_mushroom,))
   cursor.execute("UPDATE Plant SET Price = ? WHERE NAME = '화려한 버섯'", (Fancy_mushroom,))
   con.commit()

def ExLogging(driver):
   Lurl = "https://lostark.game.onstove.com/Market/List_v2?firstCategory=90000&secondCategory=90300" \
          "&characterClass=&tier=0&grade=99&itemName=&pageNo=1&isInit=false&sortType=1&_=1623805762403"
   driver.get(Lurl)
   html = driver.page_source
   soup = BeautifulSoup(html, 'html.parser')

   # 목재
   Wood = soup.select_one('#tbodyItemList > tr:nth-child(1) > td:nth-child(4) > div > em')
   Wood = Function.check(Wood) / 100

   # 부드러운 목재
   Soft_Wood = soup.select_one('#tbodyItemList > tr:nth-child(2) > td:nth-child(4) > div > em')
   Soft_Wood = Function.check(Soft_Wood) / 10

   # 튼튼한 목재
   Strong_Wood = soup.select_one('#tbodyItemList > tr:nth-child(3) > td:nth-child(4) > div > em')
   Strong_Wood = Function.check(Strong_Wood) / 10

   cursor.execute("UPDATE Logging SET Price = ? WHERE NAME = '목재'", (Wood,))
   cursor.execute("UPDATE Logging SET Price = ? WHERE NAME = '부드러운 목재'", (Soft_Wood,))
   cursor.execute("UPDATE Logging SET Price = ? WHERE NAME = '튼튼한 목재'", (Strong_Wood,))
   con.commit()

def ExMining(driver):
   Eurl = "https://lostark.game.onstove.com/Market/List_v2?firstCategory=90000&secondCategory=90400" \
       "&characterClass=&tier=0%27%20\%20%27&grade=99&itemName=&pageNo=1&isInit=false&sortType=1&_=1623805762404"

   driver.get(Eurl)
   html = driver.page_source
   soup = BeautifulSoup(html, 'html.parser')

   # 철광석
   Iron_ore = soup.select_one('#tbodyItemList > tr:nth-child(1) > td:nth-child(4) > div > em')
   Iron_ore = Function.check(Iron_ore) / 100

   # 묵직한 철광석
   Heavy_Iron_ore = soup.select_one('#tbodyItemList > tr:nth-child(2) > td:nth-child(4) > div > em')
   Heavy_Iron_ore = Function.check(Heavy_Iron_ore) / 10

   # 단단한 철광석
   Hard_Iron_ore = soup.select_one('#tbodyItemList > tr:nth-child(3) > td:nth-child(4) > div > em')
   Hard_Iron_ore = Function.check(Hard_Iron_ore) / 10

   cursor.execute("UPDATE Mining SET Price = ? WHERE NAME = '철광석'", (Iron_ore,))
   cursor.execute("UPDATE Mining SET Price = ? WHERE NAME = '묵직한 철광석'", (Heavy_Iron_ore,))
   cursor.execute("UPDATE Mining SET Price = ? WHERE NAME = '단단한 철광석'", (Hard_Iron_ore,))
   con.commit()

def ExHunting(driver):
   Hurl = "https://lostark.game.onstove.com/Market/List_v2?firstCategory=90000&secondCategory=90500" \
          "&characterClass=&tier=0&grade=99&itemName=&pageNo=1&isInit=false&sortType=1&_=1623805762405"

   driver.get(Hurl)
   html = driver.page_source
   soup = BeautifulSoup(html, 'html.parser')

   # 다듬은 생고기
   Meat = soup.select_one('#tbodyItemList > tr:nth-child(2) > td:nth-child(4) > div > em')
   Meat = Function.check(Meat) / 10

   # 두툼한 생고기(100)
   Thick_Meat = soup.select_one('#tbodyItemList > tr:nth-child(1) > td:nth-child(4) > div > em')
   Thick_Meat = Function.check(Thick_Meat) / 100

   # 칼다르 두툼한 생고기
   K_Meat = soup.select_one('#tbodyItemList > tr:nth-child(4) > td:nth-child(4) > div > em')
   K_Meat = Function.check(K_Meat) / 10

   # 오레하 두툼한 생고기
   O_Meat = soup.select_one('#tbodyItemList > tr:nth-child(5) > td:nth-child(4) > div > em')
   O_Meat = Function.check(O_Meat) / 10

   # 질긴가죽
   Tough_Leather = soup.select_one('#tbodyItemList > tr:nth-child(3) > td:nth-child(4) > div > em')
   Tough_Leather = Function.check(Tough_Leather) / 10

   cursor.execute("UPDATE Hunting SET Price = ? WHERE NAME = '다듬은 생고기'", (Meat,))
   cursor.execute("UPDATE Hunting SET Price = ? WHERE NAME = '두툼한 생고기'", (Thick_Meat,))
   cursor.execute("UPDATE Hunting SET Price = ? WHERE NAME = '칼다르 생고기'", (K_Meat,))
   cursor.execute("UPDATE Hunting SET Price = ? WHERE NAME = '오레하 생고기'", (O_Meat,))
   cursor.execute("UPDATE Hunting SET Price = ? WHERE NAME = '질긴가죽'", (Tough_Leather,))
   con.commit()

def ExFishing(driver):
   Furl = "https://lostark.game.onstove.com/Market/List_v2?firstCategory=90000" \
       "&secondCategory=90600&characterClass=&tier=0%27%20\%20%27&grade=99&itemName=&pageNo=1&isInit=false&sortType=1&_=1623805762406%27"

   driver.get(Furl)
   html = driver.page_source
   soup = BeautifulSoup(html, 'html.parser')

   # 칼다르 태양잉어
   K_Carp = soup.select_one('#tbodyItemList > tr:nth-child(4) > td:nth-child(4) > div > em')
   K_Carp = Function.check(K_Carp) / 10

   # 오레하 태양잉어
   O_Carp = soup.select_one('#tbodyItemList > tr:nth-child(5) > td:nth-child(4) > div > em')
   O_Carp = Function.check(O_Carp) / 10

   # 붉은 살 생선
   Red_Fish = soup.select_one('#tbodyItemList > tr:nth-child(2) > td:nth-child(4) > div > em')
   Red_Fish = Function.check(Red_Fish) / 10

   # 자연산 진주
   Pearl = soup.select_one('#tbodyItemList > tr:nth-child(3) > td:nth-child(4) > div > em')
   Pearl = Function.check(Pearl) / 10

   # 생선
   Fish = soup.select_one('#tbodyItemList > tr:nth-child(1) > td:nth-child(4) > div > em')
   Fish = Function.check(Fish) / 100

   cursor.execute("UPDATE Fishing SET Price = ? WHERE NAME = '칼다르 태양잉어'", (K_Carp,))
   cursor.execute("UPDATE Fishing SET Price = ? WHERE NAME = '오레하 태양잉어'", (O_Carp,))
   cursor.execute("UPDATE Fishing SET Price = ? WHERE NAME = '붉은 살 생선'", (Red_Fish,))
   cursor.execute("UPDATE Fishing SET Price = ? WHERE NAME = '자연산 진주'", (Pearl,))
   cursor.execute("UPDATE Fishing SET Price = ? WHERE NAME = '생선'", (Fish,))
   con.commit()

def ExArchaeology(driver):
   Aurl = 'https://lostark.game.onstove.com/Market/List_v2?firstCategory=90000&secondCategory=90700&characterClass=&tier=0' \
           '&grade=99&itemName=&pageNo=1&isInit=false&sortType=1&_=1623805762408'

   driver.get(Aurl)
   html = driver.page_source
   soup = BeautifulSoup(html, 'html.parser')

   # 칼다르 유물
   K_Relic = soup.select_one('#tbodyItemList > tr:nth-child(3) > td:nth-child(4) > div > em')
   K_Relic = Function.check(K_Relic) / 10

   # 오레하 유물
   O_Relic = soup.select_one('#tbodyItemList > tr:nth-child(4) > td:nth-child(4) > div > em')
   O_Relic = Function.check(O_Relic) / 10

   # 희귀한 유물
   Rare_Relic = soup.select_one('#tbodyItemList > tr:nth-child(2) > td:nth-child(4) > div > em')
   Rare_Relic = Function.check(Rare_Relic) / 10

   # 고대 유물
   Ancient_Relic = soup.select_one('#tbodyItemList > tr:nth-child(1) > td:nth-child(4) > div > em')
   Ancient_Relic = Function.check(Ancient_Relic) / 100

   # 고고학 결정(3)
   cursor.execute("UPDATE Archaeology SET Price = ? WHERE NAME = '칼다르 유물'", (K_Relic,))
   cursor.execute("UPDATE Archaeology SET Price = ? WHERE NAME = '오레하 유물'", (O_Relic,))
   cursor.execute("UPDATE Archaeology SET Price = ? WHERE NAME = '희귀한 유물'", (Rare_Relic,))
   cursor.execute("UPDATE Archaeology SET Price = ? WHERE NAME = '고대 유물'", (Ancient_Relic,))
   con.commit()
   con.close()