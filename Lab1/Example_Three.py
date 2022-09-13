# Here in example three we'll be looking at variables and variable assignment.

# To assign a value to a variable, you can use the syntax: var = value
# Where var is the name of your variable, which can be lots of different things, though there are rules! (Try some variable names out for yourselves! 
# What happens when you use spaces? Underscores?)
# = is the assignment operator
# and value is the value that you're assigning to the variable. Variables can hold lots of different kinds of data (Integers, Floats, Booleans, Strings, Lists, etc...)

# In the below example, we're assigning the value of the variable a to the integer 10, and b to 20.
a = 10
b = 20

print(a)
print(b)
print(a + b)

c = a
a = b
b = c

print(a) # What do you expect here?
print(b) # Here?
print(c) # Here?
