def print_mxn(string, n):
    for i in range(0, len(string), n):
        print(string[i:i+n])


print_mxn("아이엠어보이유알어걸", 3)
