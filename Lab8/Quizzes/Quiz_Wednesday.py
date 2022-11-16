import unittest
# Note that today's Quiz will be a bit different than usual

# Firstly, you will be completing this individually (no communication)
# Secondly, this will be closed-book (other than the official Python documentation)
# Thirdly, please only make changes where the comments indicate, on this file itself
# Finally, to get full marks, you must complete all 7/7 tasks

# Your first task is to create a function called find_highest_value that finds the highest value of some input list of floats L and returns its index
# TODO: Complete find_highest_value


# Your second task will be to create a function called remove_all_ees that takes in a string s and returns the string with all instances of the substring 'ee' removed (don't remove single 'e's)
# TODO: complete remove_all_ees


# Your third task will be to create a function called find_smallest_div that takes in two nonempty lists of integers and returns the indices of the two (one from each list) that, when divided, give the smallest quotient. Return as a tuple.
# TODO: complete find_smallest_div


# Your fourth task will be to create a recursive function rec_add that takes in a list of integers L and if there is one element returns it plus 2, else it returns the value of the last integer in the list plus rec_add of the list minus that element
# TODO: complete rec_add


class QuizTestCases(unittest.TestCase): # Your fifth task will be to complete all unittests here.
    def test_1_find_highest_value_normal(self): # An example for you...
        self.assertEqual(find_highest_value([4, 5, 3, 3, 0, -3]), 1)

    def test_2_remove_all_ees(self): # Create a test case for the remove_all_ees function
        pass

    def test_3_find_smallest_div(self): # Create TWO test cases for the find_smallest_div function
        pass
    def test_4_find_smallest_div_negative(self): # ... hint: consider lists with negative values (for the find_smallest_div function)
        pass

    def test_5_rec_add(self): # Create a test case for the rec_add function
        pass
    
if __name__ == "__main__":
    print("Running quiz")
    

    # Your sixth last task is to create some string, call the remove_all_ees function on that string such that it permanently changes the string, then print that edited string
    # TODO: do the above

    # Your final task will be to call the find_highest_value function on a list, such that it returns the value 4. You pick the list so that this is the case.
    # TODO: do the above

    unittest.main(exit=True)
