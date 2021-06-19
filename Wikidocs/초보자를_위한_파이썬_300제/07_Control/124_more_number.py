num = []

for i in range(3) :
    number = int(input(F"input number{i+1} : "))
    num.append(number)

max_num = num[0]

for i in range(3) :
    if max_num < num[i] :
        max_num = num[i]

print(max_num)