import unittest


class SLLNode:
    def __init__(self, value):
        self.value = value
        self.next = None


# Time: O(n)
# Space: O(1)
def merge_nodes(head):
    cur = head.next
    cur_sum = 0

    tail = None

    while cur:
        if cur.value == 0:
            if not tail:
                tail = head = SLLNode(cur_sum)
            else:
                tail.next = SLLNode(cur_sum)
                tail = tail.next

            cur_sum = 0

        else:
            cur_sum += cur.value

        cur = cur.next

    return head


class TestMergeNodesInBetweenZeroes(unittest.TestCase):
    def test_merge_nodes_in_between_zeroes(self):
        head = SLLNode(0)
        head.next = SLLNode(3)
        head.next.next = SLLNode(1)
        head.next.next.next = SLLNode(0)
        head.next.next.next.next = SLLNode(4)
        head.next.next.next.next.next = SLLNode(5)
        head.next.next.next.next.next.next = SLLNode(2)
        head.next.next.next.next.next.next.next = SLLNode(0)

        res = merge_nodes(head)

        self.assertEqual(res.value, 4)
        self.assertEqual(res.next.value, 11)


if __name__ == "__main__":
    unittest.main()
