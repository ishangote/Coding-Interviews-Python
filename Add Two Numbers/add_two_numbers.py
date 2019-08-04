"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""

class SLLNode:
    def __init__(self, val):
        self.val = val
        self.next = None

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
        
        l3.next = SLLNode(temp % 10 + carry)
        carry = temp // 10

        l3 = l3.next

        if not l1 and not l2 and carry == 1:
                l3.next = ListNode(carry)

    return dummy.next

import unittest
class TestAddTwoNumbers(unittest.TestCase):