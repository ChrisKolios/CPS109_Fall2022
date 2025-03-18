# -*- coding: utf-8 -*-
"""
Created on Tue Mar 18 14:03:22 2025

@author: ckoli
"""
import unittest

# Question 2: Number Nom-Nom-Nom

def num_eat_num(current_num_list, num_iters, passable_data=None):
    '''
    Why was 6 afraid of 7? 

    Because 7 8 9! Get it?! Seven 'ate' nine!

    ...

    Well here's the thing: it's a number-eat-number world out there. Survival of the fittest, and all that.

    You're a number-ologist grad student, studying lists of numbers in their natural habitats. 
    You've stumbled upon a miraculous discovery: if a number is exactly 2 less than its neighbour,
    then the smaller one can eat its bigger neighbour! (e.g. 7 eats 9, or 3 eats 5)

    You want to publish this ASAP. Your supervisor tasks you with simulating a number-eat-number environment, using the following rules:
        
    You are given a list of unique numbers as input. 
    Start from the very left of the list in your processing.
    Look at the leftmost number L, and the number directly to its right R.

    If R is greater than L, then R will 'eat' L, UNLESS R is exactly 2 units greater than L, in which case L 'eats' R.
    So for example, [1, 2], or [1, 5] would have 2 or 5 'eat' 1, but [1, 3], or [6, 8], would have 1 'eat' 3, or 6 'eat' 8.
    Vice versa applies for R eating L, so for example [4, 2], would have 2 'eat' 4.

    When a number eats another number, it removes it from the list, but crucially, per your discovery, it also gains
    its 2-unit-greater-edible powers! (Much like the chimera ants in HunterXHunter (peak show don't @ me)).
                                                                            
    So for example, with [1, 3, 5], after one iteration you would have [1, 5] (as 1 eats 3), and after the second you would have
    just [1], (as 1 eats 5, by the powers it got from eating 3).

    But, if you had [1, 3, 4] then after one iteration you get [1, 4] (as 1 eats 3), and after the second you would have
    just [4], (as 4 eats 1).

    Finally, this property is inheritible in its totality. When one number eats another it gains all of its accumulated powers. 
    For example, with [1, 3, 4, 5], you would get [1(3), 4, 5] (where (3) indicates 1 has the 2-greater-eating-power of 3)
    [4 (1, 3), 5]
    [4 (1, 3, 5)]

    In the case of a situation where both numbers can eat eachother
    E.g. [1, 3, 5, 9, 7] -> [1(3), 5, 9, 7] -> [1(3,5), 9, 7] -> [9(1,3,5), 7]
    The leftmost number wins -> [9(1,3,5,7)]

    Given the list, as well as the number of iterations to run (or -1, for until last num standing), simulate 
    this ecological numerical phenomenon!
    Return the final list after the specified number of iterations.
    Note that there is an optional passable_data argument to the function that you can use if you so desire.

    As a final wrench in the question, solve this problem using recursion!
    '''
    
    # Edge cases (or, more accurately, base cases!):

    
    # Get the left and right numbers
    
    
    # Now what we can do is use a data structure such as a dictionary to store the powers of each number (since each number is unique)
    
    
    # Uncomment to see recursive stack
    # print(left_num, right_num, current_num_list, passable_data)
    
    # We now see if L eats R, or vice versa, and handle the dictionary as well
    # What are the cases we might need to deal with?
    
    # Once the eating is complete, call the function recursively with one less iteration, the reduces list, and the updated
    # passable_data dictionary for eating inheritance


class TestNumEatNum(unittest.TestCase):
    
    def test_empty(self): # Empty list should stay empty
        self.assertEqual(num_eat_num([], 0), [])
        self.assertEqual(num_eat_num([], -1), [])
        self.assertEqual(num_eat_num([], 2), [])
    
    def test_one_element(self): # 1 element should remain unchanged
        self.assertEqual(num_eat_num([1], 0), [1])
        self.assertEqual(num_eat_num([1], -1), [1])
        self.assertEqual(num_eat_num([1], 2), [1])
    
    def test_two_elements(self):
        self.assertEqual(num_eat_num([1, 2], 0), [1, 2]) # No iters -> unchanged
        self.assertEqual(num_eat_num([1, 2], -1), [2]) # 2 > 1
        self.assertEqual(num_eat_num([1, 2], 2), [2]) # 2 > 1
        self.assertEqual(num_eat_num([2, 1], -1), [2]) # 2 > 1
        
    def test_two_elements_greater_rule(self):
        self.assertEqual(num_eat_num([1, 3], 0), [1, 3]) # No iters -> unchanged
        self.assertEqual(num_eat_num([1, 3], -1), [1]) # 3-2 = 1
        self.assertEqual(num_eat_num([1, 3], 1), [1]) # 3-2 = 1
        self.assertEqual(num_eat_num([1, 3], 2), [1]) # 3-2 = 1
        self.assertEqual(num_eat_num([3, 1], -1), [1]) # 3-2 = 1
        
    def test_inheritance_property(self):
        self.assertEqual(num_eat_num([1, 3, 5], -1), [1]) # 1 eats then eats
        self.assertEqual(num_eat_num([1, 3, 5], 1), [1, 5]) # 1 eats
        
    def test_small_endnum(self):
        self.assertEqual(num_eat_num([1, 3, 5, 2], -1), [2]) # 1 eats then eats then eaten
        self.assertEqual(num_eat_num([1, 3, 5, 2], 2), [1, 2]) # 1 eats then eats
    
    def test_complex_cases(self):
        self.assertEqual(num_eat_num([1, 3, 5, 4, 2, 7], -1), [2]) # 2 can eat 7 as 5 inherited
        self.assertEqual(num_eat_num([1, 3, 6, 4, 2, 7], -1), [7]) # 2 can't eat 7 as no 5
        self.assertEqual(num_eat_num([1, 3, 5, 9, 7], -1), [9]) # left takes precedence
        self.assertEqual(num_eat_num([1, 3, 5, 7, 9], -1), [1])
        self.assertEqual(num_eat_num([9, 6, 5], -1), [9])
        self.assertEqual(num_eat_num([9, 6, 7], -1), [7])
        
        
if __name__ == "__main__":
    unittest.main(exit=True)
    #print(num_eat_num([1, 3, 5, 4, 2, 7], -1))
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    