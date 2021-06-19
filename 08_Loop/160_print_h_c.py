data = ['intra.h', 'intra.c', 'define.h', 'run.py']

for detail in data:
    if detail.split('.')[1] in ['h', 'c']:
        print(detail)
