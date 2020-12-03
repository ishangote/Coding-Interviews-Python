import unittest
from sll import print_list, make_list
from palindrome_sll import is_palindrome

class TestPalindromeSinglyLinkedList(unittest.TestCase):
    def test_edge(self):
        self.assertEqual(is_palindrome(None), True)
        ll = make_list([1])
        self.assertEqual(is_palindrome(ll), True)

    def test_generic(self):
        ll = make_list([1, 2, 2, 1])
        self.assertEqual(is_palindrome(ll), True)

        ll = make_list([1, 2, 3, 2, 1])
        self.assertEqual(is_palindrome(ll), True)

        ll = make_list([1, 2, 1, 2])
        self.assertEqual(is_palindrome(ll), False)

if __name__ == "__main__": unittest.main()