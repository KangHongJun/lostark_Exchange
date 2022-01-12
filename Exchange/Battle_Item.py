from bs4 import BeautifulSoup
import sqlite3
import Function


con = sqlite3.connect("./Battle_Item.db")
cursor = con.cursor()

def ExPotion(driver):
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

def ExBuff(driver):
   B_url = 'https://lostark.game.onstove.com/Market/List_v2?firstCategory=60000&secondCategory=60500' \
           '&characterClass=&tier=0&grade=99%27%20\%20%27&itemName=&pageNo=1&isInit=false&sortType=1&_=1623805762408'

   driver.get(B_url)
   html = driver.page_source
   soup = BeautifulSoup(html, 'html.parser')

   #진군의 깃발
   Flag = soup.select_one('#tbodyItemList > tr:nth-child(1) > td:nth-child(4) > div > em')
   Flag = Function.check(Flag)

   # 보호 물약
   Protection = soup.select_one('#tbodyItemList > tr:nth-child(2) > td:nth-child(4) > div > em')
   Protection = Function.check(Protection)

   # 신속 로브
   Quick = soup.select_one('#tbodyItemList > tr:nth-child(3) > td:nth-child(4) > div > em')
   Quick = Function.check(Quick)

   # 빛나는 보호 물약
   SProtection = soup.select_one('#tbodyItemList > tr:nth-child(4) > td:nth-child(4) > div > em')
   SProtection = Function.check(SProtection)

   # 빛나는 신속 로브
   SQuick = soup.select_one('#tbodyItemList > tr:nth-child(5) > td:nth-child(4) > div > em')
   SQuick = Function.check(SQuick)

   # 각성 물약
   Arousal = soup.select_one('#tbodyItemList > tr:nth-child(6) > td:nth-child(4) > div > em')
   Arousal = Function.check(Arousal)

   # 아드로핀 물약
   Atropine = soup.select_one('#tbodyItemList > tr:nth-child(7) > td:nth-child(4) > div > em')
   Atropine = Function.check(Atropine)

   cursor.execute("UPDATE Buff SET Price = ? WHERE NAME = '진군의 깃발'", (Flag,))
   cursor.execute("UPDATE Buff SET Price = ? WHERE NAME = '보호 물약'", (Protection,))
   cursor.execute("UPDATE Buff SET Price = ? WHERE NAME = '신속 로브'", (Quick,))
   cursor.execute("UPDATE Buff SET Price = ? WHERE NAME = '빛나는 보호 물약'", (SProtection,))
   cursor.execute("UPDATE Buff SET Price = ? WHERE NAME = '빛나는 신속 로브'", (SQuick,))
   cursor.execute("UPDATE Buff SET Price = ? WHERE NAME = '각성 물약'", (Arousal,))
   cursor.execute("UPDATE Buff SET Price = ? WHERE NAME = '아드로핀 물약'", (Atropine,))
   con.commit()


