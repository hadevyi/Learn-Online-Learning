num = input("주민등록번호 : ")

if 0 <= int(num.split('-')[1][1:3]) <= 8 :
    print("서울 입니다.")
else :
    print("서울이 아닙니다.")