line = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
words = line.split()
print(words[1])
email = words[1]
address = email.split('@')
print(address)              # email address
print(address[1])           # @ subsequent = univ. name
