# Given a sorted linked list, delete all nodes that have duplicate numbers, 
# leaving only distinct numbers from the original list.
"""
Example 1:
Input: 1->2->3->3->4->4->5
Output: 1->2->5
Example 2:

Input: 1->1->1->2->3
Output: 2->3
"""
class SLLNode:
    def __init__(self, val):
        self.val = val
        self.next = None

#---------------------------------------

def remove_duplicates_ii(head):
    if not head: return None
    dummy = SLLNode(-9999)
    dummy.next = head
    lnd = dummy # Latest non-duplicate

    while head and head.next:
        if head.val == head.next.val:
            while head and head.next and head.val == head.next.val:
                head = head.next
            
            head = head.next
            lnd.next = head
        
        else:
            lnd = lnd.next
            head = head.next

    return dummy.next

#---------------------------------------

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
        self.assertEqual(self.print_node_vals(remove_duplicates_ii(None)), [])

    def test_all_duplicates(self):
        
        self.assertEqual(self.print_node_vals(remove_duplicates_ii(self.dup)), [])

    def test_remove_duplicates_generic(self):
        self.assertEqual(self.print_node_vals(remove_duplicates_ii(self.head)), [1, 2, 5])

if __name__ == "__main__": unittest.main()