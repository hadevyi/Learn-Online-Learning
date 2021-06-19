def computepay(hours, rate) :
    if hours > 40 :
        over_hours = hours - 40
        pay = (hours * rate) + (over_hours * 0.5 * rate)
    else :
        pay = hours * rate

    return pay

hours = input("Enter Hours: ")
rate = input("Enter rate: ")

try :
    hours = float(hours)
    rate = float(rate)
except :
    print("Error. please enter numeric input")
    quit()                                              # program done

result = computepay(hours, rate)
print("Pay:",result)
