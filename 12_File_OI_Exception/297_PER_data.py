per = ["10.31", "", "8.00"]
new_per = []

for i in per:
    try :
        data = float(i)
    except :
        data = 0
    new_per.append(data)

print(new_per)