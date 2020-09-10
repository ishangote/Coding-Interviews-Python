"""
You're given 2 huge integers represented by linked lists. Each linked list element is a number from 0 to 9999 that represents a number with exactly 4 digits. The represented number might have leading zeros. Your task is to add up these huge integers and return the result in the same format.

Example
For a = [9876, 5432, 1999] and b = [1, 8001], the output should be
addTwoHugeNumbers(a, b) = [9876, 5434, 0].

Explanation: 987654321999 + 18001 = 987654340000.

For a = [123, 4, 5] and b = [100, 100, 100], the output should be
addTwoHugeNumbers(a, b) = [223, 104, 105].

Explanation: 12300040005 + 10001000100 = 22301040105.

Input/Output

[execution time limit] 4 seconds (py3)

[input] linkedlist.integer a

The first number, without its leading zeros.

Guaranteed constraints:
0 ≤ a size ≤ 104,
0 ≤ element value ≤ 9999.

[input] linkedlist.integer b

The second number, without its leading zeros.

Guaranteed constraints:
0 ≤ b size ≤ 104,
0 ≤ element value ≤ 9999.

[output] linkedlist.integer

The result of adding a and b together, returned without leading zeros in the same format.
"""

class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class SLL:
    def __init__(self, head):
        self.head = head

    def parse_sll(self):
        ans = []
        while self.head:
            ans.append(self.head.value)
            self.head = self.head.next
        return ans

    def create_sll(self, nums):
        cur = dummy = ListNode("DUMMY")
        for n in nums:
            cur.next = ListNode(n)
            cur = cur.next
        self.head = dummy.next
        return self.head
        
"""
prev = None
    1 -> 2 -> 3
    ^
"""
def reverse_sll(head):
    prev = None
    cur = head
    while cur:
        tmp = cur.next
        cur.next = prev
        prev = cur
        cur = tmp
    return prev
  
def addTwoHugeNumbers(a, b):
    a = reverse_sll(a)
    b = reverse_sll(b)
    
    ans = dummy = ListNode("DUMMY")
    cur_a, cur_b = a, b
    carry = 0
    while cur_a or cur_b:
        num_a, num_b = 0, 0
        if cur_a:
            num_a  = cur_a.value
            cur_a = cur_a.next
        
        if cur_b:
            num_b = cur_b.value
            cur_b = cur_b.next
            
        tmp = num_a + num_b + carry
        ans.next = ListNode(tmp % 10000)
        ans = ans.next
        carry = tmp // 10000
        
    if carry:
        ans.next = ListNode(carry)
        
    head = reverse_sll(dummy.next)
    sll = SLL(head)
    return sll.parse_sll()

import unittest
class TestAddTwoHugeNumbers(unittest.TestCase):
    def test_generic(self):
        a, b = SLL(None), SLL(None)
        a_head = a.create_sll([9876, 5432, 1999])
        b_head = b.create_sll([1, 8001])
        self.assertEqual(addTwoHugeNumbers(a_head, b_head), [9876, 5434, 0])

    def test_generic2(self):
        a, b = SLL(None), SLL(None)
        a_head = a.create_sll([123, 4, 5])
        b_head = b.create_sll([100, 100, 100])
        self.assertEqual(addTwoHugeNumbers(a_head, b_head), [223, 104, 105])

    def test_generic3(self):
        a, b = SLL(None), SLL(None)
        a_head = a.create_sll([1234, 1234, 0])
        b_head = b.create_sll([0])
        self.assertEqual(addTwoHugeNumbers(a_head, b_head), [1234, 1234, 0])

    def test_generic4(self):
        a, b = SLL(None), SLL(None)
        a_head = a.create_sll([1])
        b_head = b.create_sll([9999, 9999, 9999, 9999, 9999, 9999])
        self.assertEqual(addTwoHugeNumbers(a_head, b_head), [1, 0, 0, 0, 0, 0, 0])

if __name__ == "__main__": unittest.main()