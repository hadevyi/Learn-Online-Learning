smallest = None
print('Before')
numbers = [9, 41, 12, 3, 74, 15]
for value in numbers :
    if smallest is None :
        smallest = value
    elif value < smallest :
        smallest = value
    print(smallest, value)
print('After', smallest)

# 9 9
# 9 41
# 9 12
# 3 3
# 3 74
# 3 15
# After 3
