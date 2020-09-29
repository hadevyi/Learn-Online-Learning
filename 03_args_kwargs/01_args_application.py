def plus(*args) :       # We can use LIKE print-function
    result = 0
    for number in args :
        result += number
    return result

print(plus(1,1,1,2,2,1,2,1,3,12,1,1,1,1))