d = {'b':1, 'a':10, 'c':22}
d.items()                       # dict_items([('b', 1), ('a', 10), ('c', 22)])
sorted(d.items())               # [('a', 10), ('b', 1), ('c', 22)]

for k, v in sorted(d.items()):
    print(k, v)
