"""
Approach 1:
h                   t
1 -> 2 -> 3 -> 4 -> 5   k = 2
          ^    nh
          r

               h
1 -> 2 -> 3    4 -> 5
^                   |
|___________________|

"""
class SLL:
    def __init__(self, val):
        self.val = val
        self.next = None

def rotate_sll(head, k):
    if not head or not head.next or k == 0: return head
    
    tail, length = head, 1
    while tail.next:
        tail = tail.next
        length += 1
    
    k %= length
    if k == 0: return head
    
    runner = head
    for itr in range(length - k - 1):
        runner = runner.next
    
    new_head = runner.next
    runner.next = None
    tail.next = head
    head = new_head

    return head

import unittest
class TestRotateSinglyLinkedList(unittest.TestCase):
    def test_rotate_sll_invalid_ip(self):

        self.assertEqual(rotate_sll(None, 4), None)

        head = SLL(1)
        self.assertEqual(rotate_sll(head, 4), head)

        head1 = SLL(1)
        head1.next = SLL(2)
        head1.next.next = SLL(3)
        self.assertEqual(rotate_sll(head1, 0), head1)

    def test_rotate_sll_k_gt_length(self):
        head = SLL(1)
        head.next = SLL(2)
        head.next.next = SLL(3)
        head.next.next.next = SLL(4)
        head.next.next.next.next = SLL(5)

        self.assertEqual(rotate_sll(head, 7).val, 4)
        self.assertEqual(rotate_sll(head, 15), head)

    def test_rotate_sll_generic(self):
        head = SLL(1)
        head.next = SLL(2)
        head.next.next = SLL(3)
        head.next.next.next = SLL(4)
        head.next.next.next.next = SLL(5)

        self.assertEqual(rotate_sll(head, 3).val, 3)

if __name__ == "__main__": unittest.main()