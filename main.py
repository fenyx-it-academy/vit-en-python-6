# This is third assignment
# This is main module

import utilities

try:
    x = input("Please enter a number: ")

    if utilities.isprime(x):
        print("{} is a prime number.".format(x))
    else:
        print("{} is not a prime number.".format(x))

    factorial = utilities.factorial(x)
    print("The factorial of {} is {}.".format(x, factorial))

    fibonacci = utilities.fibonacci(x)
    print("The fibonacci of {} is {}.".format(x, fibonacci))
except:
    print("<<<***Unfortunately, a unexpected ERROR occurred***>>>")

