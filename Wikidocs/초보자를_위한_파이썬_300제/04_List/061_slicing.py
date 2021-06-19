price = ['20180728', 100, 130, 140, 150, 160, 170]

# 1st
for data in price :
    if type(data) != int :
        price.remove(data)

print(price)

# 2nd
price = ['20180728', 100, 130, 140, 150, 160, 170]
print(price[1:])