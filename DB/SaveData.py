import sqlite3
import Function


class Reinforce:
    def ExReforging(driver,db):
        con = sqlite3.connect(db)
        cursor = con.cursor()
        Rurl = 'https://lostark.game.onstove.com/Market/List_v2?firstCategory=50000&secondCategory=50010&' \
               'characterClass=&tier=0&grade=99%27%20\%20%27&itemName=&pageNo=1&isInit=false&sortType=1&_=1623805762408'
        driver.get(Rurl)

        Item_name = driver.find_elements_by_css_selector('#tbodyItemList > tr > td:nth-child(1) > div > span.name')
        Item_price = driver.find_elements_by_css_selector('#tbodyItemList > tr > td:nth-child(4) > div > em')

        for i in range(len(Item_name)):
            Item_price[i] = Function.check(Item_price[i].text)
            cursor.execute("UPDATE Reforging SET Price = ? WHERE NAME = ?", (Item_price[i],Item_name[i].text,))

        # 2page
        Rurl = 'https://lostark.game.onstove.com/Market/List_v2?firstCategory=50000&secondCategory=50010' \
               '&characterClass=&tier=0&grade=99%27%20\%20%27&itemName=&pageNo=2&isInit=false&sortType=1&_=1623805762408'

        driver.get(Rurl)

        Item_name = driver.find_elements_by_css_selector('#tbodyItemList > tr > td:nth-child(1) > div > span.name')
        Item_price = driver.find_elements_by_css_selector('#tbodyItemList > tr > td:nth-child(4) > div > em')

        for i in range(len(Item_name)):
            Item_price[i] = Function.check(Item_price[i].text)
            cursor.execute("UPDATE Reforging SET Price = ? WHERE NAME = ?", (Item_price[i], Item_name[i].text,))

        # 3page
        Rurl = 'https://lostark.game.onstove.com/Market/List_v2?firstCategory=50000&secondCategory=50010' \
               '&characterClass=&tier=0&grade=99%27%20\%20%27&itemName=&pageNo=3&isInit=false&sortType=1&_=1623805762408'

        driver.get(Rurl)

        Item_name = driver.find_elements_by_css_selector('#tbodyItemList > tr > td:nth-child(1) > div > span.name')
        Item_price = driver.find_elements_by_css_selector('#tbodyItemList > tr > td:nth-child(4) > div > em')

        for i in range(len(Item_name)):
            Item_price[i] = Function.check(Item_price[i].text)
            cursor.execute("UPDATE Reforging SET Price = ? WHERE NAME = ?", (Item_price[i], Item_name[i].text,))
        con.commit()

    def ExReforging_Add(driver,db):
        con = sqlite3.connect(db)
        cursor = con.cursor()
        RAurl = 'https://lostark.game.onstove.com/Market/List_v2?firstCategory=50000' \
                '&secondCategory=50020&characterClass=&tier=0&grade=99%27%20\%20%27&itemName=&pageNo=1&isInit=false&sortType=1&_=1623805762408'

        driver.get(RAurl)
        Item_name = driver.find_elements_by_css_selector('#tbodyItemList > tr > td:nth-child(1) > div > span.name')
        Item_price = driver.find_elements_by_css_selector('#tbodyItemList > tr > td:nth-child(4) > div > em')

        for i in range(len(Item_name)):
            Item_price[i] = Function.check(Item_price[i].text)
            cursor.execute("UPDATE Reforging_Add SET Price = ? WHERE NAME = ?", (Item_price[i], Item_name[i].text,))

        # 2page
        RAurl = 'https://lostark.game.onstove.com/Market/List_v2?firstCategory=50000' \
                '&secondCategory=50020&characterClass=&tier=0&grade=99%27%20\%20%27&itemName=&pageNo=2&isInit=false&sortType=1&_=1623805762408'

        driver.get(RAurl)
        Item_name = driver.find_elements_by_css_selector('#tbodyItemList > tr > td:nth-child(1) > div > span.name')
        Item_price = driver.find_elements_by_css_selector('#tbodyItemList > tr > td:nth-child(4) > div > em')

        for i in range(len(Item_name)):
            Item_price[i] = Function.check(Item_price[i].text)
            cursor.execute("UPDATE Reforging_Add SET Price = ? WHERE NAME = ?", (Item_price[i], Item_name[i].text,))

        # 3page
        RAurl = 'https://lostark.game.onstove.com/Market/List_v2?firstCategory=50000' \
                '&secondCategory=50020&characterClass=&tier=0&grade=99%27%20\%20%27&itemName=&pageNo=3&isInit=false&sortType=1&_=1623805762408'

        driver.get(RAurl)
        Item_name = driver.find_elements_by_css_selector('#tbodyItemList > tr > td:nth-child(1) > div > span.name')
        Item_price = driver.find_elements_by_css_selector('#tbodyItemList > tr > td:nth-child(4) > div > em')

        for i in range(len(Item_name)):
            Item_price[i] = Function.check(Item_price[i].text)
            cursor.execute("UPDATE Reforging_Add SET Price = ? WHERE NAME = ?", (Item_price[i], Item_name[i].text,))

        # 4page
        RAurl = 'https://lostark.game.onstove.com/Market/List_v2?firstCategory=50000' \
                '&secondCategory=50020&characterClass=&tier=0&grade=99%27%20\%20%27&itemName=&pageNo=4&isInit=false&sortType=1&_=1623805762408'

        driver.get(RAurl)
        Item_name = driver.find_elements_by_css_selector('#tbodyItemList > tr > td:nth-child(1) > div > span.name')
        Item_price = driver.find_elements_by_css_selector('#tbodyItemList > tr > td:nth-child(4) > div > em')

        for i in range(len(Item_name)):
            Item_price[i] = Function.check(Item_price[i].text)
            cursor.execute("UPDATE Reforging_Add SET Price = ? WHERE NAME = ?", (Item_price[i], Item_name[i].text,))
        con.commit()
        con.close()

