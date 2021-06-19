warn_investment_list = ["Microsoft", "Google", "Naver", "Kakao", "SAMSUNG", "LG"]

data = input(">> 종목명은? ")

if data in warn_investment_list :
    print("투자 경고 종목입니다.")
else :
    print("투자 경고 종목이 아닙니다.")