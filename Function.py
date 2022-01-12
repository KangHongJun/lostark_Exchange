
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
        # ','이 포함됐다면 ',' 제거
        if( ',' in value.text):
            value = value.text
            value = value.replace(",","")
            value = int(value)
            return value
        else:
            value = int(value.text)
            return value