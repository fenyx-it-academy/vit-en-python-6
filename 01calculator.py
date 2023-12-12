# This is first assignment
# This is a simple calculator

import operations01

msgwelcome = """ Welcome to de simpel calculator!
If you want adding twee number please Enter between twee number + !
If you want subtracting twee number please Enter between twee number - !
If you want multiplying twee number please Enter between twee number * !
If you want divide twee number please Enter between twee number / !
For end of the calculate you must enter = !"""

print(msgwelcome)

operation = ""
while True:
    try:
        firstnum = float(input("Please enter first number: "))
    except:
        print("!!!You must enter just a NUMERIC amount not else!!!")
    else:
        break
condition = True
while condition:
    try:
        operation = input("Please enter operation: ")
    except:
        print("You entered a wrong operation!\nPlease enter a operation as + - * or /")
    else:
        if operation == '+':
            while True:
                try:
                    nextnum = float(input("Please enter next number: "))
                except:
                    print("!!!You must enter just a NUMERIC amount not else!!!")
                else:
                    break
            totalnum = operations01.add(firstnum, nextnum)
            print("{} + {} = {}".format(firstnum, nextnum, totalnum))
            firstnum = totalnum
        elif operation == '-':
            while True:
                try:
                    nextnum = float(input("Please enter next number: "))
                except:
                    print("!!!You must enter just a NUMERIC amount not else!!!")
                else:
                    break
            totalnum = operations01.substract(firstnum, nextnum)
            print("{} - {} = {}".format(firstnum, nextnum, totalnum))
            firstnum = totalnum
        elif operation == '*':
            while True:
                try:
                    nextnum = float(input("Please enter next number: "))
                except:
                    print("!!!You must enter just a NUMERIC amount not else!!!")
                else:
                    break
            totalnum = operations01.multiply(firstnum, nextnum)
            print("{} * {} = {}".format(firstnum, nextnum, totalnum))
            firstnum = totalnum
        elif operation == '/':
            while True:
                try:
                    nextnum = float(input("Please enter next number: "))
                except:
                    print("!!!You must enter just a NUMERIC amount not else!!!")
                else:
                    break
            if nextnum == 0.0:
                print("<<<*** FATAL ERROR ***>>>\nDivide by zero is not valid!")
            else:
                totalnum = operations01.divide(firstnum, nextnum)
                print("{} / {} = {}".format(firstnum, nextnum, totalnum))
                firstnum = totalnum
        else:
            if operation == '=':
                condition = False
            else:
                print("de operation is not valid!\nYou must enter a valid operation as <<< + - * / >>>")

print("Total is <<< {} >>>".format(totalnum))