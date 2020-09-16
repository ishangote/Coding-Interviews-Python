"""
Given a linked list, swap every two adjacent nodes and return its head.

You may not modify the values in the list's nodes, only nodes itself may be changed. 

Example:
Given 1->2->3->4, you should return the list as 2->1->4->3.
                                
    dummy -> 2 -> 1 -> 4 -> 3 -> 5
                                 c tmp
                            p

while c is not None and c.next is not None:
    tmp = c.next
    c.next = t.next
    tmp.next = c
    prev.next = tmp
    prev = c
    c = c.next

"""

def swap_pair_nodes(head):
    dummy = prev = ListNode("DUMMY")
    dummy.next = head
    cur = head
    while cur and cur.next:
        tmp = cur.next
        cur.next = tmp.next
        tmp.next = cur
        prev.next = tmp
        prev = cur
        cur = cur.next

    return dummy.next

"""
In            Expected        Actual
None           None           None
1              1                1
1 -> 2         2                2

1 -> 2 -> 3    2 -> 1 -> 3      2


d -> 2 -> 1 -> 3
          p
     t         c

"""