"""
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.
k is a positive integer and is less than or equal to the length of the linked list. 
If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

Example:
Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5

Note:

Only constant extra memory is allowed.
You may not alter the values in the list's nodes, only nodes itself may be changed.
"""

"""
k = 3

3
^
1   2 -> 3 -> 4 -> 5 -> 6 -> 7
        e
s   
p
    c   
    t


3 -> 2 -> 1    4 -> 5 -> 6 -> 7
          ^
s              tmp

3 -> 2 -> 1 -> 4 -> 5 -> 6 -> 7
               ^
               s

3 -> 2 -> 1 ->  4 -> 5 -> 6 -> 7
                          ^
                s



Reverse Operation:
k = 3 for example:
step 0: a -> b -> c -> (next k-group)

step 1:      b -> c -> (next k-group)
                  a ---^

step 2:           c -> (next k-group)
             b -> a ---^

step 3:                (next k-group)
        c -> b -> a ---^

finish: c -> b -> a -> (next k-group)
"""
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

def reverseNodesInKGroups(head, k):
    dummy = jump = ListNode(0)
    dummy.next = l = r = head
    
    while True:
        count = 0
        while r and count < k:   # use r to locate the range
            r = r.next
            count += 1
        if count == k:  # if size k satisfied, reverse the inner linked list
            pre, cur = r, l
            for _ in range(k):
                cur.next, cur, pre = pre, cur.next, cur  # standard reversing
            jump.next, jump, l = pre, l, r  # connect two k-groups
        else:
            return dummy.next
            
            

                