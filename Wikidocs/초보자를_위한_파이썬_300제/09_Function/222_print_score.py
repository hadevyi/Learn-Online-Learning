def print_score(num_list):
    total = 0
    for num in num_list:
        total += num
    print(total/len(num_list))


print_score([1, 2, 3])
