import unittest
# Note that today's Quiz will be a bit different than usual

# Firstly, you will be completing this individually (no communication)
# Secondly, this will be closed-book (other than the official Python documentation)
# Thirdly, please only make changes where the comments indicate, on this file itself
# Finally, to get full marks, you must complete all 7/7 tasks

# Your first task is to create a function called find_highest_value that finds the highest value of some input list of floats L and returns its index
def find_highest_value(L):
    maximum = L[0]
    max_index = 0
    for i in range(1, len(L)):
        if (L[i] > maximum):
            maximum = L[i]
            max_index = i
    return max_index


# Your second task will be to create a function called remove_all_ees that takes in a string s and returns the string with all instances of the substring 'ee' removed (don't remove single 'e's)
def remove_all_ees(s):
    return s.replace("ee", "")


# Your third task will be to create a function called find_smallest_div that takes in two nonempty lists of integers and returns the indices of the two (one from each list) that, when multiplied, give the smallest quotient. Return as a tuple.
def find_smallest_div(L, M):
    smallest_div = L[0] / M[0]
    i_index = 0
    j_index = 0
    for i in range(len(L)):
        for j in range(len(M)):
            if (L[i] / M[j] < smallest_div):
                smallest_div = L[i] / M[j]
                i_index = i
                j_index = j
            #if (M[j] / L[i] < smallest_div): # Include to test both directions? (not sure if necessary but tired rn). Don't think needed...
            #    smallest_div = M[j] / L[i]
            #    i_index = i
            #    j_index = j
    return (i_index, j_index)


# Your fourth task will be to create a recursive function rec_add that takes in a list of integers L and if there is one element returns it plus 2, else it returns the value of the last integer in the list plus rec_add of the list without that element
def rec_add(L):
    if (len(L) == 0): # Base Case 0
        return 0
    elif len(L) == 1: # Base Case 1
        return L[0] + 2
    else: # Recursive Step
        return L[-1] + rec_add(L[:-1])


class QuizTestCases(unittest.TestCase): # Your fifth task will be to complete all unittests here.
    def test_1_find_highest_value_normal(self): # An example for you...
        self.assertEqual(find_highest_value([4, 5, 3, 3, 0, -3]), 1)

    def test_2_remove_all_ees(self): # Create a test case for the remove_all_ees function
        self.assertEqual(remove_all_ees("ebeeses"), "ebses")

    def test_3_find_smallest_div(self): # Create TWO test cases for the find_smallest_div function
        self.assertEqual(find_smallest_div([1, 3, 2], [3, 2, 1]), (0, 0)) # 1/3?
    def test_4_find_smallest_div_negative(self): # ... hint: consider lists with negative values (for the find_smallest_div function)
        self.assertEqual(find_smallest_div([-1, 3, -4], [-3, 2, 1]), (2, 2)) # -4/1 = -4

    def test_5_red_add(self): # Create a test case for the rec_add function
        self.assertEqual(rec_add([3, 2, 1]), 8)
    
if __name__ == "__main__":
    print("Running quiz")
    

    # Your sixth last task is to create some string, call the remove_all_ees function on that string such that it permanently changes the string, then print that edited string
    s = "peeke"
    s = remove_all_ees(s)
    print(s)

    # Your final task will be to call the find_highest_value function on a list, such that it returns the value 4. You pick the list so that this is the case.
    print(find_highest_value([4, 3, 2, 0, 5]))

    unittest.main(exit=True)
