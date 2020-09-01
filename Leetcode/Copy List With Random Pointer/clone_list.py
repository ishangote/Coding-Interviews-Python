# A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.
# Return a deep copy of the list.

"""
    |----------->
1   2   3   4   5
|_______^       |
    ^___________|


Approach 1: O(n) Time O(n) space
use hashmap to store [original:clone] map
First Pass
hm = {1:1', 2:2', 3:3', 4:4', 5:5'}
Second Pass
connect next pointers and random pointers

Approach 2: O(n) Time O(1) space

First Pass
1   2   3   4   5

1'  2'  3'  4'  5'

Second Pass: Assign random pointers
1   2   3   4   5
| / | / | / | / |
1'  2'  3'  4'  5'

Third Pass (Restore second list)
*
1   2   3   4   5
| / | / | / | / |
1'  2'  3'  4'  5'

--------------------------------------------------

1 -> 2 -> 3 -> 4 -> None
v    v    v    v
3    1    3    2


1 -> 1 -> 2 -> 2 -> 3 -> 3 -> 4 -> 4 -> None
v    v    v    v    v    v    v    v
3         1         3         2


"""
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = None
        self.random = None

# Approach 1:
# Time: O(n) where n is the number of nodes in the linked list
# Space: O(n)
def clone_list1(head):
    if not head: return None
    copy_nodes = {}
    # First Pass:
    cur = head
    while cur:
        copy_nodes[cur] = Node(cur.val, None, None)
        cur = cur.next

    # Second Pass
    cur = head
    while cur:
        copy_nodes[cur].next = copy_nodes[cur.next] if cur.next else None
        copy_nodes[cur].random = copy_nodes[curr.random] if cur.random else None
        cur = cur.next

    return copy_nodes[head]

# Approach 2:
# Time: O(n)
# Space: O(1)
def clone_list(head):
    if not head: return None
        
    # First Pass
    cur = head
    while cur:
        tmp = cur.next
        cur.next = Node(cur.val, tmp, None)
        cur = tmp
        
    # Second Pass
    cur = head
    while cur:
        cur.next.random = cur.random.next if cur.random else None
        cur = cur.next.next
    
    # Third Pass
    cur = head
    copy_head = copy_cur = head.next
    
    while cur:
        cur.next = cur.next.next
        cur = cur.next
        
        copy_cur.next = copy_cur.next.next if copy_cur.next else None
        copy_cur = copy_cur.next
        
    return copy_head

import unittest
class TestRandomLinkedList(unittest.TestCase):
    def test_none_input(self):
        self.assertEqual(random_linked_list(None), None)

# Please help me write a unittest case for this problem!

if __name__ == "__main__": unittest.main()