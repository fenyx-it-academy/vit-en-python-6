# This is third assignment
# This is an utilities module

# This is a function that calculate if a number of integer prime is or not
def isprime (x):
    counter = 1
    try:
        intnum = int(x)
        while counter < intnum - 1:
            counter += 1
            if intnum == 2:
                return True
            elif (intnum % counter) == 0:
                return False

    except:
        print("<<<***ERROR, the argument of the isprime is a non-numeric data***>>>")
        return False
    return True

# End of de isprime function

# This is a factorial function
def factorial (x):
    fact = 1
    try:
        num = int(x)
        for i in range(1, num+1, 1):
            fact *= i
    except:
        print("<<<***ERROR, the argument of the factorial is a non-numeric data***>>>")

    return fact

# End of the factorial function

# This is a fibonacci function
def fibonacci (x):
    try:
        num = int(x)
        if x == 0:
            return 0
        elif x == 1:
            return 1
        else:
            return fibonacci(num - 2) + fibonacci(num - 1)
    except:
        print("<<<***ERROR, the argument of the fibonacci is a non-numeric data***>>>")
        return 0

# End of the fibonacci
