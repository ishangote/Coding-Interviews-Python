# Reverse a singly linked list

"""

I: 2 -> 6 -> 9      O: 9 -> 6 -> 2 => 
                    O: 2 <- 6 <- 9
   ^

curr = 2
prev = None
temp_next_node = 6
2 -> prev
prev = 2
curr = 6


curr = 6
prev = 2
temp_next_node = 9
6 -> prev
prev = 6
curr = 9

curr = 9
prev = 6
temp_next_node = None
9 -> prev
prev = 9
curr = None

return prev

"""

import unittest

class SLLNode:
    def __init__(self, data):
        self.data = data
        self.next = None


def reverse_sll(sll_head):

    if sll_head == None: return None
    curr = sll_head
    prev = None
    temp_next_node = None

    while curr:
        temp_next_node = curr.next
        curr.next = prev
        prev = curr
        curr = temp_next_node
    return prev.data


class TestReverseLinkedList(unittest.TestCase):
    def test_none(self):
        self.assertEqual(reverse_sll(None), None)

    def test_single_node(self):
        self.assertEqual(reverse_sll(SLLNode(2)), 2)
        
    def test_generic_example(self):
        a = SLLNode(2)
        b = SLLNode(6)
        c = SLLNode(9)
        a.next = b
        b.next = c
        self.assertEqual(reverse_sll(a), 9)

if __name__ == "__main__": unittest.main()


    

