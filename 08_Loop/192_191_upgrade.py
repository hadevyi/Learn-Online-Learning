data = [
    [2000,  3050,  2050,  1980],
    [7500,  2050,  2050,  1980],
    [15450, 15050, 15550, 14900]
]

for onedata in data:
    for detail in onedata:
        print(detail*1.00014)
    print("-"*4)
