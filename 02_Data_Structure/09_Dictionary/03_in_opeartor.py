'csev' in ccc
# False

# Using 'in'
counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names :
    if name in counts: # if counts existed key, count one-more.
        counts[name] = counts[name] + 1
    else :             # if counts not existed key, count one.
        counts[name] = 1
print(counts)

# Using 'not in' : result is equal 'in'
counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names :
    if name not in counts:
       counts[name] = 1
    else :
        counts[name] = counts[name] + 1
print(counts)
