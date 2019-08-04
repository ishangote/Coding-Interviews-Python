"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.


REMEMBER TESTCASE: 99 + 1
"""

class SLLNode:
    def __init__(self, val):
        self.val = val
        self.next = None

#--------------------------------------------------

def add_two_numbers(l1, l2):
    if not l1: return l2
    if not l2: return l1

    dummy = SLLNode(-999)
    l3 = dummy
    carry = 0

    while l1 or l2:
        temp = 0
        if l1: 
            temp += l1.val
            l1 = l1.next
        if l2:
            temp += l2.val
            l2 = l2.next
        
        l3.next = SLLNode((temp + carry) % 10)
        carry = (temp + carry) // 10

        l3 = l3.next

        if not l1 and not l2 and carry == 1:
                l3.next = SLLNode(carry)

    return dummy.next

#--------------------------------------------------

import unittest
class TestAddTwoNumbers(unittest.TestCase):
    
    def create_list(self, vals):
        dummy = SLLNode(-999)
        curr = dummy
        for val in vals:
            curr.next = SLLNode(val)
            curr = curr.next
        return dummy.next

    def print_list(self, head):
        if not head: return None
        ans = []
        while head:
            ans.append(head.val)
            head = head.next
        return ans

#--------------------------------------------------TESTING

    def test_not_l2(self):
        l1 = self.create_list([2, 4, 3])
        l2 = None
        self.assertEqual(self.print_list(add_two_numbers(l1, l2)), [2, 4, 3])
        
    def test_generic(self):
        l1 = self.create_list([2, 4, 3])
        l2 = self.create_list([8, 1])
        self.assertEqual(self.print_list(add_two_numbers(l1, l2)), [0, 6, 3])

        l1 = self.create_list([9, 9])
        l2 = self.create_list([1])
        self.assertEqual(self.print_list(add_two_numbers(l1, l2)), [0, 0, 1])

        l1 = self.create_list([9, 9])
        l2 = self.create_list([9])
        self.assertEqual(self.print_list(add_two_numbers(l1, l2)), [8, 0, 1])

if __name__ == "__main__": unittest.main()