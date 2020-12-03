import unittest
from sll import print_list, make_list, SLLNode
from merge_lists import merge_lists

class TestMergeTwoSLL(unittest.TestCase):
    def test_none_lists(self):
        self.assertEqual(print_list(merge_lists(None, None)), [])

    def test_l1_none(self):
        l1 = make_list([])
        l2 = make_list([-2, 2, 3])
        self.assertEqual(print_list(merge_lists(l1, l2)), [-2, 2, 3])
    
    def test_l2_none(self):
        l1 = make_list([-1, 2, 6])
        l2 = make_list([])
        self.assertEqual(print_list(merge_lists(l1, l2)), [-1, 2, 6])

    def test_merge_lists(self):
        l1 = make_list([-1, 2, 6])
        l2 = make_list([-2, 2, 3])
        self.assertEqual(print_list(merge_lists(l1, l2)), [-2, -1, 2, 2, 3, 6])

if __name__ == '__main__': unittest.main()