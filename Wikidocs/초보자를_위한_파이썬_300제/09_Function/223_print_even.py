def print_even(num_list):
    even_list = []

    for num in num_list:
        if num % 2 == 0:
            even_list.append(num)

    print(even_list)


print_even([1, 3, 2, 10, 12, 11, 15])
