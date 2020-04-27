"""
3 -> 6 -> 8 -> 13 -> 15 -> None
1 -> 8 -> 10-> 13 -> None
"""

import unittest
class SSLNode:
    def __init__(self, data):
        self.data = data
        self.next = None

def merge_lists(l1, l2):
    dummy = SSLNode(-1111)
    curr_tail = dummy
    
    while l1 and l2:
        if l1.data <= l2.data:
            curr_tail.next = l1
            l1 = l1.next
        else:
            curr_tail.next = l2
            l2 = l2.next

        curr_tail = curr_tail.next

    curr_tail.next = l1 if l1 else l2

    if dummy.next:
        return dummy.next.data
    else: return None
    

class TestMergeTwoSLL(unittest.TestCase):
    def test_none_lists(self):
        self.assertEqual(merge_lists(None, None), None)

    def test_l1_none(self):
        l2 = SSLNode(-2)
        l2.next = SSLNode(2)
        l2.next.next = SSLNode(3)
        self.assertEqual(merge_lists(None, l2), -2)
    
    def test_l2_none(self):
        l1 = SSLNode(-1)
        l1.next = SSLNode(2)
        l1.next.next = SSLNode(6)
        self.assertEqual(merge_lists(l1, None), -1)

    def test_merge_lists(self):
        l1 = SSLNode(-1)
        l1.next = SSLNode(2)
        l1.next.next = SSLNode(6)
        l2 = SSLNode(-2)
        l2.next = SSLNode(2)
        l2.next.next = SSLNode(3)

        self.assertEqual(merge_lists(l1, l2), -2)

if __name__ == '__main__': unittest.main()