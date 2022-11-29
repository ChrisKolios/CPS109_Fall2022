# Lab 9 crash course (covers (in order - randomness, multi-dimensional arrays, and finally exception handling))
# Please email me @ ckolios@ryerson.ca if you have any questions/comments/concerns

# If we want to use randomness in our Python programs, we must import the random library (which comes default bundled with Python)
import random

# For some of the nested-list work
import itertools

# Note: I'm gonna do things a bit sloppy (all in the main without classes) just for expediency of writing
if __name__ == '__main__':
    print('Running Lab 9 Crash Course')

    # Randomness
    do_random = False
    if (do_random):
        # I'd highly recommend checking out the docs: https://docs.python.org/3/library/random.html
        # Also note that for security purposes the random module should not be used (it is psuedo-random)

        # When using randomness, we first want to set the seed. This defaults to be based on the current time on the system.
        # I won't go into it, but essentially this seed helps us get seemingly random numbers (the fact that we rely on the
        # seed means that we only get psuedo-random numbers). Given the same seed, we will always have the same distribution
        # of random numbers.
        random.seed()
        # You'll notice that if we set the seed to something (e.g. 1), then the below will always evaluate to the same values.

        my_random_number = random.randint(0, 100) # Will choose a random number between 0 and 100
        print(my_random_number)

        my_second_random_number = random.randint(0, 100)
        print(my_second_random_number) # Notice that they are (most likely!) different (and different after each execution)

        my_simulated_dice_roll = random.randint(1, 6) # To simulate a die
        my_simulated_dice_list = [1, 2, 3, 4, 5, 6]
        my_list_simulated_dice_roll = random.choice(my_simulated_dice_list) # Randomly picks from the list (any seq)
        print(my_simulated_dice_roll, my_list_simulated_dice_roll) # The above two are functionally equivalent

        my_list_of_fishes = ["Nemo", "Dory", "Crush", "Marlin", "Bubbles"]
        print(my_list_of_fishes) # Notice maintains order
        random.shuffle(my_list_of_fishes)
        print(my_list_of_fishes) # Notice shuffled (differently depending on run)

        my_list_of_books = ["The Hobbit", "Great Expectations", "The Waste Land", "Northanger Abbey", "Moby Dick"] # Some new list
        # To sample with replacement (i.e. we do not modify our original list, so we can have multiple of the same book selected) we use ranndom.choices()
        # Note that it can be weighted too! (https://docs.python.org/3/library/random.html#random.choices)
        # .choices() is different than .choice() (.choices uses floating point arithmetic for speed so it can introduce bias)
        my_2_random_books = random.choices(my_list_of_books, k=2)
        print(my_2_random_books) # Can even be 2 of the same book!
        my_3_random_books = random.choices(my_list_of_books, k=3)
        print(my_3_random_books)

        # Sometimes we want to sample without replacement (i.e. no duplicates allowed)
        my_2_random_books = random.sample(my_list_of_books, k=2)
        print(my_2_random_books)
        print(my_list_of_books) # Notice that it doesn't modify our existing list, but the selection is valid assuming no replacement

        # For more details see the docs linked at the top. This was just a brief introduction to what the random module is capable of!

    do_nested_lists = False
    if (do_nested_lists):
        # As always, I'd highly recommend checking out this section of the official documentation: https://docs.python.org/3/tutorial/datastructures.html#nested-list-comprehensions

        # I'm not going to dwell on this too much, as it's a minor technical thing that you should be aware of.
        # What if you have a list within a list? So for example a list of grocery lists?

        chris_grocery_list = ["Red Bell Pepper", "Kale", "Chicken Tenders"]
        saghar_grocery_list = ["Apple", "Banana", "Clementine"]
        daniel_grocery_list = ["Durian", "Eggplant", "Figs"]
        everyones_grocery_lists = [chris_grocery_list, saghar_grocery_list, daniel_grocery_list]

        # To get the first list within the list, we just use our regular list access syntax
        first_nested_list = everyones_grocery_lists[0]
        print(first_nested_list) # Chris' list, as expected

        # But what if we want to get the first item in the first list?
        # Now we use this kind of nested list / multi-dimensional array syntax
        first_item_in_first_nested_list = everyones_grocery_lists[0][0]
        print(first_item_in_first_nested_list) # Red Bell Pepper, as expected
        print(everyones_grocery_lists[1][2]) # Clementine, as expected

        # We can even use list comprehension to access elements...
        mixed_list = [element for element in everyones_grocery_lists[0]]
        print(mixed_list) # Chris' list

        mixed_list_2 = [[individual_grocery_list[i] for individual_grocery_list in everyones_grocery_lists] for i in range(3)]
        print(mixed_list_2) # Rows and columns switched (so the first list is the first from each original list, the second is the second from each, and third from third)

        # You can use itertools.zip_longest to swap rows and columns for unevenly-sized lists (see: https://docs.python.org/3/library/itertools.html#itertools.zip_longest)
        everyones_grocery_lists = [["Apple", "Banana", "Cherry"], ["Durian", "Eggplant"], ["Figs", "Grapes", "Huckleberry"]]
        mixed_list_3 = [list(x) for x in itertools.zip_longest(*everyones_grocery_lists)] # Will default fill to None
        print(mixed_list_3)

        # Can then remove all instances of None
        for individual_list in mixed_list_3:
            if (None in individual_list):
                individual_list.remove(None)
        print(mixed_list_3) # And now we have the desired unvevenly-transposed list! (if we want it for some reason)

        # A typical use-case you'll see for nested-lists is matrices, which are just lists of lists of integers
        my_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        print("Full:", my_matrix, "2nd list:", my_matrix[1], "2nd element of 2nd list:", my_matrix[1][1])

    do_exceptions = False
    if (do_exceptions):
        # As always, I'd highly recommend checking out this section of the official documentation: https://docs.python.org/3/tutorial/errors.html
        # Here I'll try to provide a brief crash-course re: exceptions and how they work (with a focus on typical use-cases)

        # Typically dividing by 0 gives an error. Let's use a try/except block to catch this error.
        try: # We will try to run whatever is put in here.
            print("Trying bad division") # Notice that this prints
            x = 1/0 # Illegal operation
            print(x) # Notice that this doesn't print
        except: # When we get an exception of any kind we run this block
            print("An exception has occurred") # We can print, or do whatever here. Typically it is good practice to print/return something.

        # If we want to be more detailed re: what kind of error we're getting, we can use the following syntax
        try:
            print("Trying bad division again")
            y = 1/0
            print(y)
        except Exception as err: # Exception is the wildcard class to catch (most) non-fatal exception
            print(f"Unexpected {err=}, {type(err)=}")
            #raise # We can optionally call raise here, to halt the execution of our program upon encountering an error

        # This third way of doing things is the best practice - 
        # to anticipate certain kinds of errors and proceed depending on this - 
        # and raise an exception if we encounter something unexpected
        try:
            print("Trying bad division finally")
            z = zz/1 # Uncomment to get name error
            #z = 1/0 # Uncomment to get zero division error
            #q = []
            #z = q[1] # Uncomment to get unhandled error
            print(z)
        except NameError as err:
            print("Name Error:", err)
            z = 1
        except ZeroDivisionError as err:
            print("Zero Divison Error:", err)
            z = 2
        except Exception as err:
            print(f"Unexpected {err=}, {type(err)=}")
            raise # Raise the error and halt execution
        print(z) # Notice how this is different depending on which except was hit

        # Let's now see a common use-case: error handling for user input!
        valid_input_entered = False
        while not valid_input_entered: # While the user has not entered valid inputs for division...
            try:
                numerator = int(input("Enter your numerator (int):")) # Try to cast their numerator to an int
                denominator = int(input("Enter your denominator (int):")) # Try to cast their denominator to an int
                division_result = numerator/denominator # Try to divide numerator by denominator
                #division_result = aaa/denominator # Uncomment to see the base exception case
                print("Good inputs!")
            except ValueError as err:
                print("Please enter two integers:", err)
            except ZeroDivisionError as err:
                print("Please ensure your denominator is not 0:", err)
            except Exception as err:
                print(f"Unexpected {err=}, {type(err)=}")
                raise # Break out
            else: # Your else will occur after your try if no exceptions have occurred
                print("The division result is:", division_result)
                valid_input_entered = True

        # Two final (quick) cases
        
        # First is raising a specific exception
        anything_but_five = float(input("Enter any number except 5:"))
        if (anything_but_five == 5.0):
            raise ValueError("I said not to enter 5! >:(")
        else:
            print("Well done friend!")

        # Last is using the finally case
        a = 1
        #b = 0
        b = 1 # Uncomment to see how this works with no exception raised

        try:
            c = a/b
            print(c)
        except ZeroDivisionError as err:
            print("Zero Divison Error:", err)
        finally: # Stuff in the finally will always occur right before the try statement completes (and right before the except completes if there is an exception)
            print("Finally is happening now")
            c = 0 # Mwahaha

        print(c)

        # See: https://docs.python.org/3/tutorial/errors.html#defining-clean-up-actions

    print("Done the Crash Course!")
    # I hope this was helpful! Make sure to check out the official python documentation and your professor's slides for more details!
