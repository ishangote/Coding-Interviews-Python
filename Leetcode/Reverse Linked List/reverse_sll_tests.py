from reverse_sll import reverse_sll
from sll import SLLNode, print_list, make_list
import unittest

class TestReverseLinkedList(unittest.TestCase):
    def test_none(self):
        self.assertEqual(reverse_sll(None), None)
        
    def test_generic_example(self):
        input = make_list([2, 6, 9])
        self.assertEqual(print_list(reverse_sll(input)), [9, 6, 2])

if __name__ == "__main__": unittest.main()