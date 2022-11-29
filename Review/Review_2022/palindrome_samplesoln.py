import unittest
'''
Assume that s is a string. Check to see if s is a palindrome.
If it is, return True. Else, return False. Recall that a
palinedrome is a string that is the same string if reversed.

You must use RECURSION to solve the problem.

For example, 
recursive_palindrome('racecar') is True
recursive_palindrome('blue') is False

Three test caases have been included. Add two more,
both of which should be edge cases.
'''
def recursive_palindrome(s) :
    # BC 1: Empty
    if len(s) == 0:
        return True
    elif len(s) == 1: # BC 2: 1 thing
        print(s, True)
        return True
    else: # 2 or more
        recursive_result = recursive_palindrome(s[1:-1]) # s minus the first and last characters (-1 is non-inclusive, which is why not -2)
        # print(s[0], s[-1], recursive_result) # To ensure things working properly
        return ((s[0] == s[-1]) and recursive_result)

class PalinTests(unittest.TestCase):
    def test1(self):
        self.assertTrue(recursive_palindrome('racecar'))
    def test2(self):
        self.assertFalse(recursive_palindrome('blue'))
    def test3(self):
        self.assertTrue(recursive_palindrome('madam'))
    def test4(self):
        self.assertEqual(recursive_palindrome(''), True)
    def test5(self):
        self.assertEqual(recursive_palindrome('a'), True)
    def test6(self): # For my own sanity
        self.assertEqual(recursive_palindrome('aaabaa'), False)

if __name__=='__main__':
    unittest.main(exit=True)
