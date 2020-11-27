data = [i for i in range(10)]

for num in data :
    try :
        result = 1/num
    except ZeroDivisionError :
        print("분모에는 0이 올 수 없습니다.")
    else :
        print(F"{num} :: {result}")