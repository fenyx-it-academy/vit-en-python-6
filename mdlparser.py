# Begin of separator
def separator(strinput):
    num_maker = 0
    numbers = list([])
    counter = 0
    numbers.append(0)

    for x in strinput:
        try:
            num =  int(x)
        except:
            if x == ',':
                numbers.append(0)
                numbers[counter] += num_maker
                num_maker = 0
                counter += 1
                continue
            else:
                return False
        else:
            num_maker = num_maker * 10 + num

    numbers[counter] += num_maker
    return numbers

# End of separator

# Begin of sum
def sum(a):
    temp = 0
    for x in a:
        temp += x

    return temp

# End of sum

# Begin of average
def average(sum, count):
    return float(sum) / count

# End of average