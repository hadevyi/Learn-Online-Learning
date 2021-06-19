per = ["10.31", "", "8.00"]

for i in per:
    try :
        print(float(i))
    except :
        print("0")

'''
ValueError: could not convert string to float: 

per의 중간의 아무런 값이 없는 ""이 있기에 이를 출력할 수 없는것이다.
'''