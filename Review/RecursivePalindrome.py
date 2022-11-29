import unittest
'''
Assume that s is a string. Check to see if s is a palindrome.
If it is, return True. Else, return False. Recall that a
palindrome is a string that is the same string if reversed.

You must use RECURSION to solve the problem.

For example, 
recursive_palindrome('racecar') is True
recursive_palindrome('blue') is False

Three test cases have been included. Add two more,
both of which should be edge cases.
'''
def recursive_palindrome(s) :
    pass

class PalinTests(unittest.TestCase):
    def test1(self):
        self.assertTrue(recursive_palindrome('racecar'))
    def test2(self):
        self.assertFalse(recursive_palindrome('blue'))
    def test3(self):
        self.assertTrue(recursive_palindrome('madam'))

if __name__=='__main__':
    unittest.main(exit=True)
