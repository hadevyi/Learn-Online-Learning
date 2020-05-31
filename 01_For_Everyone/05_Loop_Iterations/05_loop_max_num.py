largest_so_far = -1 # 값을 가지고 있는 변수를 선언해 줍니다. 작은 수로 -1로 선언을 합니다.
print('Before', largest_so_far) # 최초의 값과 루프 이후의 값을 비교하기 위해 print 함수로 현재의 값을 확인 합니다.
numbers = [9, 41, 12, 3, 74, 15] # 강의와는 달리 numbers라는 int를 원소로 가지는 list를 선언하였습니다.
for the_num in numbers :
    if the_num > largest_so_far : # iteration value의 현재의 값(the_num)이 현재 가장 큰 값이 할당 되어 있는 largest_so_far보다 크다면 largest_so_far의 값을 the_num으로 바꿔줍니다.
        largest_so_far = the_num
    print('largest_so_far: ', largest_so_far, 'current number: ',the_num)

print('After', largest_so_far)

# Before -1
# largest_so_far:  9 current number:  9
# largest_so_far:  41 current number:  41
# largest_so_far:  41 current number:  12
# largest_so_far:  41 current number:  3
# largest_so_far:  74 current number:  74
# largest_so_far:  74 current number:  15
# After 74
