"""
Questions:
1. Rotate clockwise and circular? -> yes
2. what if k negative? -> no
3. k > len(linked list)? -> Can be
4. Is it sll? -> yes
5. k == 0? -> can be

Examples:
0 -> 1 -> 2 -> None, k = 4
l = 3
k %= l = 1

one roatation =>
2 -> 0 -> 1 -> None

--------------------------

1 -> 2 -> 3 -> 4 -> 5 -> NULL, k = 2
h                    
          nt    
               nh
                    t
          
l = 5 (length)
new tail (nt) = (l - k)th node
detach
"""
class SLL:
    def __init__(self, val):
        self.val = val
        self.next = None

def get_sll_length(head):
    tail, length = head, 1
    
    while tail.next:
        tail = tail.next
        length += 1
    
    return tail, length

def get_new_tail(head, end):
    cur = head
    for itr in range(end):
        cur = cur.next
    return cur

def rotate_sll(head, k):
    if not head or not head.next or k == 0: return head
    
    # Calculate length
    tail, length = get_sll_length(head)
    k %= length
    #To solve test case (4)
    if k == 0: return head
    
    #Find new head
    new_tail = get_new_tail(head, length - k - 1)
    
    #Detach
    new_head = new_tail.next
    new_tail.next = None
    tail.next = head
    
    return new_head       

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