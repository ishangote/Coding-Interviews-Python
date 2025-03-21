import unittest


class DLLNode:
    def __init__(self, key, value):
        # Store both key and value in the node
        self.key = key
        self.value = value
        self.next = None
        self.prev = None


class LRUCache:
    # Space: O(capacity)
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}  # Maps key to its node in the linked list.

        # Create dummy head and tail nodes to avoid edge case checks.
        self.head = DLLNode("DUMMY_HEAD", -1)
        self.tail = DLLNode("DUMMY_TAIL", -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    # Time: O(1)
    def _remove(self, node):
        # Remove node from the doubly-linked list.
        node.prev.next = node.next
        node.next.prev = node.prev

    # Time: O(1)
    def _add(self, node):
        # Add node right after the head (most recent position).
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    # Time O(1)
    def get(self, key):
        if key not in self.cache:
            return -1

        # Move node to the head (mark as recently used)
        node = self.cache[key]
        self._remove(node)
        self._add(node)

        return node.value

    # Time: O(1)
    def put(self, key, value):
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self._remove(node)
            self._add(node)
        else:
            # If cache is at capacity, remove the LRU node from the tail
            if len(self.cache) == self.capacity:
                lru = self.tail.prev
                self._remove(lru)
                del self.cache[lru.key]

            # Insert the new node at the head of the list
            node = DLLNode(key, value)
            self.cache[key] = node
            self._add(node)


class TestLRUCache(unittest.TestCase):
    def test_get_and_put(self):
        # Create a cache with capacity 2.
        cache = LRUCache(2)

        # Add two entries.
        cache.put(1, 1)
        cache.put(2, 2)
        # Get key 1, which should be present.
        self.assertEqual(cache.get(1), 1, "Expected value 1 for key 1")

        # Add a new key; since capacity is 2, this should evict the least recently used key.
        cache.put(3, 3)  # Key 2 should be evicted.
        self.assertEqual(cache.get(2), -1, "Expected key 2 to be evicted")

        # Adding another key should evict key 1.
        cache.put(4, 4)  # Key 1 should be evicted.
        self.assertEqual(cache.get(1), -1, "Expected key 1 to be evicted")
        self.assertEqual(cache.get(3), 3, "Expected key 3 to be present")
        self.assertEqual(cache.get(4), 4, "Expected key 4 to be present")

    def test_update_existing_key(self):
        # Create a cache with capacity 2.
        cache = LRUCache(2)
        cache.put(1, 1)
        self.assertEqual(cache.get(1), 1, "Initial value for key 1 should be 1")

        # Update the same key with a new value.
        cache.put(1, 10)
        self.assertEqual(cache.get(1), 10, "After update, value for key 1 should be 10")

        # Fill the cache and update again.
        cache.put(2, 2)
        cache.put(1, 100)
        self.assertEqual(
            cache.get(1), 100, "After second update, value for key 1 should be 100"
        )
        self.assertEqual(cache.get(2), 2, "Key 2 should still be present")

    def test_non_existent_key(self):
        # Create a cache with capacity 2.
        cache = LRUCache(2)
        # Try to get a key that was never added.
        self.assertEqual(cache.get(99), -1, "Non-existent key should return -1")


if __name__ == "__main__":
    unittest.main()
