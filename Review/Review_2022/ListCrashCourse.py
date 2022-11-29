# This example is to show us some common operations we can perform on lists, as well as some common list use cases
# You'll notice that the structure of the program is such that we have our functions up at the top and our 
# if __name__ == "__main__" after. You'll generally want to follow this structure.

def first_list_function(input_list): # Pretty useless function, but serves to show structure
	print(input_list)

def second_list_function(input_list_1, input_list_2): # Same as above re: not being that useful...
	return input_list_1

if __name__ == "__main__":

	print("Hello Class") # Hello!

	my_empty_list = [] # This is the syntax for creating an empty list. We use square brackets here.

	print(my_empty_list) # We can print the list, just like we can print other data structures. 
	# You'll notice we just get empty square brackets here, as there's nothing in the list at the moment.

	my_prepopulated_list = ["Apple", "Banana", "Pear", "Strawberry"] # We can also use the syntax
	# of multiple list elements separated by commas to populate the list as we declare our list variable

	print(my_prepopulated_list) # You'll notice it prints the list with its elements separated by commas

	x = "Melon"
	y = 3

	my_peculiar_list = ["Any kind of string", 1, x, y] # We can also have lists composed of multiple different
	# data types, or even include variables within the list. In your general use case you'll want to keep lists 
	# composed of one type of data (for simplicity's sake)

	print(my_peculiar_list) # As expected - items separated by commas...

	# One of the most useful properties about lists is that they are mutable. This term means that we can modify
	# the data that the list is composed of in-place, without having to overwrite our current variable.

	simple_number_list = [1, 2, 3, 4, 5]

	print(simple_number_list)

	simple_number_list.append(6) # When we want to add something to the end of a list, we use the syntax: listname.append(x)
	# Where listname is the name of your list variable, and x is whatever data you want to add to the end

	print(simple_number_list) # You'll see that we have added 6 to the end of the list
	simple_number_list.append("Cherry")
	print(simple_number_list) # It doesn't matter what kind of data we append

	x = simple_number_list.pop() # If we want to remove the item at the end of the list, we can call listname.pop()
	print(simple_number_list) # We no longer have 'Cherry' in our list
	print(x) # You'll notice that not only does pop remove things from the list, but it also returns whatever it just
	# removed (which we set a variable x to, in case we want the removed item)

	simple_number_list_extension = [7, 8]
	simple_number_list.extend(simple_number_list_extension) # We can use the my_list.extend(new_list) method to add a new_list or some
	# other kind of iterable to an existing list my_list.
	print(simple_number_list) # We've now combined our two lists

	print(len(simple_number_list_extension)) # We can use the syntax: len(list) to get the length of some list (i.e. the # of items in it)

	# What if we want to see what kind of data is at a specific position in the list? In this case, we can use something called indexing.
	# Consider the following list: 
	fruit_list = ["Apple", "Banana", "Cherry"]
	print(len(fruit_list)) # Our length is 3, as there are 3 items in the list. Makes sense.
	# Indexing means that we access data from a list at a certain position.
	print(fruit_list[0]) # To access the first element of a list, we do: listname[0]. Notice the square brackets, and that indices start at 0 (not 1)!
	print(fruit_list[1]) # The second element will be at index 1
	print(fruit_list[2]) # And so on... We can access the object at any position in the list by just calling the list name 
	# and putting the index in square brackets (you can access wherever in whatever order).

	#print(fruit_list[3]) # If we uncomment this we'll get a IndexError: list index out of range. This is because since there are only 3 items in the list
	# our indices go from 0 to 2 (0 - first item, 1 - second item, 2 - third item, 3 - nonexistant hence error)

	fruit_list.insert(2, "Blueberry") # We can use the .insert(x, y) method to insert AT index x some data y to the list.
	print(fruit_list)

	fruit_list.pop(0) # Similarly, we can use the .pop(x) method to remove the item at index x
	print(fruit_list)

	fruit_list[1] = "Boysenberry" # We can also edit the current list by overwriting the value at a certain index with a new value
	print(fruit_list)

	# fruit_list[3] = "Durian" # Again, we can't set a new value outside the range of the list via this syntax (we have to use .append())
	# as there is currently nothing at index 3 so there is nothing to assign "Durian" to.

	first_list_function(fruit_list) # Of course we can pass in lists as arguments to our functions
	my_returned_list = second_list_function(fruit_list, fruit_list) # And similarly our function output can be a list
	print(my_returned_list)

	# Some bonus (useful) syntax:
	print(fruit_list[-1]) # We can also have negative indices, which indicate "from the end" (with -1 being the last element, -2
	# being the second last element, etc...)
	print(fruit_list[-2])

	print(fruit_list[0:2]) # We can also get a certain sublist of the list by using indexing with a colon.
	# The syntax here is: list[start_index:end_index], non-inclusive at the end (you'll notice we do not print "Cherry")
	print(fruit_list[1:2]) # Just the element at index 1 (the second element)
	print(fruit_list[0:0]) # Nothing here (remember - non-inclusive)
	print(fruit_list[1:]) # Not providing either argument means we just go from the start / end respectively to / from the provided argument
	# So here we go from the second element to the end
	print(fruit_list[:]) # The whole thing!

	# Any questions re: lists as a datatype? We will get into loops right after this, which are useful when combined with lists.
