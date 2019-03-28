# Copy List with Random Pointer
# A linked list is given such that each node contains an additional 
# random pointer which could point to any node in the list or null.
# You must return the copy of the given head as a reference to the cloned list.


"""

1 -> 2 -> 3 -> 4 -> None
v    v    v    v
3    1    3    2


1 -> 1 -> 2 -> 2 -> 3 -> 3 -> 4 -> 4 -> None
v    v    v    v    v    v    v    v
3         1         3         2


"""

import unittest
class SLLNode:
    def __init__(self):
        self.next = None
        self.random = None

def random_linked_list(ll1):

    if ll1 == None: return None
    
    curr = ll1
    while curr != None:
        temp = SLLNode()
        temp.next = curr.next
        curr.next = temp
        curr = curr.next.next

    curr = ll1
    while curr != None:
        if curr.random: curr.next.random = curr.random.next
        curr = curr.next.next

# 1 -> 1 -> 2 -> 2 -> 3 -> 3 -> 4 -> 4 -> None
# v    v    v    v    v    v    v    v
# 3         1         3         2

    curr = ll1
    ll2 = ll1.next
    curr2 = ll2
    while curr != None:
        curr.next = curr.next.next
        curr = curr.next

        if curr2.next != None: curr2.next = curr.next
        curr2 = curr2.next
    
    return ll2


class TestRandomLinkedList(unittest.TestCase):
    def test_none_input(self):
        self.assertEqual(random_linked_list(None), None)

# Please help me write a unittest case for this problem!

if __name__ == "__main__": unittest.main()