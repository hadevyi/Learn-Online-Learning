zork = 0
print('Before', zork)
numbers = [9, 41, 12, 3, 74, 15] # 강의와는 달리 numbers라는 int를 원소로 가지는 list를 선언하였습니다.
for thing in numbers :
    zork = zork + thing
    print(zork, thing)
print('After', zork)

# Before 0
# 9 9
# 50 41
# 62 12
# 65 3
# 139 74
# 154 15
# After 154
