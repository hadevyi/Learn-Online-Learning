import re                               # To Use a Regular Expression

hand = open('box-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('From:', line) :
        print(line)
