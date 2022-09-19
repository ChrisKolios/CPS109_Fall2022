def friday_quiz_func(a, b, c, d): # General approach idea
    maxnum = a
    minnum = a
    if (b > maxnum):
        maxnum = b
    if (b < minnum):
        minnum = b
    if (c > maxnum):
        maxnum = c
    if (c < minnum):
        minnum = c
    if (d > maxnum):
        maxnum = d
    if (d < minnum):
        minnum = d

    print(minnum)
    print(maxnum)
    return minnum + maxnum

friday_quiz_output = friday_quiz_func(2, 1, 4, 3)
print(friday_quiz_output)
friday_quiz_output = friday_quiz_func(2, -2, 2, 2)
print(friday_quiz_output)
friday_quiz_output = friday_quiz_func(3.1, 3.01, 3.001, 3.0001)
print(friday_quiz_output)

def friday_bonus_quiz_func(a, b, c, d): # General bonus approach idea
    maxnum = max(a, b, c, d)
    minnum = min(a, b, c, d)
    print(minnum)
    print(maxnum)
    return "The sum of the minimum and maximum variables is " + str(minnum + maxnum) + "."

friday_bonus_quiz_output = friday_bonus_quiz_func(1, 2, 3, 4)
print(friday_bonus_quiz_output)

def friday_leet_bonus_quiz_func(a, b, c, d): # It's only 2 lines! (using assignment expressions / the walrus operator - new as of Python 3.8+)
    print(minnum:= min(a,b,c,d),"\n"+str(maxnum:= max(a,b,c,d)))
    return "The sum of the minimum and maximum variables is " + str(minnum+maxnum) + "."

friday_leet_bonus_quiz_output = friday_leet_bonus_quiz_func(1, 2, 3, 4)
print(friday_leet_bonus_quiz_output)

def friday_super_leet_bonus_quiz_func(a,b,c,d): # Only 1 line and efficient! (using return)
    return str(minnum:=min(a,b,c,d))+"\n"+str(maxnum:=max(a,b,c,d))+"\n", "The sum of the minimum and maximum variables is " + str(minnum+maxnum) + "."

print("{}{}".format(w := friday_super_leet_bonus_quiz_func(1, 2, 3, 4)[0], x:= friday_super_leet_bonus_quiz_func(1,2,3,4)[1])) # Using assignment expressions
print(*friday_super_leet_bonus_quiz_func(1, 2, 3, 4), sep='') # Alternate approach using the * operator, which expands the contents of some iterable datatype
friday_super_leet_bonus_quiz_output = friday_super_leet_bonus_quiz_func(1, 2, 3, 4)[1]; print(friday_super_leet_bonus_quiz_func(1, 2, 3, 4)[0] + friday_super_leet_bonus_quiz_output) # More boring but technically valid


def friday_super_leet_bonus_quiz_func_v2(a,b,c,d): # Inefficient, but easier to do
    print(str(min(a,b,c,d))+"\n"+str(max(a,b,c,d))+"\nThe sum of the minimum and maximum variables is " + str(min(a,b,c,d)+max(a,b,c,d)) + ".")

friday_super_leet_bonus_quiz_func_v2(1,2,3,4)

def friday_super_leet_bonus_quiz_func_v3(a,b,c,d): # Efficient and one line! (using print)
    print("{}\n{}\nThe sum of the minimum and maximum variables is {}.".format(minnum:= min(a,b,c,d), maxnum:= max(a,b,c,d), sumnum:= minnum+maxnum))

friday_super_leet_bonus_quiz_func_v3(1,2,3,4)
