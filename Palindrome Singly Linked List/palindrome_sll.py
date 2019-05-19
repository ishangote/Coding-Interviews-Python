# Return True if SLL is Palindorm else False => O(n) space

"""

1 -> 2 -> 3 -> 2-> 1 -> null       True
          ^
                   ^

1 -> 2 -> 3 -> 3 -> 2-> 1 -> null     True
               ^
                              ^


1 -> 2 -> 3 -> 1 -> null
^
^
"""
import unittest
class SLLNode:
    def __init__(self, data):
        self.data = data
        self.next = None

def palindrome_sll(sll_head):
    if not sll_head: return None

    stack = []
    slow_pointer = fast_pointer = sll_head

    while fast_pointer != None and fast_pointer.next != None:
        stack.append(slow_pointer.data)
        slow_pointer = slow_pointer.next
        fast_pointer = fast_pointer.next.next  

    #Odd Length SLL Case:
    if fast_pointer: slow_pointer = slow_pointer.next
    
    while slow_pointer != None:
        if slow_pointer.data == stack[-1]: stack.pop()
        slow_pointer = slow_pointer.next
    
    return len(stack) == 0   

class TestPalindromeSinglyLinkedList(unittest.TestCase):
    def test_none_input(self):
        self.assertEqual(palindrome_sll(None), None)
    
    def test_one_input(self):
        self.assertEqual(palindrome_sll(SLLNode(2)), True)

    def test_false_examples(self):
        a, b, c, d= SLLNode(1), SLLNode(2), SLLNode(3), SLLNode(1)
        a.next, b.next, c.next = b, c, d
        self.assertEqual(palindrome_sll(a), False)

    def test_true_examples(self):
        a, b, c, d= SLLNode(1), SLLNode(2), SLLNode(2), SLLNode(1)
        a.next, b.next, c.next = b, c, d
        self.assertEqual(palindrome_sll(a), True)

        a, b, c, d, e= SLLNode(1), SLLNode(2), SLLNode(3), SLLNode(2), SLLNode(1)
        a.next, b.next, c.next, d.next = b, c, d, e
        self.assertEqual(palindrome_sll(a), True)


if __name__ == "__main__": unittest.main()