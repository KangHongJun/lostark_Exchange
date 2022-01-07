from bs4 import BeautifulSoup
import sqlite3
import Function


con = sqlite3.connect("./Reinforce.db")
cursor = con.cursor()

def Reforging(driver):
   A_url = 'https://lostark.game.onstove.com/Market/List_v2?firstCategory=60000&secondCategory=60200' \
            '&characterClass=&tier=0&grade=99%27%20\%20%27&itemName=&pageNo=1&isInit=false&sortType=1&_=1623805762408'

   driver.get(A_url)
   html = driver.page_source
   soup = BeautifulSoup(html, 'html.parser')

   # 회복약
   Healing = soup.select_one('#tbodyItemList > tr:nth-child(1) > td:nth-child(4) > div > em')
   Healing = Function.check(Healing)

   # 고급 회복약
   Rare_Healing = soup.select_one('#tbodyItemList > tr:nth-child(2) > td:nth-child(4) > div > em')
   Rare_Healing = Function.check(Rare_Healing)

   # 정령의 회복약
   Spirit_Healing = soup.select_one('#tbodyItemList > tr:nth-child(3) > td:nth-child(4) > div > em')
   Spirit_Healing = Function.check(Spirit_Healing)

   # 빛나는 정령의 회복약
   SSpirit_Healing = soup.select_one('#tbodyItemList > tr:nth-child(4) > td:nth-child(4) > div > em')
   SSpirit_Healing = Function.check(SSpirit_Healing)

   con = sqlite3.connect("./Battle_Item.db")
   cursor = con.cursor()
   cursor.execute("UPDATE Potion SET Price = ? WHERE NAME = '회복약'", (Healing,))
   cursor.execute("UPDATE Potion SET Price = ? WHERE NAME = '고급 회복약'", (Rare_Healing,))
   cursor.execute("UPDATE Potion SET Price = ? WHERE NAME = '정령의 회복약'", (Spirit_Healing,))
   cursor.execute("UPDATE Potion SET Price = ? WHERE NAME = '빛나는 정령의 회복약'", (SSpirit_Healing,))
   con.commit()
