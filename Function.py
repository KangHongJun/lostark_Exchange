from DB import GetData
from Exchange import Battle_Item, Life, Reinforce

def UpdataDB(driver):
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