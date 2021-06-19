ccc = dict()
ccc['csev'] = 1
ccc['cwen'] = 1
print(ccc)
ccc['cwen'] = ccc['cwen'] + 1
print(ccc)

''' Error : Because ccc is have not 'csev' key
ccc = dict()
print(ccc['csev'])
'''
