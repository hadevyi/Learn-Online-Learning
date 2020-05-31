hours = float(input("Enter Hours: "))
rate = float(input("Enter rate: "))

if hours > 40 :
    over_hours = hours - 40
    pay = (hours * rate) + (over_hours * 0.5 * rate)
else :
    pay = hours * rate
print("Pay:",pay)
