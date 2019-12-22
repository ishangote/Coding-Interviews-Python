# Given a linked list, swap every two adjacent nodes and return its head.
# You may not modify the values in the list's nodes, only nodes itself may be changed.

"""
Example:
Given 1->2->3->4, you should return the list as 2->1->4->3.


Example:
a b c d e => b a d c e

Approach 1: Iterative

a -> b -> c -> d -> e

new_head = head.next (b)
pre = dummy = SSLNode(-999)

tmp = head.next (b)
h   tmp
a -> b -> c -> d -> e

head.next = temp.next
h   tmp
a    b -> c -> d -> e
|_________^

tmp.next = head
h   tmp
a <- b    c -> d -> e
|_________^

pre.next = temp
pre [DUMMY]
     |
h   tmp
a <- b    c -> d -> e
|_________^

pre = pre.next

    pre
h   tmp
a <- b    c -> d -> e
|_________^

head = head.next
    pre
    tmp   h
a <- b    c -> d -> e
|_________^

Approach 2: Recursive

Base Conditions: if not head or not head.next: return head


"""
class SLLNode:
    def __init__(self, val):
        self.val = val
        self.next = None

#----------------------------------------------

def swap_nodes_iterative(head):
    if not head or not head.next:
        return head
    new_head = head.next 
    pre = SLLNode("DUMMY")
    while head and head.next:
        tmp = head.next
        head.next = tmp.next
        tmp.next = head
        pre.next = tmp
        head = head.next
        pre = tmp.next
    return new_head

#----------------------------------------------

def swap_nodes_recursive(head):
    if not head or not head.next: return head
    new_head = head.next
    head.next = swap_nodes_recursive(new_head.next)
    new_head.next = head
    return new_head

#----------------------------------------------

import unittest
class TestSwapNodesInPairsInSLL(unittest.TestCase):
    def create_list(self, vals):
        dummy = SLLNode(-999)
        curr = dummy
        for val in vals:
            curr.next = SLLNode(val)
            curr = curr.next
        return dummy.next

    def print_list(self, head):
        if not head: return []
        ans = []
        while head:
            ans.append(head.val)
            head = head.next
        return ans

#----------------------------------------------

    def test_basecases(self):
        head = None
        head1 = self.create_list([1])

        self.assertEqual(self.print_list(swap_nodes_iterative(head)), [])
        self.assertEqual(self.print_list(swap_nodes_recursive(head)), [])

        self.assertEqual(self.print_list(swap_nodes_iterative(head1)), [1])
        self.assertEqual(self.print_list(swap_nodes_recursive(head1)), [1])

    def test_generic(self):
        head = self.create_list(['a', 'b', 'c', 'd', 'e'])
        self.assertEqual(self.print_list(swap_nodes_iterative(head)), ['b', 'a', 'd', 'c', 'e'])
        head = self.create_list(['a', 'b', 'c', 'd', 'e'])
        self.assertEqual(self.print_list(swap_nodes_recursive(head)), ['b', 'a', 'd', 'c', 'e'])

        head1 = self.create_list(['a', 'b', 'c', 'd', 'e', 'f'])
        self.assertEqual(self.print_list(swap_nodes_iterative(head1)), ['b', 'a', 'd', 'c', 'f', 'e'])
        head1 = self.create_list(['a', 'b', 'c', 'd', 'e', 'f'])
        self.assertEqual(self.print_list(swap_nodes_recursive(head1)), ['b', 'a', 'd', 'c', 'f', 'e'])

if __name__ == "__main__":unittest.main()