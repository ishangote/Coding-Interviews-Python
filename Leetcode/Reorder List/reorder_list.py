# Given a singly linked list L: L0→L1→…→Ln-1→Ln,
# reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…
# You may not modify the values in the list's nodes, only nodes itself may be changed.
"""
Example 1:
Given 1->2->3->4, reorder it to 1->4->2->3.
Example 2:

Given 1->2->3->4->5, reorder it to 1->5->2->4->3.

1 2 3 4 5

1 2 3
4 5

1 2 3
|/|/
5 4

1. Split list at middle 
2. Reverse second list
3. Merge Lists

"""

class SLLNode:
    def __init__(self, val):
        self.val = val
        self.next = None

def split_list(head):
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    mid = slow.next
    slow.next = None
    return head, mid

def reverse_list(head):
    prev = None
    while head:
        tmp = head.next
        head.next = prev
        prev = head
        head = tmp
    return prev

def merge_lists(l1, l2):
    dummy = SLLNode(-999)
    dummy.next = l1

    tmp1, tmp2 = l1, l2

    while l2:
        tmp1 = tmp1.next
        l1.next = l2
        l1 = tmp1

        tmp2 = tmp2.next
        l2.next = l1
        l2 = tmp2

    return dummy.next

def reorder_list(head):
    if not head: return None

    l1, l2 = split_list(head)
    l2 = reverse_list(l2)

    return merge_lists(l1, l2)

import unittest
class TestReorderList(unittest.TestCase):

    head1 = SLLNode(1)
    head1.next = SLLNode(2)
    head1.next.next = SLLNode(3)
    head1.next.next.next = SLLNode(4)
    head1.next.next.next.next = SLLNode(5)

    head2 = SLLNode(1)
    head2.next = SLLNode(2)
    head2.next.next = SLLNode(3)
    head2.next.next.next = SLLNode(4)

    def print_nodes(self, head):
        if not head: return []
        curr = head
        ans = []
        while curr:
            ans.append(curr.val)
            curr = curr.next
        return ans

    def test_generic(self):
        self.assertEqual(self.print_nodes(reorder_list(self.head1)), [1, 5, 2, 4, 3])
        self.assertEqual(self.print_nodes(reorder_list(self.head2)), [1, 4, 2, 3])

if __name__ == "__main__": unittest.main()