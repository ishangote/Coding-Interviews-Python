# Given a linked list, remove the n-th node from the end of list and return its head.
"""
Example:
Given linked list: 1->2->3->4->5, and n = 2.
After removing the second node from the end, the linked list becomes 1->2->3->5.

Approach1: (Two passes)

Remove L - N + 1 element from start by finding L

Appraoch 2: (One Passs)

second pointer at n + 1 steps from first => they have n elements in between them

1 -> 2 -> 3 -> 4 -> 5 -> None
^
               ^


1 -> 2 -> 3 -> 4 -> 5 -> None
               ^
                          ^

NOTE: n will always be valid
"""
class SLLNode:
    def __init__(self, val):
        self.val = val
        self.next = None

#------------------------------------------

def one_pass_remove_nth(head, n):
    if not head: return None
    
    fast = slow = head
    for itr in range(n): fast = fast.next
    
    if not fast: return head.next

    while fast.next:
        fast = fast.next
        slow = slow.next
    
    slow.next = slow.next.next
    return head

#------------------------------------------

def two_pass_remove_nth(head, n):
    if not head: return None
    L, curr = 1, head
    while curr.next: 
        L += 1
        curr = curr.next
    
    if L == n: return head.next
    curr = head

    for itr in range(L - n - 1):
        curr = curr.next
    
    curr.next = curr.next.next

    return head

#------------------------------------------

import unittest
class TestRemoveNthElemnet(unittest.TestCase):
    def print_node_vals(self, node):
        if not node: return []
        ans = []
        while node:
            ans.append(node.val)
            node = node.next
        return ans

    def create_list(self, vals):
        dummy = SLLNode(-999)
        curr = dummy
        for val in vals:
            curr.next = SLLNode(val)
            curr = curr.next
        return dummy.next

#------------------------------------------

    def test_l_equal_to_n(self):

        head = self.create_list([1, 2, 3, 4, 5])

        self.assertEqual(self.print_node_vals(one_pass_remove_nth(head, 5)), [1, 2, 3, 5])
        self.assertEqual(self.print_node_vals(two_pass_remove_nth(head, 5)), [1, 2, 3, 5])

    def test_generic(self):

        head = self.create_list([1, 2, 3, 4, 5])
        head1 = self.create_list([1])
        head2 = self.create_list([1, 2])
        head3 = self.create_list([1, 2, 3])
        head4 = self.create_list([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

        self.assertEqual(self.print_node_vals(one_pass_remove_nth(head, 2)), [1, 2, 3, 5])

        self.assertEqual(self.print_node_vals(one_pass_remove_nth(head2, 2)), [2])
        self.assertEqual(self.print_node_vals(one_pass_remove_nth(head2, 1)), [1])

        self.assertEqual(self.print_node_vals(one_pass_remove_nth(head3, 1)), [1, 2])
        self.assertEqual(self.print_node_vals(one_pass_remove_nth(head1, 1)), [])

        self.assertEqual(self.print_node_vals(two_pass_remove_nth(head, 2)), [1, 2, 3, 5])

        self.assertEqual(self.print_node_vals(two_pass_remove_nth(head2, 2)), [2])
        self.assertEqual(self.print_node_vals(two_pass_remove_nth(head2, 1)), [1])

        self.assertEqual(self.print_node_vals(one_pass_remove_nth(head3, 1)), [1, 2])
        self.assertEqual(self.print_node_vals(two_pass_remove_nth(head1, 1)), [])

        self.assertEqual(self.print_node_vals(one_pass_remove_nth(head4, 10)), [1, 2, 3, 4, 5, 6, 7, 8, 9])

if __name__ == "__main__": unittest.main()