def ExAttack(driver):
   A_url = 'https://lostark.game.onstove.com/Market/List_v2?firstCategory=60000&secondCategory=60300' \
           '&characterClass=&tier=0&grade=99%27%20\%20%27&itemName=&pageNo=1&isInit=false&sortType=1&_=1623805762408'
   driver.get(A_url)
   html = driver.page_source
   soup = BeautifulSoup(html, 'html.parser')

   # page1
   # 섬광 수류탄
   Flash = soup.select_one('#tbodyItemList > tr:nth-child(1) > td:nth-child(4) > div > em')
   Flash = Function.check(Flash)

   # 화염 수류탄
   Flame = soup.select_one('#tbodyItemList > tr:nth-child(2) > td:nth-child(4) > div > em')
   Flame = Function.check(Flame)

   # 냉기 수류탄
   Cold_Air = soup.select_one('#tbodyItemList > tr:nth-child(3) > td:nth-child(4) > div > em')
   Cold_Air = Function.check(Cold_Air)

   # 전기 수류탄
   Electric = soup.select_one('#tbodyItemList > tr:nth-child(4) > td:nth-child(4) > div > em')
   Electric = Function.check(Electric)

   # 암흑 수류탄
   Dark = soup.select_one('#tbodyItemList > tr:nth-child(5) > td:nth-child(4) > div > em')
   Dark = Function.check(Dark)

   # 부식 폭탄
   Corrosion = soup.select_one('#tbodyItemList > tr:nth-child(6) > td:nth-child(4) > div > em')
   Corrosion = Function.check(Corrosion)

   # 천둥 물약
   Thunder = soup.select_one('#tbodyItemList > tr:nth-child(7) > td:nth-child(4) > div > em')
   Thunder = Function.check(Thunder)

   # 회오리 수류탄
   Tornado = soup.select_one('#tbodyItemList > tr:nth-child(8) > td:nth-child(4) > div > em')
   Tornado = Function.check(Tornado)

   # 점토 수류탄
   Clay = soup.select_one('#tbodyItemList > tr:nth-child(9) > td:nth-child(4) > div > em')
   Clay = Function.check(Clay)

   # 수면 폭탄
   Sleeping = soup.select_one('#tbodyItemList > tr:nth-child(10) > td:nth-child(4) > div > em')
   Sleeping = Function.check(Sleeping)

   A_url = 'https://lostark.game.onstove.com/Market/List_v2?firstCategory=60000&secondCategory=60300' \
           '&characterClass=&tier=0&grade=99%27%20\%20%27&itemName=&pageNo=2&isInit=false&sortType=1&_=1623805762408'
   driver.get(A_url)
   html = driver.page_source
   soup = BeautifulSoup(html, 'html.parser')

   # 2page
   # 성스러운 폭탄
   Holy = soup.select_one('#tbodyItemList > tr:nth-child(1) > td:nth-child(4) > div > em')
   Holy = Function.check(Holy)

   # 파괴 폭탄
   Destruction = soup.select_one('#tbodyItemList > tr:nth-child(2) > td:nth-child(4) > div > em')
   Destruction = Function.check(Destruction)

   # 빛나는 섬광 수류탄
   SFlash = soup.select_one('#tbodyItemList > tr:nth-child(3) > td:nth-child(4) > div > em')
   SFlash = Function.check(SFlash)

   # 빛나는 화염 수류탄
   SFlame = soup.select_one('#tbodyItemList > tr:nth-child(4) > td:nth-child(4) > div > em')
   SFlame = Function.check(SFlame)

   # 빛나는 냉기 수류탄
   SCold_Air = soup.select_one('#tbodyItemList > tr:nth-child(5) > td:nth-child(4) > div > em')
   SCold_Air = Function.check(SCold_Air)

   # 빛나는 전기 수류탄
   SElectric = soup.select_one('#tbodyItemList > tr:nth-child(6) > td:nth-child(4) > div > em')
   SElectric = Function.check(SElectric)

   # 빛나는 점토 수류탄
   SClay = soup.select_one('#tbodyItemList > tr:nth-child(7) > td:nth-child(4) > div > em')
   SClay = Function.check(SClay)

   # 빛나는 회오리 수류탄
   STornado = soup.select_one('#tbodyItemList > tr:nth-child(8) > td:nth-child(4) > div > em')
   STornado = Function.check(STornado)

   # 빛나는 암흑 수류탄
   SDark = soup.select_one('#tbodyItemList > tr:nth-child(9) > td:nth-child(4) > div > em')
   SDark = Function.check(SDark)

   # 빛나는 수면 폭탄
   Ssleeping = soup.select_one('#tbodyItemList > tr:nth-child(10) > td:nth-child(4) > div > em')
   Ssleeping = Function.check(Ssleeping)

   A_url = 'https://lostark.game.onstove.com/Market/List_v2?firstCategory=60000&secondCategory=60300' \
           '&characterClass=&tier=0&grade=99%27%20\%20%27&itemName=&pageNo=3&isInit=false&sortType=1&_=1623805762408'
   driver.get(A_url)
   html = driver.page_source
   soup = BeautifulSoup(html, 'html.parser')

   # 3page
   # 빛나는 파괴 폭탄
   SDestruction = soup.select_one('#tbodyItemList > tr:nth-child(1) > td:nth-child(4) > div > em')
   SDestruction = Function.check(SDestruction)

   # 빛나는 부식 폭탄
   SCorrosion = soup.select_one('#tbodyItemList > tr:nth-child(2) > td:nth-child(4) > div > em')
   SCorrosion = Function.check(SCorrosion)

   # 빛나는 성스러운 폭탄
   SHoly = soup.select_one('#tbodyItemList > tr:nth-child(3) > td:nth-child(4) > div > em')
   SHoly = Function.check(SHoly)

   cursor.execute("UPDATE Attack SET Price = ? WHERE NAME = '섬광 수류탄'", (Flash,))
   cursor.execute("UPDATE Attack SET Price = ? WHERE NAME = '화염 수류탄'", (Flame,))
   cursor.execute("UPDATE Attack SET Price = ? WHERE NAME = '냉기 수류탄'", (Cold_Air,))
   cursor.execute("UPDATE Attack SET Price = ? WHERE NAME = '전기 수류탄'", (Electric,))
   cursor.execute("UPDATE Attack SET Price = ? WHERE NAME = '암흑 수류탄'", (Dark,))
   cursor.execute("UPDATE Attack SET Price = ? WHERE NAME = '부식 폭탄'", (Corrosion,))
   cursor.execute("UPDATE Attack SET Price = ? WHERE NAME = '천둥 물약'", (Thunder,))
   cursor.execute("UPDATE Attack SET Price = ? WHERE NAME = '회오리 수류탄'", (Tornado,))
   cursor.execute("UPDATE Attack SET Price = ? WHERE NAME = '점토 수류탄'", (Clay,))
   cursor.execute("UPDATE Attack SET Price = ? WHERE NAME = '수면 폭탄'", (Sleeping,))
   cursor.execute("UPDATE Attack SET Price = ? WHERE NAME = '성스러운 폭탄'", (Holy,))
   cursor.execute("UPDATE Attack SET Price = ? WHERE NAME = '파괴 폭탄'", (Destruction,))
   cursor.execute("UPDATE Attack SET Price = ? WHERE NAME = '빛나는 섬광 수류탄'", (SFlash,))
   cursor.execute("UPDATE Attack SET Price = ? WHERE NAME = '빛나는 화염 수류탄'", (SFlame,))
   cursor.execute("UPDATE Attack SET Price = ? WHERE NAME = '빛나는 냉기 수류탄'", (SCold_Air,))
   cursor.execute("UPDATE Attack SET Price = ? WHERE NAME = '빛나는 전기 수류탄'", (SElectric,))
   cursor.execute("UPDATE Attack SET Price = ? WHERE NAME = '빛나는 점토 수류탄 '", (SClay,))
   cursor.execute("UPDATE Attack SET Price = ? WHERE NAME = '빛나는 회오리 수류탄'", (STornado,))
   cursor.execute("UPDATE Attack SET Price = ? WHERE NAME = '빛나는 암흑 수류탄'", (SDark,))
   cursor.execute("UPDATE Attack SET Price = ? WHERE NAME = '빛나는 수면 폭탄'", (Ssleeping,))
   cursor.execute("UPDATE Attack SET Price = ? WHERE NAME = '빛나는 파괴 폭탄'", (SDestruction,))
   cursor.execute("UPDATE Attack SET Price = ? WHERE NAME = '빛나는 부식 폭탄'", (SCorrosion,))
   cursor.execute("UPDATE Attack SET Price = ? WHERE NAME = '빛나는 성스러운 폭탄'", (SHoly,))


   con.commit()


