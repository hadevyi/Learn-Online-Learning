def print_value_by_key(data, find):
    # 1 : 처음부터 끝까지 찾아보기
    for key, value in data.items():
        if key == find:
            print(value)

    # 2 : 존재하면 꺼내기
    if find in data.items():
        print(data[find])


my_dict = {"10/26": [100, 130, 100, 100],
           "10/27": [10, 12, 10, 11]}

print_value_by_key(my_dict, "10/26")
