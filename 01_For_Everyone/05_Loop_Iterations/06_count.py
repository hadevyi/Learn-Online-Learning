zork = 0
print('Before', zork)
numbers = [9, 41, 12, 3, 74, 15] # 강의와는 달리 numbers라는 int를 원소로 가지는 list를 선언하였습니다.
for thing in numbers :
    zork = zork + 1
    print(zork, thing)
print('After', zork)

# Before 0
# 1 9
# 2 41
# 3 12
# 4 3
# 5 74
# 6 15
# After 6
