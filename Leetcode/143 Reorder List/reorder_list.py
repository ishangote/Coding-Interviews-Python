import unittest


class SLLNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def reorder_list(head):
    slow, fast = head, head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    prev = None
    cur = slow.next
    slow.next = None

    while cur:
        tmp = cur.next
        cur.next = prev
        prev = cur
        cur = tmp

    pt1, pt2 = head, prev

    while pt2:
        tmp1 = pt1.next
        pt1.next = pt2
        pt1 = tmp1

        tmp2 = pt2.next
        pt2.next = pt1
        pt2 = tmp2

    return head


class TestReorderList(unittest.TestCase):

    head1 = SLLNode(1)
    head1.next = SLLNode(2)
    head1.next.next = SLLNode(3)
    head1.next.next.next = SLLNode(4)
    head1.next.next.next.next = SLLNode(5)

    head2 = SLLNode(1)
    head2.next = SLLNode(2)
    head2.next.next = SLLNode(3)
    head2.next.next.next = SLLNode(4)

    def print_nodes(self, head):
        if not head:
            return []
        curr = head
        ans = []
        while curr:
            ans.append(curr.val)
            curr = curr.next
        return ans

    def test_generic(self):
        self.assertEqual(self.print_nodes(reorder_list(self.head1)), [1, 5, 2, 4, 3])
        self.assertEqual(self.print_nodes(reorder_list(self.head2)), [1, 4, 2, 3])


if __name__ == "__main__":
    unittest.main()
