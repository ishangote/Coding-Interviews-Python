# Given a sorted linked list, delete all duplicates such that each element appear only once.
"""
Example 1:
Input: 1->1->2
Output: 1->2

Example 2:
Input: 1->1->2->3->3
Output: 1->2->3
"""
class SLLNode:
    def __init__(self, val):
        self.val = val
        self.next = None

def remove_duplicates(head):
    curr = head
    while curr and curr.next:
        if curr.val == curr.next.val: curr.next = curr.next.next
        else: curr = curr.next

    return head

import unittest
class TestRemoveDuplicatesii(unittest.TestCase):
    #1->2->3->3->3->4->4->5
    head = SLLNode(1)
    head.next = SLLNode(2)
    head.next.next = SLLNode(3)
    head.next.next.next = SLLNode(3)
    head.next.next.next.next = SLLNode(3)
    head.next.next.next.next.next = SLLNode(4)
    head.next.next.next.next.next.next = SLLNode(4)
    head.next.next.next.next.next.next.next = SLLNode(5)

    dup = SLLNode(1)
    dup.next = SLLNode(1)
    dup.next.next = SLLNode(1)

    def print_node_vals(self, node):
        ans = []
        while node:
            ans.append(node.val)
            node = node.next
        return ans

    def test_invalid_input(self):
        self.assertEqual(self.print_node_vals(remove_duplicates(None)), [])

    def test_all_duplicates(self):
        
        self.assertEqual(self.print_node_vals(remove_duplicates(self.dup)), [1])

    def test_remove_duplicates_generic(self):
        self.assertEqual(self.print_node_vals(remove_duplicates(self.head)), [1, 2, 3, 4, 5])

if __name__ == "__main__": unittest.main()
