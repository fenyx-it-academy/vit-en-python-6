# This is a Dice simulation program

import random

def dice (x):
    try:
        i = int(x)
        msg = "This is a simulator of a dice with {} sides."
        print(msg.format(x))
        while True:
            command = input("---Please enter \'R\' as Roll or \'S\' as Stop---:")
            if command.lower() == 'r':
                d = random.randint(1, i)
                print("The number of the {} ".format(d))
                continue
            elif command.lower() == 's':
                break
            else:
                print("You entered wrong command.Please try again")
                continue
    except:
        print("There is not any dice with {} sides".format(x))

