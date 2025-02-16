import unittest


class SLLNode:
    def __init__(self, value, next=None, random=None):
        self.value = value
        self.next = next
        self.random = random

    def __hash__(self):
        return id(self)  # Keep hash method for dictionary keys

    def __eq__(self, other):
        """Check structural equality (same values, same structure)."""
        if not isinstance(other, SLLNode):
            return False
        return self.value == other.value


# Time: O(n) where n => number of nodes in sll
# Space: O(n)
def copy_random_list_hm(head):
    if not head:
        return None

    copy_nodes = {}
    cur = head
    while cur:
        copy_nodes[cur] = SLLNode(cur.value)
        cur = cur.next

    cur = head
    while cur:
        copy_nodes[cur].next = copy_nodes[cur.next] if cur.next else None
        copy_nodes[cur].random = copy_nodes[cur.random] if cur.random else None
        cur = cur.next

    return copy_nodes[head]


# -------------------------------------------------------- #


# Time: O(n), where n => number of nodes in sll
# Space: O(1)
def copy_random_list_optimized(head):
    if not head:
        return None

    # First Pass: Insert copied nodes
    cur = head
    while cur:
        tmp = cur.next
        cur.next = SLLNode(cur.value)
        cur.next.next = tmp
        cur = tmp

    # Second Pass: Assign random pointers
    cur = head
    while cur:
        cur.next.random = cur.random.next if cur.random else None
        cur = cur.next.next

    # Third Pass: Restore original list and extract the copied list
    cur = head
    copy_head = copy_cur = head.next

    while cur and cur.next:
        cur.next = cur.next.next
        cur = cur.next

        if copy_cur and copy_cur.next:
            copy_cur.next = copy_cur.next.next
            copy_cur = copy_cur.next

    return copy_head


# -------------------------------------------------------- #


class TestRandomLinkedList(unittest.TestCase):
    def list_to_dict(self, head):
        """Helper method to convert linked list to dictionary representation for easier comparison."""
        nodes = {}
        cur = head
        while cur:
            nodes[cur] = {"val": cur.value, "next": cur.next, "random": cur.random}
            cur = cur.next
        return nodes

    def test_copy_random_list_hm_none_input(self):
        self.assertIsNone(copy_random_list_hm(None))

    def test_copy_random_list_optimized_none_input(self):
        self.assertIsNone(copy_random_list_optimized(None))

    def test_copy_random_list_hm_single_node_no_random(self):
        node = SLLNode(1)
        copied_head = copy_random_list_hm(node)
        self.assertEqual(copied_head.value, node.value)
        self.assertIsNone(copied_head.next)
        self.assertIsNone(copied_head.random)

    def test_copy_random_list_optimized_single_node_no_random(self):
        node = SLLNode(1)
        copied_head = copy_random_list_optimized(node)
        self.assertEqual(copied_head.value, node.value)
        self.assertIsNone(copied_head.next)
        self.assertIsNone(copied_head.random)

    def test_copy_random_list_hm_single_node_with_random(self):
        node = SLLNode(1)
        node.random = node  # Random pointer points to itself
        copied_head = copy_random_list_hm(node)
        self.assertEqual(copied_head.value, node.value)
        self.assertIsNone(copied_head.next)
        self.assertEqual(
            copied_head.random, copied_head
        )  # Should point to itself in copy

    def test_copy_random_list_optimized_single_node_with_random(self):
        node = SLLNode(1)
        node.random = node  # Random pointer points to itself
        copied_head = copy_random_list_optimized(node)
        self.assertEqual(copied_head.value, node.value)
        self.assertIsNone(copied_head.next)
        self.assertEqual(
            copied_head.random, copied_head
        )  # Should point to itself in copy

    def test_copy_random_list_hm_multiple_nodes(self):
        node1 = SLLNode(1)
        node2 = SLLNode(2)
        node3 = SLLNode(3)

        node1.next = node2
        node2.next = node3

        node1.random = node3
        node2.random = node1
        node3.random = node2

        copied_head = copy_random_list_hm(node1)
        copied_dict = self.list_to_dict(copied_head)
        original_dict = self.list_to_dict(node1)

        self.assertEqual(len(copied_dict), len(original_dict))
        for orig, copy in zip(original_dict.values(), copied_dict.values()):
            self.assertEqual(orig["val"], copy["val"])
            self.assertEqual(orig["next"] is not None, copy["next"] is not None)
            self.assertEqual(orig["random"] is not None, copy["random"] is not None)

    def test_copy_random_list_optimized_multiple_nodes(self):
        node1 = SLLNode(1)
        node2 = SLLNode(2)
        node3 = SLLNode(3)

        node1.next = node2
        node2.next = node3

        node1.random = node3
        node2.random = node1
        node3.random = node2

        copied_head = copy_random_list_optimized(node1)
        copied_dict = self.list_to_dict(copied_head)
        original_dict = self.list_to_dict(node1)

        self.assertEqual(len(copied_dict), len(original_dict))
        for orig, copy in zip(original_dict.values(), copied_dict.values()):
            self.assertEqual(orig["val"], copy["val"])
            self.assertEqual(orig["next"] is not None, copy["next"] is not None)
            self.assertEqual(orig["random"] is not None, copy["random"] is not None)


if __name__ == "__main__":
    unittest.main()