class Battle_Item:
    def ExPotion(driver,db):
        con = sqlite3.connect(db)
        cursor = con.cursor()
        A_url = 'https://lostark.game.onstove.com/Market/List_v2?firstCategory=60000&secondCategory=60200' \
                '&characterClass=&tier=0&grade=99%27%20\%20%27&itemName=&pageNo=1&isInit=false&sortType=1&_=1623805762408'

        driver.get(A_url)
        Item_name = driver.find_elements_by_css_selector('#tbodyItemList > tr > td:nth-child(1) > div > span.name')
        Item_price = driver.find_elements_by_css_selector('#tbodyItemList > tr > td:nth-child(4) > div > em')

        for i in range(len(Item_name)):
            Item_price[i] = Function.check(Item_price[i].text)
            cursor.execute("UPDATE Potion SET Price = ? WHERE NAME = ?", (Item_price[i], Item_name[i].text,))
        con.commit()

    def ExBuff(driver,db):
        con = sqlite3.connect(db)
        cursor = con.cursor()
        B_url = 'https://lostark.game.onstove.com/Market/List_v2?firstCategory=60000&secondCategory=60500' \
                '&characterClass=&tier=0&grade=99%27%20\%20%27&itemName=&pageNo=1&isInit=false&sortType=1&_=1623805762408'

        driver.get(B_url)
        Item_name = driver.find_elements_by_css_selector('#tbodyItemList > tr > td:nth-child(1) > div > span.name')
        Item_price = driver.find_elements_by_css_selector('#tbodyItemList > tr > td:nth-child(4) > div > em')

        for i in range(len(Item_name)):
            Item_price[i] = Function.check(Item_price[i].text)
            cursor.execute("UPDATE Buff SET Price = ? WHERE NAME = ?", (Item_price[i], Item_name[i].text,))
        con.commit()

    def ExAttack(driver,db):
        con = sqlite3.connect(db)
        cursor = con.cursor()
        A_url = 'https://lostark.game.onstove.com/Market/List_v2?firstCategory=60000&secondCategory=60300' \
                '&characterClass=&tier=0&grade=99%27%20\%20%27&itemName=&pageNo=1&isInit=false&sortType=1&_=1623805762408'
        driver.get(A_url)
        Item_name = driver.find_elements_by_css_selector('#tbodyItemList > tr > td:nth-child(1) > div > span.name')
        Item_price = driver.find_elements_by_css_selector('#tbodyItemList > tr > td:nth-child(4) > div > em')

        for i in range(len(Item_name)):
            Item_price[i] = Function.check(Item_price[i].text)
            cursor.execute("UPDATE Attack SET Price = ? WHERE NAME = ?", (Item_price[i], Item_name[i].text,))

        # 2page
        A_url = 'https://lostark.game.onstove.com/Market/List_v2?firstCategory=60000&secondCategory=60300' \
                '&characterClass=&tier=0&grade=99%27%20\%20%27&itemName=&pageNo=2&isInit=false&sortType=1&_=1623805762408'
        driver.get(A_url)
        Item_name = driver.find_elements_by_css_selector('#tbodyItemList > tr > td:nth-child(1) > div > span.name')
        Item_price = driver.find_elements_by_css_selector('#tbodyItemList > tr > td:nth-child(4) > div > em')

        for i in range(len(Item_name)):
            Item_price[i] = Function.check(Item_price[i].text)
            cursor.execute("UPDATE Attack SET Price = ? WHERE NAME = ?", (Item_price[i], Item_name[i].text,))

        # 3page
        A_url = 'https://lostark.game.onstove.com/Market/List_v2?firstCategory=60000&secondCategory=60300' \
                '&characterClass=&tier=0&grade=99%27%20\%20%27&itemName=&pageNo=3&isInit=false&sortType=1&_=1623805762408'
        driver.get(A_url)
        Item_name = driver.find_elements_by_css_selector('#tbodyItemList > tr > td:nth-child(1) > div > span.name')
        Item_price = driver.find_elements_by_css_selector('#tbodyItemList > tr > td:nth-child(4) > div > em')

        for i in range(len(Item_name)):
            Item_price[i] = Function.check(Item_price[i].text)
            cursor.execute("UPDATE Attack SET Price = ? WHERE NAME = ?", (Item_price[i], Item_name[i].text,))
        con.commit()

    def ExAssistance(driver,db):
        con = sqlite3.connect(db)
        cursor = con.cursor()
        A_url = 'https://lostark.game.onstove.com/Market/List_v2?firstCategory=60000&secondCategory=60400' \
                '&characterClass=&tier=0&grade=99%27%20\%20%27&itemName=&pageNo=1&isInit=false&sortType=1&_=1623805762408'

        driver.get(A_url)
        Item_name = driver.find_elements_by_css_selector('#tbodyItemList > tr > td:nth-child(1) > div > span.name')
        Item_price = driver.find_elements_by_css_selector('#tbodyItemList > tr > td:nth-child(4) > div > em')

        for i in range(len(Item_name)):
            Item_price[i] = Function.check(Item_price[i].text)
            cursor.execute("UPDATE Assistance SET Price = ? WHERE NAME = ?", (Item_price[i], Item_name[i].text,))

        # page2
        A_url = 'https://lostark.game.onstove.com/Market/List_v2?firstCategory=60000&secondCategory=60400' \
                '&characterClass=&tier=0&grade=99%27%20\%20%27&itemName=&pageNo=2&isInit=false&sortType=1&_=1623805762408'

        driver.get(A_url)
        Item_name = driver.find_elements_by_css_selector('#tbodyItemList > tr > td:nth-child(1) > div > span.name')
        Item_price = driver.find_elements_by_css_selector('#tbodyItemList > tr > td:nth-child(4) > div > em')

        for i in range(len(Item_name)):
            Item_price[i] = Function.check(Item_price[i].text)
            cursor.execute("UPDATE Assistance SET Price = ? WHERE NAME = ?", (Item_price[i], Item_name[i].text,))
        con.commit()
        con.close()


