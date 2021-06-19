fname = input('Enter the file name:  ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened: ', fname)
    quit()

count = 0
for line in fhand:
    if line.startswith('Subject:') :
        count = count + 1
print('There were', count, 'subject lines in', fname)

# There were 27 subject lines in mbox-short.txt와 같이 출력됩니다.
