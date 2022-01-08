from bs4 import BeautifulSoup
import sqlite3
import Function

con = sqlite3.connect("./Reinforce.db")
cursor = con.cursor()

def ExReforging(driver):
   Rurl = 'https://lostark.game.onstove.com/Market/List_v2?firstCategory=50000&secondCategory=50010&' \
          'characterClass=&tier=0&grade=99%27%20\%20%27&itemName=&pageNo=1&isInit=false&sortType=1&_=1623805762408'

   driver.get(Rurl)
   html = driver.page_source
   soup = BeautifulSoup(html, 'html.parser')

   #destroying stone - DS
   # 파괴석 조각
   DS_Fragment = soup.select_one('#tbodyItemList > tr:nth-child(1) > td:nth-child(4) > div > em')
   DS_Fragment= Function.check(DS_Fragment)

   #파괴석
   DS = soup.select_one('#tbodyItemList > tr:nth-child(2) > td:nth-child(4) > div > em')
   DS = Function.check(DS)

   #파괴석 결정
   DS_crystals = soup.select_one('#tbodyItemList > tr:nth-child(3) > td:nth-child(4) > div > em')
   DS_crystals = Function.check(DS_crystals)

   #파괴강석
   DS_adamant = soup.select_one('#tbodyItemList > tr:nth-child(4) > td:nth-child(4) > div > em')
   DS_adamant = Function.check(DS_adamant)

   #guardian stone - GS
   #수호석 조각
   GS_Fragment = soup.select_one('#tbodyItemList > tr:nth-child(5) > td:nth-child(4) > div > em')
   GS_Fragment = Function.check(GS_Fragment)

   # 수호석
   GS = soup.select_one('#tbodyItemList > tr:nth-child(6) > td:nth-child(4) > div > em')
   GS = Function.check(GS)

   # 수호석 결정
   GS_crystals = soup.select_one('#tbodyItemList > tr:nth-child(7) > td:nth-child(4) > div > em')
   GS_crystals = Function.check(GS_crystals)

   # 수호강석
   GS_adamant = soup.select_one('#tbodyItemList > tr:nth-child(8) > td:nth-child(4) > div > em')
   GS_adamant = Function.check(GS_adamant)

   #조화의 파편 주머니(소)
   SHarmony = soup.select_one('#tbodyItemList > tr:nth-child(9) > td:nth-child(4) > div > em')
   SHarmony = Function.check(SHarmony)

   #생명의 파편 주머니(소)
   SLife = soup.select_one('#tbodyItemList > tr:nth-child(10) > td:nth-child(4) > div > em')
   SLife = Function.check(SLife)

   #2page
   Rurl = 'https://lostark.game.onstove.com/Market/List_v2?firstCategory=50000&secondCategory=50010' \
          '&characterClass=&tier=0&grade=99%27%20\%20%27&itemName=&pageNo=2&isInit=false&sortType=1&_=1623805762408'

   driver.get(Rurl)
   html = driver.page_source
   soup = BeautifulSoup(html, 'html.parser')

   #명예의 파편 주머니(소)
   SHonor = soup.select_one('#tbodyItemList > tr:nth-child(1) > td:nth-child(4) > div > em')
   SHonor = Function.check(SHonor)

   #하급 오레하 융합 재료
   Low_Ounion = soup.select_one('#tbodyItemList > tr:nth-child(2) > td:nth-child(4) > div > em')
   Low_Ounion = Function.check(Low_Ounion)

   # 조화의 파편 주머니(중)
   MHarmony = soup.select_one('#tbodyItemList > tr:nth-child(3) > td:nth-child(4) > div > em')
   MHarmony = Function.check(MHarmony)

   # 생명의 파편 주머니(중)
   MLife = soup.select_one('#tbodyItemList > tr:nth-child(4) > td:nth-child(4) > div > em')
   MLife = Function.check(MLife)

   # 명예의 파편 주머니(중)
   MHonor = soup.select_one('#tbodyItemList > tr:nth-child(5) > td:nth-child(4) > div > em')
   MHonor = Function.check(MHonor)

   # 중급 오레하 융합 재료
   Mid_Ounion = soup.select_one('#tbodyItemList > tr:nth-child(6) > td:nth-child(4) > div > em')
   Mid_Ounion = Function.check(Mid_Ounion)

   # 칻다르 융합 재료
   Kunion = soup.select_one('#tbodyItemList > tr:nth-child(7) > td:nth-child(4) > div > em')
   Kunion = Function.check(Kunion)

   # 조화의 파편 주머니(대)
   BHarmony = soup.select_one('#tbodyItemList > tr:nth-child(8) > td:nth-child(4) > div > em')
   BHarmony = Function.check(BHarmony)

   # 생명의 파편 주머니(대)
   BLife = soup.select_one('#tbodyItemList > tr:nth-child(9) > td:nth-child(4) > div > em')
   BLife = Function.check(BLife)

   # 명예의 파편 주머니(대)
   BHonor = soup.select_one('#tbodyItemList > tr:nth-child(10) > td:nth-child(4) > div > em')
   BHonor = Function.check(BHonor)


   #3page
   Rurl = 'https://lostark.game.onstove.com/Market/List_v2?firstCategory=50000&secondCategory=50010' \
          '&characterClass=&tier=0&grade=99%27%20\%20%27&itemName=&pageNo=3&isInit=false&sortType=1&_=1623805762408'

   driver.get(Rurl)
   html = driver.page_source
   soup = BeautifulSoup(html, 'html.parser')

   # 상급 오레하 융합
   High_Ounion = soup.select_one('#tbodyItemList > tr:nth-child(1) > td:nth-child(4) > div > em')
   High_Ounion = int(High_Ounion.text)

   cursor.execute("UPDATE Reforging SET Price = ? WHERE NAME = '파괴석 조각'", (DS_Fragment,))
   cursor.execute("UPDATE Reforging SET Price = ? WHERE NAME = '파괴석'", (DS,))
   cursor.execute("UPDATE Reforging SET Price = ? WHERE NAME = '파괴석 결정'", (DS_crystals,))
   cursor.execute("UPDATE Reforging SET Price = ? WHERE NAME = '파괴강석'", (DS_adamant,))
   cursor.execute("UPDATE Reforging SET Price = ? WHERE NAME = '수호석 조각'", (GS_Fragment,))
   cursor.execute("UPDATE Reforging SET Price = ? WHERE NAME = '수호석'", (GS,))
   cursor.execute("UPDATE Reforging SET Price = ? WHERE NAME = '수호석 결정'", (GS_crystals,))
   cursor.execute("UPDATE Reforging SET Price = ? WHERE NAME = '수호강석'", (GS_adamant,))
   cursor.execute("UPDATE Reforging SET Price = ? WHERE NAME = '조화의 파편 주머니(소)'", (SHarmony,))
   cursor.execute("UPDATE Reforging SET Price = ? WHERE NAME = '생명의 파편 주머니(소)'", (SLife,))
   cursor.execute("UPDATE Reforging SET Price = ? WHERE NAME = '명예의 파편 주머니(소)'", (SHonor,))
   cursor.execute("UPDATE Reforging SET Price = ? WHERE NAME = '하급 오레하 융화 재료'", (Low_Ounion,))
   cursor.execute("UPDATE Reforging SET Price = ? WHERE NAME = '조화의 파편 주머니(중)'", (MHarmony,))
   cursor.execute("UPDATE Reforging SET Price = ? WHERE NAME = '생명의 파편 주머니(중)'", (MLife,))
   cursor.execute("UPDATE Reforging SET Price = ? WHERE NAME = '명예의 파편 주머니(중)'", (MHonor,))
   cursor.execute("UPDATE Reforging SET Price = ? WHERE NAME = '중급 오레하 융화 재료'", (Mid_Ounion,))
   cursor.execute("UPDATE Reforging SET Price = ? WHERE NAME = '칼다르 융화 재료'", (Kunion,))
   cursor.execute("UPDATE Reforging SET Price = ? WHERE NAME = '조화의 파편 주머니(대)'", (BHarmony,))
   cursor.execute("UPDATE Reforging SET Price = ? WHERE NAME = '생명의 파편 주머니(대)'", (BLife,))
   cursor.execute("UPDATE Reforging SET Price = ? WHERE NAME = '명예의 파편 주머니(대)'", (BHonor,))
   cursor.execute("UPDATE Reforging SET Price = ? WHERE NAME = '상급 오레하 융화 재료'", (High_Ounion,))
   con.commit()

