# This is second assignment
# This is a parser program

import mdlparser as parser

inputstr = input("Please enter your numbers that is separate with , :")

if parser.separator(inputstr):
    sum = parser.sum(parser.separator(inputstr))
    count = len(parser.separator(inputstr))
    average = parser.average(sum, count)
    msg = """<<<<<
    The list of numbers that you entered is:   {}
    The sum of numbers that you entered is:    {}
    The average of numers that you entered is: {}
    >>>>>
    """
    print(msg.format(inputstr, sum, average))
else:
    print("<<<***Unfortunately, you entered a non-numerical data***>>>")
