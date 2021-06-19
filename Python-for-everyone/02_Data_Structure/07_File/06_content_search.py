fhand = open('mbox-short.txt')
for line in fhand:    
    line = line.rstrip() # 오른쪽 공백 제거
    if line.startswith('From:') :
        print(line)

# 결과값으로 From: 으로 시작되는 문자열이 출력되게 됩니다.
