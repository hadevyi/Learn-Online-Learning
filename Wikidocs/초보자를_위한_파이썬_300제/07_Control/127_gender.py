num = input("주민등록번호 : ")

if num[7] in ["1", "3"] :
    print("남자")
elif num[7] in ["2", "4"] :
    print("여자")