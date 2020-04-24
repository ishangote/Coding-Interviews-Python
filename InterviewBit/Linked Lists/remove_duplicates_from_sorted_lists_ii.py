class SLLNode:
    def __init__(self, val):
        self.val = val
        self.next = None

def deleteDuplicates(A):
    dummy = prev = SLLNode("dummy")
    dummy.next = A
    
    curr = A
    
    while curr and curr.next:
        if curr.val == curr.next.val:
            while curr and curr.next and curr.val == curr.next.val: 
                curr= curr.next
            
            curr = curr.next
            prev.next = curr
            
            
        else:
            prev = prev.next
            curr = curr.next
            
    return dummy.next

import unittest
class TestRemoveDuplicatesii(unittest.TestCase):
    #1->2->3->3->3->4->4->5
    head = SLLNode(1)
    head.next = SLLNode(2)
    head.next.next = SLLNode(3)
    head.next.next.next = SLLNode(3)
    head.next.next.next.next = SLLNode(3)
    head.next.next.next.next.next = SLLNode(4)
    head.next.next.next.next.next.next = SLLNode(4)
    head.next.next.next.next.next.next.next = SLLNode(5)

    dup = SLLNode(1)
    dup.next = SLLNode(1)
    dup.next.next = SLLNode(1)

    def print_node_vals(self, node):
        ans = []
        while node:
            ans.append(node.val)
            node = node.next
        return ans

    def test_invalid_input(self):
        self.assertEqual(self.print_node_vals(deleteDuplicates(None)), [])

    def test_all_duplicates(self):
        
        self.assertEqual(self.print_node_vals(deleteDuplicates(self.dup)), [])

    def test_remove_duplicates_generic(self):
        self.assertEqual(self.print_node_vals(deleteDuplicates(self.head)), [1, 2, 5])

if __name__ == "__main__": unittest.main()