apart = [[101, 102], [201, 202], [301, 302]]

for item in apart[::-1]:
    for detail in item[::-1]:
        print(detail, "호")
