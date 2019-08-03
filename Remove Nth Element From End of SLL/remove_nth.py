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

import unittest
class TestRemoveNthElemnet(unittest.TestCase):
    head = SLLNode(1)
    head.next = SLLNode(2)
    head.next.next = SLLNode(3)
    head.next.next.next = SLLNode(4)
    head.next.next.next.next = SLLNode(5)

    head1 = SLLNode(1)

    head2 = SLLNode(1)
    head2.next = SLLNode(2)

    def print_node_vals(self, node):
        if not node: return []
        ans = []
        while node:
            ans.append(node.val)
            node = node.next
        return ans

    def test_generic(self):
        self.assertEqual(self.print_node_vals(one_pass_remove_nth(self.head, 2)), [1, 2, 3, 5])
        self.assertEqual(self.print_node_vals(one_pass_remove_nth(self.head2, 2)), [2])
        self.assertEqual(self.print_node_vals(one_pass_remove_nth(self.head1, 1)), [])

if __name__ == "__main__": unittest.main()