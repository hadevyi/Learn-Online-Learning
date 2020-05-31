count = 0 # 평균을 전체 원소의 수로 나누기 위해 total number를 확인합니다.
sum = 0
print('Before', count, sum)
numbers = [9, 41, 12, 3, 74, 15] # 강의와는 달리 numbers라는 int를 원소로 가지는 list를 선언하였습니다.
for value in numbers :
    count = count + 1
    sum = sum + value
    print(count, sum, value)
print('After', count, sum, sum/count)

# Before 0 0
# 1 9 9
# 2 50 41
# 3 62 12
# 4 65 3
# 5 139 74
# 6 154 15
# After 6 154 25.666666666666668
