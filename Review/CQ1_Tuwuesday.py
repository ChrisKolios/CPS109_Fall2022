# -*- coding: utf-8 -*-
"""
Created on Tue Mar 18 12:53:50 2025

@author: ckoli
"""
import unittest

# Question 1: F0R M3, it was a tuwuesday

def transmogrify_string(string_to_transmogrify):
    '''
    hewwo, I am chwis cwinge-l
    4ND 1 4M 4MR-B0T

    and today, we'we going to teach youwu
    4B0UT 5TR1NG C0MPR3H3N510N.

    we both speak with a uwuniquwue diawect
    4ND R3QU1R3 7R4N5L4710N 70 C0NV3R53 W17H Y0U

    uwuntiw youwu sowve this quwuestion
    W3 MU57 5P34K 1N 7H3S3 V01C35.

    Just kidding. Your task is as follows:
    Given an input string, return the transmogrified form of the string, such that the first half
    is uwuified, and the second half is translated into L337 speak.

    To uwuify a string, you must make it all lowercase, turn all "r"s and "l"s into "w"s, and turn all "u"s into "uwu"s
    To translate a string into L337 speak, you must make it all uppercase, turn "A"s into "4"s, "E"s into "3"s, 
        "I"s into "1"s, "O"s into "0"s, "S"s into "5"s, and "T"s into "7"s.
        
    If you reach the end of the first half of the string in the middle of a word, finish it in uwu-form.

    '''
    
    # Comments are for recommended approach...
    
    # Handle edge case at top
    
    # Split the list into 2 halves, one to be uwuified, and one to be turned into leet speak
        
    # Uwuify the first half
            
    # Leet speak the second half
    
    # Add them together, then return

class TestUwuify(unittest.TestCase):
    
    def test_1_word_uwu(self):
        self.assertEqual(transmogrify_string("hello"), "hewwo")
        self.assertEqual(transmogrify_string("sorry"), "sowwy")
        self.assertEqual(transmogrify_string("cute"), "cuwute")
    def test_shakespeare(self):
        self.assertEqual(transmogrify_string("To be or not to be, that is the question"), "to be ow not to be, that 15 7H3 QU35710N") # mid is first t of 'that'
        self.assertEqual(transmogrify_string("To bee or not to bee, that is the question"), "to bee ow not to bee, 7H47 15 7H3 QU35710N") # mid is ,
    def test_true_peak_literature(self):
        self.assertEqual(transmogrify_string("Somebody once told me the world is gonna roll me; I ain't the sharpest tool in the shed"), # mid is 1st l of 'roll'
                         "somebody once towd me the wowwd is gonna woww M3; 1 41N'7 7H3 5H4RP357 700L 1N 7H3 5H3D")
    def test_uwuroboception(self):
        self.assertEqual(transmogrify_string("uwu! nuzzles your PC! H4H4H4 R0b075 RUL3"), 'uwuwuwu! nuwuzzwes youwuw pc! H4H4H4 R0B075 RUL3')
    def test_edge_cases(self):
        self.assertEqual(transmogrify_string(""), "")
        self.assertEqual(transmogrify_string("U"), "uwu")
    

if __name__ == '__main__':
    unittest.main(exit=True)