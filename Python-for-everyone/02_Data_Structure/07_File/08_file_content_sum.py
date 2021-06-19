filename = open('mbox-short.txt')

for lines in filename :
    line = lines.rstrip()
    print(line.upper())
