(x, y) = (4, 'fred')
print(y)                        # fred
(a, b) = (99, 98)
print(a)                        # 99

def t() :
    return (10, 20)
x, y = t()
print(x, y)                     # 10 20

# () is recognized as a tuple, even if it is not used.
x, y = 1, 10
print(x, y)                     # 1 10

x, y = y, x
print(x, y)                     # 10 1
