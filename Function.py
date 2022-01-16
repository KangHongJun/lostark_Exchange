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
        if( ',' in value):
            #value = value.text
            value = value.replace(",","")
            value = int(value)
            return value
        else:
            return value

def Life_check(name,value):
    Life_list = ['들꽃','목재','두툼한 생고기','철광석','생선','고고학']
    if value is None:
        value = 0
        return value
    else:
        if name in Life_list:
            value = int(value) / 100
            return value
        else:
            return int(value) / 10