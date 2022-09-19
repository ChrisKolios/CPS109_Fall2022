def my_three(a, b, c):
    if (a >= b) and (a >= c):
        print(a)
    elif (b >= a) and (b >= c):
        print(b)
    else:
        print(c)
    
    if (a == b) and (a == c):
        print("There is no standout number")

def my_three_fast(a, b, c):
    print(max(a,b,c))
    if (a == b) and (a == c):
        print("There is no standout number")
    print(a+b+c)

a = 1
b = 2
c = 3
my_three(a,b,c)
my_three_fast(a,b,c)

a = 2
b = 2
c = 2
my_three(a,b,c)
my_three_fast(a,b,c)

a = 2
b = 3
c = 3
my_three(a,b,c)
my_three_fast(a,b,c)
