x = [9, 8, 7]
x[2] = 6
print(x)                    # [9, 8, 6], list is mutable

x = (9, 8, 7)
x[2] = 6
print(x)                    # TypeError

# Under case, all Error
x = (3, 2, 1)
x.sort()
x.append(5)
x.reverse()

# each dir
 l = list()
 dir(l)

 t = tuple()
 dir(t)
