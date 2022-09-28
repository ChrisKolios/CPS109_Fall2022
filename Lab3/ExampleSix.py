# In this example we'll go into a bit of extra detail regarding how lists are functioning in the background
# We'll be covering the concept of mutability and immutability, but you don't have to completely know what these are (yet) so don't worry

# There will also be a discussion on memory management, which is beyond the scope of this course (but may prove interesting to you!)
# Do not lose sight of the forest for the trees here. There are two primary takeaways regarding lists which you'll see at the end.

def my_list_editor(input_list):
	if (len(input_list) > 0): # If there is something in the list
		input_list.pop() # Remove the value at the end of the list

def attempt_number_rewrite(input_number):
	input_number = 0

if __name__ == "__main__":
	print("Hello Class") # Hello, class

	# The first thing we should cover is the Python keyword "is"
	x = 3
	y = 3

	print(x == y) # Here we're checking if the value of x is equal to the value of y (i.e. if 3 is equal to 3) which is True
	print(x is y) # When we use the keyword "is", we're checking if, under the hood, Python is storing each object at the same location in memory. This prints True.
	# But x and y are different variables - why would they be stored in the same position in memory? Well, Python is pretty clever, and it does something called "interning"
	# Interning basically means that the actual value of the variable is stored at the location in memory, and for small strings and integers, for efficiency purposes Python
	# only stores one copy of that integer (here 3) in memory, and then x and y both point to that location in memory.

	# You'll notice this is only the case for small integers/strings.
	x = 10**100
	y = 10**100

	print(x == y) # Of course True
	print(x is y) # Now False, as we are not doing interning

	# Please don't get confused by this! Always use == to check for equality! "is" is only for checking memory, which you probably won't do in this course.

	# Anyways, there is a function called id() that gives us the memory address of a variable.

	x = 3
	idx = id(x)
	print(idx)

	y = 3
	idy = id(y)
	print(idy) # You'll notice, due to interning, it is the same id as x

	x = 10**100
	y = 10**100
	idx = id(x)
	idy = id(y)
	print(idx, idy, idx == idy) # You'll notice these are NOT the same, as there is no interning for anything except small strings and integers

	# Basically what "is" is doing is comparing if idx == idy.

	# Now let's move on to why this is important, in the context of lists

	a = [1, 2, 3]
	b = [1, 2, 3]

	print(a == b) # True, as by value they're the same
	print(a is b) # False, as they are located at different places in memory!

	c = a # What if we want to create some new list c with the values of a?
	print(c) # Just [1, 2, 3]
	print(a == c) # True, as by value they're the same
	print(a is c) # True?! The syntax c = a is just setting c to be a copy of a!

	# So what then happens if we edit c? Will a change too?
	c[0] = 3

	print(c)
	print(a) # a has also changed!

	# Here c is not really even a copy of a - it's just a reference to a

	# But that's not a desired behaviour, right? If we want to make a copy of a called c and edit it without modifying the original list a, how might we do that?

	# Two primary ways:
	a = [1, 2, 3]
	c = a[:] # Using this indexing technique, you'll notice that c is not a reference to a - it is now it's own unique list.

	print(a is c) # False! Great!
	c[0] = 3 # Check what happens when we modify the value...
	print(c)
	print(a) # Just as desired, when we modify c we don't change a

	# Here's the second way:
	c = a.copy()
	print(a is c) # False! Great!
	c[0] = 3
	print(c)
	print(a) # Just as desired, when we modify c we don't change a

	# So, the TLDR here is:
	# When you want to create an independent list2 (i.e. an independent copy) of a list list1, you either have to use the syntax:
	# 1. list2 = list1[:]
	# OR
	# 2. list2 = list1.copy()
	
	# There's a bit more to it than this (check out copy.deepcopy() if you're curious), but this is the most important thing.

	# Just a final quick note on passing lists in to functions:
	a = [1, 2, 3]
	my_list_editor(a)
	print(a) # a has now changed, even though we're not passing anything out of the function
	# This is why it can be useful to just return some new list composed of the input list's contents, instead of modifying the input list in-place (to avoid such edits)

	# This doesn't happen with immutable datatypes such as ints/strings
	x = 3
	attempt_number_rewrite(x)
	print(x) # x does not change

	# When we eventually deal with classes, you'll notice that we can modify class attributes within functions and the changes we make will persist.

	# If you want to read up on it a bit more you can check out this well-written Stack Overflow post: https://stackoverflow.com/questions/986006/how-do-i-pass-a-variable-by-reference
	# Again, though, this is beyond the scope of the course. I just wanted to give you a heads-up on why you might get some funky behaviour with lists and functions.


