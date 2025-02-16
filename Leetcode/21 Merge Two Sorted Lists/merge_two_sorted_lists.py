import unittest
from sll import print_list, make_list, SLLNode


# Time: O(n + m), where n => number of nodes in list1, m => number of nodes in list2
# Space: O(1)
def merge_two_sorted_lists(head1, head2):
    tail = dummy = SLLNode("DUMMY")

    while head1 and head2:
        if head1.value <= head2.value:
            tail.next = head1
            head1 = head1.next

        else:
            tail.next = head2
            head2 = head2.next

        tail = tail.next

    tail.next = head1 if head1 else head2

    return dummy.next


class TestMergeTwoSortedLinkedLists(unittest.TestCase):
    def test_merge_two_sorted_linked_lists(self):
        self.assertEqual(print_list(merge_two_sorted_lists(None, None)), [])

        l1 = make_list([])
        l2 = make_list([-2, 2, 3])
        self.assertEqual(print_list(merge_two_sorted_lists(l1, l2)), [-2, 2, 3])

        l1 = make_list([-1, 2, 6])
        l2 = make_list([])
        self.assertEqual(print_list(merge_two_sorted_lists(l1, l2)), [-1, 2, 6])

        l1 = make_list([-1, 2, 6])
        l2 = make_list([-2, 2, 3])
        self.assertEqual(
            print_list(merge_two_sorted_lists(l1, l2)), [-2, -1, 2, 2, 3, 6]
        )


if __name__ == "__main__":
    unittest.main()
