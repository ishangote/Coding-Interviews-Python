# Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

"""
Example:
Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6


"""
class SLLNode:
    def __init__(self, val):
        self.val = val
        self.next = None

import heapq
def merge_k_lists(list):

    min_heap = []
    for head in list:
        if head: heapq.heappush(min_heap, (head.val, head))
    
    dummy = SLLNode('DUMMY')
    tail = dummy
    while min_heap:
        data, node = heapq.heappop(min_heap)
        tail.next = node
        tail = tail.next

        if node.next:
            node = node.next
            heapq.heappush(min_heap, (node.val, node))
    
    return dummy.next

# Run in Python2
import unittest
class TestMergeKLists(unittest.TestCase):
    def test_merge_None(self):
        sll1, sll2, sll3 = None, None, None
        list1 = [sll1, sll2, sll3]
        self.assertEqual(merge_k_lists(list1), None)

        sll4, sll5, sll6 = SLLNode(1), None, None
        list2 = [sll4, sll5, sll6]
        self.assertEqual(merge_k_lists(list2), sll4)

    def test_merge_k_lists_generic(self):
        sll1, sll2, sll3 = SLLNode(1), SLLNode(1), SLLNode(2)
        sll1.next = SLLNode(4)
        sll1.next.next = SLLNode(5)
        sll2.next = SLLNode(3)
        sll2.next.next = SLLNode(4)
        sll3.next = SLLNode(6)
        list = [sll1, sll2, sll3]

        self.assertEqual(merge_k_lists(list).val, sll1.val)

if __name__ == '__main__': unittest.main()