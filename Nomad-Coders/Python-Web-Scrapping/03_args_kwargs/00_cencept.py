
def plus(a,b) :
    return a + b

print(plus(3, 4))                                 # Do
print(plus(1,1,1,1,11,2,2,2,2,1,1,1,1))           # Don't
print(plus(1,1,2,2,1,3,1,hello=True, aa=True))    # Don't

# We can create function that ▲
# But, plus-function is only 2 positional arguments
# WE NOT USE LIKE print-function
# print(1,1,1,1,1,12,2,2,2,1,1,...) < Do, It is infinite arguments

# Here's how to address these limitations:
def plus(a,b, *args) :
    print(args)         # tuple
    return a + b

print(3, 4)                                         # Do
print(plus(1,1,1,1,11,2,2,2,2,1,1,1,1))             # Do
print(plus(1,1,2,2,1,3,1,hello=True, aa=True))      # Don't

# ALSO, We can infinite keyword-arguments:
def plus(a,b, *args, **kwargs) :
    print(args)         # tuple
    print(kwargs)       # dictionary
    return a + b

print(3, 4)                                         # Do
print(plus(1,1,1,1,11,2,2,2,2,1,1,1,1))             # Do
print(plus(1,1,2,2,1,3,1,hello=True, aa=True))      # Do