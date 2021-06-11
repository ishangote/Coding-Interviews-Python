import unittest
from remove_duplicates import SLLNode
from remove_duplicates import remove_duplicates

class TestRemoveDuplicatesFromLinkedList(unittest.TestCase):
    def generate_sll(self, nums):
        if not nums: return None
        run = dummy = SLLNode("dummy")
        
        for n in nums:
            run.next = SLLNode(n)
            run = run.next
        
        return dummy.next

    def get_values_from_sll(self, head):
        nums = []
        while head:
            nums.append(head.value)
            head = head.next
        return nums
        
    def test_generic(self):
        sll1 = self.generate_sll([1, 2, 2, 3, 3, 3])
        self.assertEqual([1, 2, 3], self.get_values_from_sll(remove_duplicates(sll1)))

        sll2 = self.generate_sll([1, 1, 1])
        self.assertEqual([1], self.get_values_from_sll(remove_duplicates(sll2)))

        sll3 = None
        self.assertEqual([], self.get_values_from_sll(remove_duplicates(sll3)))

if __name__ == "__main__": unittest.main()