class Life:
    def ExPlant(driver,db):
        con = sqlite3.connect(db)
        cursor = con.cursor()
        Purl = 'https://lostark.game.onstove.com/Market/List_v2?firstCategory=90000' \
               '&secondCategory=90200&characterClass=&tier=0&grade=99&itemName=&pageNo=1&isInit=false&sortType=1&_=1623805762402'

        driver.get(Purl)
        Item_name = driver.find_elements_by_css_selector('#tbodyItemList > tr > td:nth-child(1) > div > span.name')
        Item_price = driver.find_elements_by_css_selector('#tbodyItemList > tr > td:nth-child(4) > div > em')

        for i in range(len(Item_name)):
            Item_price[i] = Function.Life_check(Item_name[i].text,Item_price[i].text)
            cursor.execute("UPDATE Plant SET Price = ? WHERE NAME = ?", (Item_price[i], Item_name[i].text,))
        con.commit()

    def ExLogging(driver,db):
        con = sqlite3.connect(db)
        cursor = con.cursor()
        Lurl = "https://lostark.game.onstove.com/Market/List_v2?firstCategory=90000&secondCategory=90300" \
               "&characterClass=&tier=0&grade=99&itemName=&pageNo=1&isInit=false&sortType=1&_=1623805762403"
        driver.get(Lurl)
        Item_name = driver.find_elements_by_css_selector('#tbodyItemList > tr > td:nth-child(1) > div > span.name')
        Item_price = driver.find_elements_by_css_selector('#tbodyItemList > tr > td:nth-child(4) > div > em')

        for i in range(len(Item_name)):
            Item_price[i] = Function.Life_check(Item_name[i].text,Item_price[i].text)
            cursor.execute("UPDATE Logging SET Price = ? WHERE NAME = ?", (Item_price[i], Item_name[i].text,))
        con.commit()

    def ExMining(driver,db):
        con = sqlite3.connect(db)
        cursor = con.cursor()
        Eurl = "https://lostark.game.onstove.com/Market/List_v2?firstCategory=90000&secondCategory=90400" \
               "&characterClass=&tier=0%27%20\%20%27&grade=99&itemName=&pageNo=1&isInit=false&sortType=1&_=1623805762404"

        driver.get(Eurl)
        Item_name = driver.find_elements_by_css_selector('#tbodyItemList > tr > td:nth-child(1) > div > span.name')
        Item_price = driver.find_elements_by_css_selector('#tbodyItemList > tr > td:nth-child(4) > div > em')

        for i in range(len(Item_name)):
            Item_price[i] = Function.Life_check(Item_name[i].text,Item_price[i].text)
            cursor.execute("UPDATE Mining SET Price = ? WHERE NAME = ?", (Item_price[i], Item_name[i].text,))
        con.commit()

    def ExHunting(driver,db):
        con = sqlite3.connect(db)
        cursor = con.cursor()
        Hurl = "https://lostark.game.onstove.com/Market/List_v2?firstCategory=90000&secondCategory=90500" \
               "&characterClass=&tier=0&grade=99&itemName=&pageNo=1&isInit=false&sortType=1&_=1623805762405"

        driver.get(Hurl)
        Item_name = driver.find_elements_by_css_selector('#tbodyItemList > tr > td:nth-child(1) > div > span.name')
        Item_price = driver.find_elements_by_css_selector('#tbodyItemList > tr > td:nth-child(4) > div > em')

        for i in range(len(Item_name)):
            Item_price[i] = Function.Life_check(Item_name[i].text,Item_price[i].text)
            cursor.execute("UPDATE Hunting SET Price = ? WHERE NAME = ?", (Item_price[i], Item_name[i].text,))
        con.commit()

    def ExFishing(driver,db):
        con = sqlite3.connect(db)
        cursor = con.cursor()
        Furl = "https://lostark.game.onstove.com/Market/List_v2?firstCategory=90000" \
               "&secondCategory=90600&characterClass=&tier=0%27%20\%20%27&grade=99&itemName=&pageNo=1&isInit=false&sortType=1&_=1623805762406%27"

        driver.get(Furl)
        Item_name = driver.find_elements_by_css_selector('#tbodyItemList > tr > td:nth-child(1) > div > span.name')
        Item_price = driver.find_elements_by_css_selector('#tbodyItemList > tr > td:nth-child(4) > div > em')

        for i in range(len(Item_name)):
            Item_price[i] = Function.Life_check(Item_name[i].text,Item_price[i].text)
            cursor.execute("UPDATE Fishing SET Price = ? WHERE NAME = ?", (Item_price[i], Item_name[i].text,))
        con.commit()

    def ExArchaeology(driver,db):
        con = sqlite3.connect(db)
        cursor = con.cursor()
        Aurl = 'https://lostark.game.onstove.com/Market/List_v2?firstCategory=90000&secondCategory=90700&characterClass=&tier=0' \
               '&grade=99&itemName=&pageNo=1&isInit=false&sortType=1&_=1623805762408'

        driver.get(Aurl)
        Item_name = driver.find_elements_by_css_selector('#tbodyItemList > tr > td:nth-child(1) > div > span.name')
        Item_price = driver.find_elements_by_css_selector('#tbodyItemList > tr > td:nth-child(4) > div > em')

        for i in range(len(Item_name)):
            Item_price[i] = Function.Life_check(Item_name[i].text,Item_price[i].text)
            cursor.execute("UPDATE Archaeology SET Price = ? WHERE NAME = ?", (Item_price[i], Item_name[i].text,))
        con.commit()
        con.close()










