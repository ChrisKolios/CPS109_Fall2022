def lab1func(a, b, c):
    current_maxnum = a
    if (b > current_maxnum):
        current_maxnum = b
    if (c > current_maxnum):
        current_maxnum = c

    if (current_maxnum % 2 == 0):
        print("Even Steven")
    else:
        print("Odd Todd")
    return current_maxnum

tempvar = lab1func(1, 2, 3)
print(tempvar)

tempvar = lab1func(2, -7, 4)
print(tempvar)

tempvar = lab1func(2, 2, 1)
print(tempvar)

def lab1bonusfunc(a, b, c):
    maxnum = max(a, b, c)
    if (maxnum % 2 == 0):
        print("Even Steven")
    else:
        print("Odd Todd")
    return "The largest variable is " + str(maxnum) + "."

tempvar = lab1bonusfunc(1, 2, 3)
print(tempvar)
