# Given a singly linked list, group all odd nodes together followed by the even nodes. 
# Please note here we are talking about the node number and not the value in the nodes.
# You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.
"""
Example 1:
Input: 1->2->3->4->5->NULL
Output: 1->3->5->2->4->NULL
Example 2:

Input: 2->1->3->5->6->4->7->NULL
Output: 2->3->6->7->1->5->4->NULL

Note:
The relative order inside both the even and odd groups should remain as it was in the input.
The first node is considered odd, the second node even and so on ...

while head:
    odd.next = head
    even.next = head.next.next
    head = head.next.next
*
1 -> 2 -> 3 -> 4 -> 5 -> NULL
head = 1
odd = dummy1 = SLLNode(-999)
even = dummy2 = SLLNode(-99)

          *
1 -> 2 -> 3 -> 4 -> 5 -> NULL
head = 3
odd = dummy1 = SLLNode(-999) -> 1 -> 3
even = dummy2 = SLLNode(-99) -> 2 -> 4
   
                    *
1 -> 2 -> 3 -> 4 -> 5 -> NULL
head = 5
odd = dummy1 = SLLNode(-999) -> 1 -> 3 -> 5
even = dummy2 = SLLNode(-99) -> 2 -> 4 -> None

1 -> 3 -> 5 - 2 -> 4 -> None
"""

class SLLNode:
    def __init__(self, val):
        self.val = val
        self.next = None

def odd_even_sll(head):
    if not head: return None
    dummy1, dummy2 = SLLNode(-999), SLLNode(-99)
    odd, even = dummy1, dummy2

    while head:
        odd.next = head
        even.next = head.next

        odd = odd.next
        even = even.next
        head = head.next.next if even else None

    odd.next = dummy2.next

    return dummy1.next

import unittest
class TestOddEvenSLL(unittest.TestCase):
    head = SLLNode(1)
    head.next = SLLNode(2)
    head.next.next = SLLNode(3)
    head.next.next.next = SLLNode(4)
    head.next.next.next.next = SLLNode(5)

    def print_nodes(self, head):
        if not head: return []
        ans = []
        while head:
            ans.append(head.val)
            head = head.next
        return ans

    def test_generic(self):
        self.assertEqual(self.print_nodes(odd_even_sll(self.head)), [1, 3, 5, 2, 4])
    
if __name__ == "__main__": unittest.main()