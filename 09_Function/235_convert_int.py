def convert_int(data):
    data = data.split(',')
    result = ""
    for detail in data:
        result += detail
    return int(result)


convert_int("1,234,567")
