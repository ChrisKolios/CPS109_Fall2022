import unittest
# Note that today's Quiz will be a bit different than usual

# Firstly, you will be completing this individually (no communication)
# Secondly, this will be closed-book (other than the official Python documentation)
# Thirdly, please only make changes where the comments indicate, on this file itself
# Finally, to get full marks, you must complete all 7/7 tasks

# Your first task is to create a function called find_lowest_value that finds the lowest value of some input list of floats L and returns its index
# TODO: Complete find_lowest_value
def find_lowest_value(L):
    minimum = L[0]
    min_index = 0
    for i in range(1, len(L)):
        if (L[i] < minimum):
            minimum = L[i]
            min_index = i
    return min_index

# Your second task will be to create a function called remove_all_qs that takes in a string s and returns the string with all instances of the letter q removed
def remove_all_qs(s):
    return s.replace("q", "")

# Your third task will be to create a function called find_biggest_mult that takes in two nonempty lists of integers and returns the indices of the two (one from each list) that, when multiplied, give the biggest product. Return as a tuple.
def find_biggest_mult(L, M):
    biggest_mult = L[0] * M[0]
    i_index = 0
    j_index = 0
    for i in range(len(L)):
        for j in range(len(M)):
            if (L[i] * M[j] > biggest_mult):
                biggest_mult = L[i] * M[j]
                i_index = i
                j_index = j
    return (i_index, j_index)


# Your fourth task will be to create a recursive function rec_mul that takes in a list of integers L and if there is one element returns it, else it returns the value of the first integer in the list times rec_mul of the list minus that element
def rec_mul(L):
    if (len(L) == 0): # Base Case 0
        return 0
    elif len(L) == 1: # Base Case 1
        return L[0]
    else: # Recursive Step
        return L[0] * rec_mul(L[1:])


class QuizTestCases(unittest.TestCase): # Your fifth task will be to complete all unittests here.
    def test_1_find_lowest_value_normal(self): # An example for you...
        self.assertEqual(find_lowest_value([4, 5, 3, 3, 0, -3]), 5)

    def test_2_remove_all_qs(self): # Create a test case for the remove_all_qs function
        self.assertEqual(remove_all_qs("quackquack"), "uackuack")

    def test_3_find_biggest_mult(self): # Create TWO test cases for the find_biggest_mult function
        self.assertEqual(find_biggest_mult([1, 3, 2], [3, 2, 1]), (1, 0))
    def test_4_find_biggest_mult_negative(self): # ... hint: consider two lists with negative values
        self.assertEqual(find_biggest_mult([-1, 3, -4], [-3, 2, 1]), (2, 0))

    def test_5_rec_mul(self): # Create a test case for the rec_mul function
        self.assertEqual(rec_mul([3, 2, 1]), 6)
    
if __name__ == "__main__":
    print("Running quiz")
    

    # Your sixth last task is to create some string, call the remove_all_qs function on that string such that it permanently changes the string, then print that edited string
    s = "qquaqck"
    s = remove_all_qs(s)
    print(s)

    # Your final task will be to call the find_lowest_value function on a list, such that it returns the value 3. You pick the list so that this is the case.
    print(find_lowest_value([4, 3, 2, 0, 1]))

    unittest.main(exit=True)
