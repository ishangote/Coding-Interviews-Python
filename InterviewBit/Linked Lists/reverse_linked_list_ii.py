"""
Reverse a linked list from position m to n. Do it in-place and in one-pass.

For example:
Given 1->2->3->4->5->NULL, m = 2 and n = 4,
return 1->4->3->2->5->NULL.

Given m, n satisfy the following condition:
1 ≤ m ≤ n ≤ length of list.

              m = 3     n = 5
    1    2    3    4    5    6    7
    5 -> 2 -> 4 -> 1 -> 3 -> 6 -> 2
p   c

              m = 3     n = 5
    1    2    3    4    5    6    7
    5 -> 2 -> 4 -> 1 -> 3 -> 6 -> 2
         p    c
         tail con


              m = 3     n = 5
    1    2    3    4    5    6    7
    5 -> 2 <- 4    1 -> 3 -> 6 -> 2
              p    c
         tail con


              m = 3     n = 5
    1    2    3    4    5    6    7
    5 -> 2 <- 4 <- 1    3 -> 6 -> 2
                   p    c
         tail con
         
              m = 3     n = 5
    1    2    3    4    5    6    7
    5 -> 2 <- 4 <- 1 <- 3    6 -> 2
                        p    c
         tail con        
    
              m = 3     n = 5
    1    2    3    4    5    6    7
    5 -> 2 -> 3 -> 1 -> 4 -> 6 -> 2
                        p    c

"""
class SLLNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class SLL:
    def __init__(self, head):
        self.head = head

    def traverse_sll(self):
        ans = []
        while self.head:
            ans.append(self.head.val)
            self.head = self.head.next
        return ans

def reverse_linked_list_ii(head, m, n):
    if not head: return None
    prev, curr = None, head
    
    while m > 1:
        prev = curr
        curr = curr.next
        m -= 1
        n -= 1
    
    tail, con = curr, prev
    
    while n >= 1:
        tmp = curr.next
        curr.next = prev
        prev = curr
        curr = tmp
        n -= 1
        
    if con: con.next = prev
    else: head = prev
        
    tail.next = curr

    return head

import unittest
class TestReverseLinkListII(unittest.TestCase):
    def init_sll(self):
        head = SLLNode(5)
        head.next = SLLNode(2)
        head.next.next = SLLNode(4)
        head.next.next.next = SLLNode(1)
        head.next.next.next.next = SLLNode(3)
        head.next.next.next.next.next = SLLNode(6)
        head.next.next.next.next.next.next = SLLNode(2)

        return head

    def test_edge(self):
        self.assertEqual(reverse_linked_list_ii(None, 3, 2), None)

    def test_genric(self):
        head = self.init_sll()
        sll = SLL(reverse_linked_list_ii(head, 3, 5))
        head = self.init_sll()
        sll1 = SLL(reverse_linked_list_ii(head, 1, 3))

        self.assertEqual(sll.traverse_sll() ,[5, 2, 3, 1, 4, 6 ,2])
        self.assertEqual(sll1.traverse_sll() ,[4, 2, 5, 1, 3, 6, 2])

if __name__ == "__main__": unittest.main()