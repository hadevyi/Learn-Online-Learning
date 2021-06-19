found = False
print('Before', found)
numbers = [9, 41, 12, 3, 74, 15]
for value in numbers :
    if value == 3 :
        found = True
        print(found, value)
        break # 특정 값을 찾았을때 해당 루프를 종료하는 것이 더욱 적절해 보입니다.
print('After', found)

# Before False
# True 3
# After True
