
def check(value):
    if value is None:
        value = 0
        return value
    else:
        if( ',' in value.text):
            value = value.text
            value = value.replace(",","")
            value = int(value)
            return value
        else:
            value = int(value.text)
            return value