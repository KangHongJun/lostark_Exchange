
def check(value):
    if value is None:
        value = 0
        return value
    else:
        value = int(value.text)
        return value