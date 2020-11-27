outfile = open("매수종목2.txt", encoding="UTF8")
row_data = {}

for data in outfile :
    temp = data.split()
    row_data[temp[0]] = temp[1]

print(row_data)
outfile.close()