def ExReforging_Add(driver):
   RAurl = 'https://lostark.game.onstove.com/Market/List_v2?firstCategory=50000' \
           '&secondCategory=50020&characterClass=&tier=0&grade=99%27%20\%20%27&itemName=&pageNo=1&isInit=false&sortType=1&_=1623805762408'

   driver.get(RAurl)
   html = driver.page_source
   soup = BeautifulSoup(html, 'html.parser')

   # 태양의 은총
   Grac_Sun = soup.select_one('#tbodyItemList > tr:nth-child(1) > td:nth-child(4) > div > em')
   Grac_Sun = Function.check(Grac_Sun)

   #아쿠투르스의 서 : 무기
   WArcturusB = soup.select_one('#tbodyItemList > tr:nth-child(2) > td:nth-child(4) > div > em')
   WArcturusB = Function.check(WArcturusB)

   #아쿠투르스의 서 : 방어구
   AArcturusB = soup.select_one('#tbodyItemList > tr:nth-child(3) > td:nth-child(4) > div > em')
   AArcturusB = Function.check(AArcturusB)

   #조화의 돌파석
   Harmony_through = soup.select_one('#tbodyItemList > tr:nth-child(4) > td:nth-child(4) > div > em')
   Harmony_through = Function.check(Harmony_through)

   #생명의 돌파석
   Life_through = soup.select_one('#tbodyItemList > tr:nth-child(5) > td:nth-child(4) > div > em')
   Life_through = Function.check(Life_through)

   #명예의 돌파석
   Honor_through = soup.select_one('#tbodyItemList > tr:nth-child(6) > td:nth-child(4) > div > em')
   Honor_through = Function.check(Honor_through)

   #위대한 명예의 돌파석
   GHonor_through = soup.select_one('#tbodyItemList > tr:nth-child(7) > td:nth-child(4) > div > em')
   GHonor_through = Function.check(GHonor_through)

   #경이로운 명예의 돌파석
   PHonor_through = soup.select_one('#tbodyItemList > tr:nth-child(8) > td:nth-child(4) > div > em')
   PHonor_through = Function.check(PHonor_through)

   #태양의 축복
   Blessing_Sun = soup.select_one('#tbodyItemList > tr:nth-child(9) > td:nth-child(4) > div > em')
   Blessing_Sun = Function.check(Blessing_Sun)

   #크라테르의 서 : 무기
   WkratherB = soup.select_one('#tbodyItemList > tr:nth-child(10) > td:nth-child(4) > div > em')
   WkratherB = Function.check(WkratherB)

   #2page
   RAurl = 'https://lostark.game.onstove.com/Market/List_v2?firstCategory=50000' \
           '&secondCategory=50020&characterClass=&tier=0&grade=99%27%20\%20%27&itemName=&pageNo=2&isInit=false&sortType=1&_=1623805762408'

   driver.get(RAurl)
   html = driver.page_source
   soup = BeautifulSoup(html, 'html.parser')

   #크라테르의 서 : 방어구
   AkratherB = soup.select_one('#tbodyItemList > tr:nth-child(1) > td:nth-child(4) > div > em')
   AkratherB = Function.check(AkratherB)

   #아크투르스의 의지 : 무기
   WArcturusW = soup.select_one('#tbodyItemList > tr:nth-child(2) > td:nth-child(4) > div > em')
   WArcturusW = Function.check(WArcturusW)

   #아크투르스의 의지 : 방어구
   AArcturusW = soup.select_one('#tbodyItemList > tr:nth-child(3) > td:nth-child(4) > div > em')
   AArcturusW = Function.check(AArcturusW)

   #야금술 : 주조 기본
   Metallurgical1 = soup.select_one('#tbodyItemList > tr:nth-child(4) > td:nth-child(4) > div > em')
   Metallurgical1 = Function.check(Metallurgical1)

   #재봉술 : 도안 기본
   Sewing1 = soup.select_one('#tbodyItemList > tr:nth-child(5) > td:nth-child(4) > div > em')
   Sewing1 = Function.check(Sewing1)

   #야금술 : 접쇠 기본
   Metallurgical2 = soup.select_one('#tbodyItemList > tr:nth-child(6) > td:nth-child(4) > div > em')
   Metallurgical2 = Function.check(Metallurgical2)

   #재봉술 : 매듭 기본
   Sewing2 = soup.select_one('#tbodyItemList > tr:nth-child(7) > td:nth-child(4) > div > em')
   Sewing2 = Function.check(Sewing2)

   #야금술 : 단조 기본
   Metallurgical3 = soup.select_one('#tbodyItemList > tr:nth-child(8) > td:nth-child(4) > div > em')
   Metallurgical3 = Function.check(Metallurgical3)

   #재봉술 : 수선 기본
   Sewing3 = soup.select_one('#tbodyItemList > tr:nth-child(9) > td:nth-child(4) > div > em')
   Sewing3 = Function.check(Sewing3)

   #별의 숨결
   Breath_Star = soup.select_one('#tbodyItemList > tr:nth-child(10) > td:nth-child(4) > div > em')
   Breath_Star = Function.check(Breath_Star)

   # 3page
   RAurl = 'https://lostark.game.onstove.com/Market/List_v2?firstCategory=50000' \
           '&secondCategory=50020&characterClass=&tier=0&grade=99%27%20\%20%27&itemName=&pageNo=3&isInit=false&sortType=1&_=1623805762408'

   driver.get(RAurl)
   html = driver.page_source
   soup = BeautifulSoup(html, 'html.parser')

   #달의 숨결
   Breath_Moon = soup.select_one('#tbodyItemList > tr:nth-child(1) > td:nth-child(4) > div > em')
   Breath_Moon = Function.check(Breath_Moon)

   #태양의 가호
   protection_Sun = soup.select_one('#tbodyItemList > tr:nth-child(2) > td:nth-child(4) > div > em')
   protection_Sun = Function.check(protection_Sun)

   #크라테르의 지혜 : 무기
   WkratherW = soup.select_one('#tbodyItemList > tr:nth-child(3) > td:nth-child(4) > div > em')
   WkratherW = Function.check(WkratherW)

   #크라테르의 지혜 : 방어구
   AkratherW = soup.select_one('#tbodyItemList > tr:nth-child(4) > td:nth-child(4) > div > em')
   AkratherW = Function.check(AkratherW)

   #야금술 : 단조 응용
   Metallurgical4 = soup.select_one('#tbodyItemList > tr:nth-child(5) > td:nth-child(4) > div > em')
   Metallurgical4 = Function.check(Metallurgical4)

   #재봉술 : 수선 응용
   Sewing4 = soup.select_one('#tbodyItemList > tr:nth-child(6) > td:nth-child(4) > div > em')
   Sewing4 = Function.check(Sewing4)

   #크라테르의 권능 : 무기
   WkratherP = soup.select_one('#tbodyItemList > tr:nth-child(7) > td:nth-child(4) > div > em')
   WkratherP = Function.check(WkratherP)

   #크라테르의 권능 : 방어구
   AkratherP = soup.select_one('#tbodyItemList > tr:nth-child(8) > td:nth-child(4) > div > em')
   AkratherP = Function.check(AkratherP)

   # 야금술 : 접쇠 심화
   Metallurgical5 = soup.select_one('#tbodyItemList > tr:nth-child(9) > td:nth-child(4) > div > em')
   Metallurgical5 = Function.check(Metallurgical5)

   #재봉술 : 매듭 심화
   Sewing5 = soup.select_one('#tbodyItemList > tr:nth-child(10) > td:nth-child(4) > div > em')
   Sewing5 = Function.check(Sewing5)

   #4page
   RAurl = 'https://lostark.game.onstove.com/Market/List_v2?firstCategory=50000' \
           '&secondCategory=50020&characterClass=&tier=0&grade=99%27%20\%20%27&itemName=&pageNo=4&isInit=false&sortType=1&_=1623805762408'

   driver.get(RAurl)
   html = driver.page_source
   soup = BeautifulSoup(html, 'html.parser')

   #야금술 : 단조 심화
   Metallurgical6 = soup.select_one('#tbodyItemList > tr:nth-child(1) > td:nth-child(4) > div > em')
   Metallurgical6 = Function.check(Metallurgical6)

   #재봉술 : 수선 심화
   Sewing6 = soup.select_one('#tbodyItemList > tr:nth-child(2) > td:nth-child(4) > div > em')
   Sewing6 = Function.check(Sewing6)

   cursor.execute("UPDATE Reforging_Add SET Price = ? WHERE NAME = '태양의 은총'", (Grac_Sun,))
   cursor.execute("UPDATE Reforging_Add SET Price = ? WHERE NAME = '아크투르스의 서 : 무기'", (WArcturusB,))
   cursor.execute("UPDATE Reforging_Add SET Price = ? WHERE NAME = '아크투르스의 서 : 방어구'", (AArcturusB,))
   cursor.execute("UPDATE Reforging_Add SET Price = ? WHERE NAME = '조화의 돌파석'", (Harmony_through,))
   cursor.execute("UPDATE Reforging_Add SET Price = ? WHERE NAME = '생명의 돌파석'", (Life_through,))
   cursor.execute("UPDATE Reforging_Add SET Price = ? WHERE NAME = '명예의 돌파석'", (Honor_through,))
   cursor.execute("UPDATE Reforging_Add SET Price = ? WHERE NAME = '위대한 명예의 돌파석'", (GHonor_through,))
   cursor.execute("UPDATE Reforging_Add SET Price = ? WHERE NAME = '경이로운 명예의 돌파석'", (PHonor_through,))
   cursor.execute("UPDATE Reforging_Add SET Price = ? WHERE NAME = '태양의 축복'", (Blessing_Sun,))
   cursor.execute("UPDATE Reforging_Add SET Price = ? WHERE NAME = '크라테르의 서 : 무기'", (WkratherB,))
   cursor.execute("UPDATE Reforging_Add SET Price = ? WHERE NAME = '크라테르의 서 : 방어구'", (AkratherB,))
   cursor.execute("UPDATE Reforging_Add SET Price = ? WHERE NAME = '아크투르스의 의지 : 무기'", (WArcturusW,))
   cursor.execute("UPDATE Reforging_Add SET Price = ? WHERE NAME = '아크투르스의 의지 : 방어구'", (AArcturusW,))
   cursor.execute("UPDATE Reforging_Add SET Price = ? WHERE NAME = '야금술 : 주조 기본'", (Metallurgical1,))
   cursor.execute("UPDATE Reforging_Add SET Price = ? WHERE NAME = '재봉술 : 도안 기본'", (Sewing1,))
   cursor.execute("UPDATE Reforging_Add SET Price = ? WHERE NAME = '야금술 : 접쇠 기본'", (Metallurgical2,))
   cursor.execute("UPDATE Reforging_Add SET Price = ? WHERE NAME = '재봉술 : 매듭 기본'", (Sewing2,))
   cursor.execute("UPDATE Reforging_Add SET Price = ? WHERE NAME = '야금술 : 단조 기본'", (Metallurgical3,))
   cursor.execute("UPDATE Reforging_Add SET Price = ? WHERE NAME = '재봉술 : 수선 기본'", (Sewing3,))
   cursor.execute("UPDATE Reforging_Add SET Price = ? WHERE NAME = '별의 숨결'", (Breath_Star,))
   cursor.execute("UPDATE Reforging_Add SET Price = ? WHERE NAME = '달의 숨결'", (Breath_Moon,))
   cursor.execute("UPDATE Reforging_Add SET Price = ? WHERE NAME = '태양의 가호'", (protection_Sun,))
   cursor.execute("UPDATE Reforging_Add SET Price = ? WHERE NAME = '크라테르의 지혜 : 무기'", (WkratherW,))
   cursor.execute("UPDATE Reforging_Add SET Price = ? WHERE NAME = '크라테르의 지혜 : 방어구'", (AkratherW,))
   cursor.execute("UPDATE Reforging_Add SET Price = ? WHERE NAME = '야금술 : 단조 응용'", (Metallurgical4,))
   cursor.execute("UPDATE Reforging_Add SET Price = ? WHERE NAME = '재봉술 : 수선 응용'", (Sewing4,))
   cursor.execute("UPDATE Reforging_Add SET Price = ? WHERE NAME = '크라테르의 권능 : 무기'", (WkratherP,))
   cursor.execute("UPDATE Reforging_Add SET Price = ? WHERE NAME = '크라테르의 권능 : 방어구'", (AkratherP,))
   cursor.execute("UPDATE Reforging_Add SET Price = ? WHERE NAME = '야금술 : 접쇠 심화'", (Metallurgical5,))
   cursor.execute("UPDATE Reforging_Add SET Price = ? WHERE NAME = '재봉술 : 매듭 심화'", (Sewing5,))
   cursor.execute("UPDATE Reforging_Add SET Price = ? WHERE NAME = '야금술 : 단조 심화'", (Metallurgical6,))
   cursor.execute("UPDATE Reforging_Add SET Price = ? WHERE NAME = '재봉술 : 수선 심화'", (Sewing6,))
   con.commit()

