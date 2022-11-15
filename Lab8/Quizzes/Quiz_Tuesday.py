import unittest
# Note that today's Quiz will be a bit different than usual

# Firstly, you will be completing this individually (no communication)
# Secondly, this will be closed-book (other than the official Python documentation)
# Thirdly, please only make changes where the comments indicate, on this file itself
# Finally, to get full marks, you must complete all 7/7 tasks

# Your first task is to create a function called find_lowest_value that finds the lowest value of some input list of floats L and returns its index
# TODO: Complete find_lowest_value


# Your second task will be to create a function called remove_all_qs that takes in a string s and returns the string with all instances of the letter q removed
# TODO: complete remove_all_qs


# Your third task will be to create a function called find_biggest_mult that takes in two nonempty lists of integers and returns the indices of the two numbers that result in the largest product (one from each list) that, when multiplied, give the biggest product. Return as a tuple.
# TODO: complete find_biggest_mult


# Your fourth task will be to create a recursive function rec_mul that takes in a list of integers L and if there is one element returns it, else it returns the value of the first integer in the list times rec_mul of the list minus that element
# TODO: complete rec_mul


class QuizTestCases(unittest.TestCase): # Your fifth task will be to complete all unittests here.
    def test_1_find_lowest_value_normal(self): # An example for you...
        self.assertEqual(find_lowest_value([4, 5, 3, 3, 0, -3]), 5)

    def test_2_remove_all_qs(self): # Create a test case for the remove_all_qs function
        pass

    def test_3_find_biggest_mult(self): # Create TWO test cases for the find_biggest_mult function
        pass
    def test_4_find_biggest_mult_negative(self): # ... hint: consider two lists with negative values
        pass

    def test_5_rec_mul(self): # Create a test case for the rec_mul function
        pass
    
if __name__ == "__main__":
    print("Running quiz")
    

    # Your sixth last task is to create some string, call the remove_all_qs function on that string such that it permanently changes the string, then print that edited string
    # TODO: do the above

    # Your final task will be to call the find_lowest_value function on a list, such that it returns the value 3. You pick the list so that this is the case.
    # TODO: do the above

    unittest.main(exit=True)
