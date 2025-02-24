import unittest


class SLLNode:
    def __init__(self, value):
        self.value = value
        self.next = None


# Time: O(n), where n => number of nodes in SLL
# Space: O(1)
def insert_in_sorted_circular_sll(node, target):
    insert_node = SLLNode(target)
    insert_node.next = insert_node

    if not node:
        return insert_node

    cur = node
    while True:
        # Case 1: Insert between two nodes
        if cur.value <= target <= cur.next.value:
            insert_node.next = cur.next
            cur.next = insert_node
            return node

        # Case 2: Insert at the end of the list where values "wrap around"
        elif cur.value > cur.next.value:
            if target >= cur.value or target <= cur.next.value:
                insert_node.next = cur.next
                cur.next = insert_node
                return node

        cur = cur.next

        # Case 3: Full circle reached without insertion; insert at the end
        if cur == node:
            insert_node.next = cur.next
            cur.next = insert_node
            return node


class TestInsertInSortedCircularLinkedList(unittest.TestCase):
    def test_insert_in_sorted_circular_sll_None(self):
        res = insert_in_sorted_circular_sll(None, 2)

        self.assertEqual(res.value, 2)
        self.assertEqual(res.next, res)

    def test_insert_in_sorted_circular_sll_generic(self):
        # Create circular list: 1 -> 2 -> 2 -> 5 -> (back to 1)
        node = SLLNode(1)
        node.next = SLLNode(2)
        node.next.next = SLLNode(2)
        node.next.next.next = SLLNode(5)
        node.next.next.next.next = node

        # Insert target value
        insert_in_sorted_circular_sll(node, 3)

        # Check values in circular list
        self.assertEqual(node.next.next.next.value, 3)
        self.assertEqual(node.next.next.next.next.value, 5)

    def test_insert_in_sorted_circular_sll_edge_smallest(self):
        # Insert a smaller value than the smallest node
        node = SLLNode(1)
        node.next = SLLNode(2)
        node.next.next = SLLNode(2)
        node.next.next.next = SLLNode(5)
        node.next.next.next.next = node

        insert_in_sorted_circular_sll(node, 0)

        self.assertEqual(node.next.next.next.next.value, 0)
        self.assertEqual(node.next.next.next.next.next.value, 1)

    def test_insert_in_sorted_circular_sll_edge_largest(self):
        # Insert a larger value than the largest node
        node = SLLNode(1)
        node.next = SLLNode(2)
        node.next.next = SLLNode(2)
        node.next.next.next = SLLNode(5)
        node.next.next.next.next = node

        insert_in_sorted_circular_sll(node, 6)

        self.assertEqual(node.next.next.next.next.value, 6)
        self.assertEqual(node.next.next.next.next.next.value, 1)

    def test_insert_in_sorted_circular_sll_all_same(self):
        # Insert into a list where all values are the same
        node = SLLNode(2)
        node.next = SLLNode(2)
        node.next.next = SLLNode(2)
        node.next.next.next = node

        insert_in_sorted_circular_sll(node, 1)

        self.assertEqual(node.next.value, 1)
        self.assertEqual(node.next.next.value, 2)


if __name__ == "__main__":
    unittest.main()
