"""

1 -> 2 -> 3 -> None


1 -> 2 -> 3 -> 4        return 2
     |_________|


"""

class SLL:
    def __init__(self, val):
        self.val = val
        self.next = None

def cycle_start(head):
    slow = fast = head
    while fast and fast.next and fast.next.next:
        slow, fast = slow.next, fast.next.next
        if slow == fast:
            break
    #Do not use if slow != fast test for 1-> None
    if not fast or not fast.next or not fast.next.next: return None

    slow = head
    while slow != fast:
        slow, fast = slow.next, fast.next
    
    return slow

import unittest
class TestCylceStart(unittest.TestCase):
    def test_none_head(self):
        self.assertEqual(cycle_start(None), None)
        self.assertEqual(cycle_start(SLL(1)), None)

    def test_not_a_cycle(self):
        head = SLL(1)
        head.next = SLL(2)
        head.next.next = SLL(3)

        self.assertEqual(cycle_start(head), None)

    def test_cycle_start(self):
        head = SLL(1)
        head.next = SLL(2)
        head.next.next = SLL(3)
        head.next.next.next = SLL(4)
        head.next.next.next = head.next

        self.assertEqual(cycle_start(head), head.next)

if __name__ == '__main__': unittest.main()