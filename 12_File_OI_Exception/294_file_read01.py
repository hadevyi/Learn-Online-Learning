outfile = open("매수종목1.txt")
row_data = []

for data in outfile :
    row_data.append(data.strip())
print(row_data)
outfile.close()
