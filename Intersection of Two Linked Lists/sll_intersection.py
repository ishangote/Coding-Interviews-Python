# Write a program to find the node at which the intersection of two singly linked lists begins.

"""
Approach1:
HashTable -> 


Approach 2:
Two pointers => 

list1 = [4, 1, 8, 6, 5]
         *            
list2 = [0, 2, 3, 8, 6, 5]
         ^
"""

class SLL_Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def sll_intersection_hm(l1, l2):
    hs = set()

    while l1:
        hs.add(l1)
        l1 = l1.next
    
    while l2:
        if l2 in hs: return l2
        else: l2 = l2.next

    return None

def sll_intersection_two_pointers(l1, l2):
    pointer1, pointer2 = l1, l2
    
    while pointer1 != pointer2:
        pointer1 = pointer1.next if pointer1 else l2
        pointer2 = pointer2.next if pointer2 else l1

    return pointer1


import unittest
class TestSLLIntersection(unittest.TestCase):

    def test_l1_l2_none(self):
        l1 = SLL_Node(4)
        l2 = SLL_Node(5)

        self.assertEqual(sll_intersection_hm(None, l2), None)
        self.assertEqual(sll_intersection_hm(l1, None), None)
        self.assertEqual(sll_intersection_hm(None, None), None)

        self.assertEqual(sll_intersection_two_pointers(None, l2), None)
        self.assertEqual(sll_intersection_two_pointers(l1, None), None)
        self.assertEqual(sll_intersection_two_pointers(None, None), None)

    def test_no_intersection(self):
        l1 = SLL_Node(4)
        l1.next = SLL_Node(1)
        l2 = SLL_Node(5)
        l2.next = SLL_Node(0)

        self.assertEqual(sll_intersection_hm(l1, l2), None)
        self.assertEqual(sll_intersection_two_pointers(l1, l2), None)
    
    def test_sll_intersection(self):
        l1 = SLL_Node(4)
        l1.next = SLL_Node(1)
        l1.next.next = SLL_Node(8)
        l1.next.next.next = SLL_Node(4)
        l1.next.next.next.next = SLL_Node(5)

        l2 = SLL_Node(5)
        l2.next = SLL_Node(0)
        l2.next.next = SLL_Node(1)
        l2.next.next.next = l1.next.next
        l2.next.next.next.next = l1.next.next.next
        l2.next.next.next.next.next = l1.next.next.next.next

        self.assertEqual(sll_intersection_hm(l1, l2), l1.next.next)
        self.assertEqual(sll_intersection_two_pointers(l1, l2), l1.next.next)

if __name__ == "__main__": unittest.main()