def ExAssistance(driver):
   A_url = 'https://lostark.game.onstove.com/Market/List_v2?firstCategory=60000&secondCategory=60400' \
           '&characterClass=&tier=0&grade=99%27%20\%20%27&itemName=&pageNo=1&isInit=false&sortType=1&_=1623805762408'

   driver.get(A_url)
   html = driver.page_source
   soup = BeautifulSoup(html, 'html.parser')

   # 신호탄
   Signal_Gun = soup.select_one('#tbodyItemList > tr:nth-child(1) > td:nth-child(4) > div > em')
   Signal_Gun =Function.check(Signal_Gun)

   # 빛나는 신호탄
   SSignal_Gun = soup.select_one('#tbodyItemList > tr:nth-child(2) > td:nth-child(4) > div > em')
   SSignal_Gun =Function.check(SSignal_Gun)

   # 만능 물약
   All_purpose = soup.select_one('#tbodyItemList > tr:nth-child(3) > td:nth-child(4) > div > em')
   All_purpose =Function.check(All_purpose)

   # 도발 허수아비
   Scarecrow = soup.select_one('#tbodyItemList > tr:nth-child(4) > td:nth-child(4) > div > em')
   Scarecrow =Function.check(Scarecrow)

   # 모닥불
   Bonfire = soup.select_one('#tbodyItemList > tr:nth-child(5) > td:nth-child(4) > div > em')
   Bonfire =Function.check(Bonfire)

   # 위장 로브
   Camouflage = soup.select_one('#tbodyItemList > tr:nth-child(6) > td:nth-child(4) > div > em')
   Camouflage =Function.check(Camouflage)

   # 성스러운 부적
   Amulet = soup.select_one('#tbodyItemList > tr:nth-child(7) > td:nth-child(4) > div > em')
   Amulet =Function.check(Amulet)

   # 정비소 이동 포탈 주문서
   Spell = soup.select_one('#tbodyItemList > tr:nth-child(8) > td:nth-child(4) > div > em')
   Spell =Function.check(Spell)

   # 페로몬 폭탄
   Pheromones = soup.select_one('#tbodyItemList > tr:nth-child(9) > td:nth-child(4) > div > em')
   Pheromones =Function.check(Pheromones)

   # 빛나는 만능 물약
   SAll_purpose = soup.select_one('#tbodyItemList > tr:nth-child(10) > td:nth-child(4) > div > em')
   SAll_purpose =Function.check(SAll_purpose)

   #page2
   A_url = 'https://lostark.game.onstove.com/Market/List_v2?firstCategory=60000&secondCategory=60400' \
           '&characterClass=&tier=0&grade=99%27%20\%20%27&itemName=&pageNo=2&isInit=false&sortType=1&_=1623805762408'

   driver.get(A_url)
   html = driver.page_source
   soup = BeautifulSoup(html, 'html.parser')
   # 빛나는 위장 로브
   SCamouflage = soup.select_one('#tbodyItemList > tr:nth-child(1) > td:nth-child(4) > div > em')
   SCamouflage =Function.check(SCamouflage)

   # 빛나는 모닥불
   SBonfire = soup.select_one('#tbodyItemList > tr:nth-child(2) > td:nth-child(4) > div > em')
   SBonfire =Function.check(SBonfire)

   # 빛나는 도발 허수아비
   SScarecrow = soup.select_one('#tbodyItemList > tr:nth-child(3) > td:nth-child(4) > div > em')
   SScarecrow =Function.check(SScarecrow)

   # 빛나는 성스러운 부적
   SAmulet = soup.select_one('#tbodyItemList > tr:nth-child(4) > td:nth-child(4) > div > em')
   SAmulet =Function.check(SAmulet)

   # 은신 로브
   Hiding = soup.select_one('#tbodyItemList > tr:nth-child(5) > td:nth-child(4) > div > em')
   Hiding =Function.check(Hiding)

   # 루테란의 나팔
   Trumpet = soup.select_one('#tbodyItemList > tr:nth-child(6) > td:nth-child(4) > div > em')
   Trumpet =Function.check(Trumpet)

   # 시간 정지 물약
   Static_time = soup.select_one('#tbodyItemList > tr:nth-child(7) > td:nth-child(4) > div > em')
   Static_time =Function.check(Static_time)

   # 빛나는 은신 로브
   SHiding = soup.select_one('#tbodyItemList > tr:nth-child(8) > td:nth-child(4) > div > em')
   SHiding =Function.check(SHiding)

   cursor.execute("UPDATE Assistance SET Price = ? WHERE NAME = '신호탄'", (Signal_Gun,))
   cursor.execute("UPDATE Assistance SET Price = ? WHERE NAME = '빛나는 신호탄'", (SSignal_Gun,))
   cursor.execute("UPDATE Assistance SET Price = ? WHERE NAME = '만능 물약'", (All_purpose,))
   cursor.execute("UPDATE Assistance SET Price = ? WHERE NAME = '도발 허수아비'", (Scarecrow,))
   cursor.execute("UPDATE Assistance SET Price = ? WHERE NAME = '모닥불'", (Bonfire,))
   cursor.execute("UPDATE Assistance SET Price = ? WHERE NAME = '위장 로브'", (Camouflage,))
   cursor.execute("UPDATE Assistance SET Price = ? WHERE NAME = '성스러운 부적'", (Amulet,))
   cursor.execute("UPDATE Assistance SET Price = ? WHERE NAME = '정비소 이동 포탈 주문서'", (Spell,))
   cursor.execute("UPDATE Assistance SET Price = ? WHERE NAME = '페로몬 폭탄'", (Pheromones,))
   cursor.execute("UPDATE Assistance SET Price = ? WHERE NAME = '빛나는 만능 물약'", (SAll_purpose,))
   cursor.execute("UPDATE Assistance SET Price = ? WHERE NAME = '빛나는 위장 로브'", (SCamouflage,))
   cursor.execute("UPDATE Assistance SET Price = ? WHERE NAME = '빛나는 모닥불'", (SBonfire,))
   cursor.execute("UPDATE Assistance SET Price = ? WHERE NAME = '빛나는 도발 허수아비'", (SScarecrow,))
   cursor.execute("UPDATE Assistance SET Price = ? WHERE NAME = '빛나는 성스러운 부적'", (SAmulet,))
   cursor.execute("UPDATE Assistance SET Price = ? WHERE NAME = '은신 로브'", (Hiding,))
   cursor.execute("UPDATE Assistance SET Price = ? WHERE NAME = '루테란의 나팔'", (Trumpet,))
   cursor.execute("UPDATE Assistance SET Price = ? WHERE NAME = '시간 정지 물약'", (Static_time,))
   cursor.execute("UPDATE Assistance SET Price = ? WHERE NAME = '빛나는 은신 로브'", (SHiding,))
   con.commit()








