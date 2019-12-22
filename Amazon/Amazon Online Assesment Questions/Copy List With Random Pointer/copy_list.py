#  A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.
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
"""
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = None
        self.random = None

def clone_list(head):
    if not head: return None

    #First Pass
    runner = head
    while runner:
        tmp = Node(runner.val, runner.next, None)
        runner.next = tmp
        runner = runner.next.next

    #Second Pass
    runner = head
    while runner:
        if runner.random: runner.next.random = runner.random.next
        runner = runner.next.next

    #Third Pass
    runner1 = head  #For original list
    runner2 = head.next #For clone list
    head2 = head.next

    while runner1:
        runner1.next = runner1.next.next
        runner1 = runner1.next

        if runner2.next != None: runner2.next = runner1.next
        runner2 = runner2.next

    return head2