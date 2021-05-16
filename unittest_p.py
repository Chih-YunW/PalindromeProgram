import unittest
import palindrome

class testCaseIsPalindrome(unittest.TestCase):
        def test_yes_palindrome(self):
                self.assertEqual(palindrome.is_p("carrac"), True)
        def test_no_palindrome(self):
                self.assertEqual(palindrome.is_p("dog"), False)
        def test_edge_caseself(self):
                self.assertEqual(palindrome.is_p("d"), True)

if __name__ == '__main__':
        unittest.main()
