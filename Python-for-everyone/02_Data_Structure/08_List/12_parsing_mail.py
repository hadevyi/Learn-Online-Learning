filename = open('mbox-short.txt')

for lines in filename :
    line = lines.rstrip()
    wds = line.split()
    # guardian in a compound statemnet
    if len(wds) < 3 or wds[0] != 'From' :   # order check (short circuit evaluaion)
        continue
    print(wds[2])
