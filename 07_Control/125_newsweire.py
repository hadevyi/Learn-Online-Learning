phone = input(">> 휴대전화 번호 입력 : ")
phone = phone.split('-')[0]

if phone == "010" :
    newsweire = "알수없음"
elif phone == "011" :
    newsweire = "SKT"
elif phone == "016" :
    newsweire = "KT"
elif phone == "019" :
    newsweire = "LGU"

print(F"당신은 {newsweire} 사용자입니다.")