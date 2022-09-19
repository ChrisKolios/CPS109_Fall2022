def my_func(a, b, c, n):
    current_maxnum = a
    if (b > current_maxnum):
        current_maxnum = b
    if (c > current_maxnum):
        current_maxnum = c

    print(current_maxnum)
    print(current_maxnum + n)

    if (a == b and a == c):
        print(a*n)

my_func(1, 2, 3, -7)
my_func(2, 2, 2, 13.5)
my_func(12, 2, 12, 17)

def my_func_bonus(a, b, c, n):
    maxnum = max(a, b, c)
    print("The largest number among the first three variables is", maxnum)
    print("The sum of", maxnum, "and", n, "is", maxnum + n)
    if (a == b and a == c):
        print("The product of", a, "and", n, "is", a*n)

my_func_bonus(2, 2, 2, 13.5)
