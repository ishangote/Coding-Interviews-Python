import unittest
from lru_cache import LRUCache

class TestLRUCache(unittest.TestCase):
    def test_lru_cache_generic(self):
        lru = LRUCache(2)
        self.assertEqual(lru.put(1, 1), None)
        self.assertEqual(lru.put(2, 2), None)
        self.assertEqual(lru.get(1), 1)
        self.assertEqual(lru.put(3, 3), None)
        self.assertEqual(lru.get(2), -1)
        self.assertEqual(lru.put(4, 4), None)
        self.assertEqual(lru.get(1), -1)
        self.assertEqual(lru.get(3), 3)
        self.assertEqual(lru.get(4), 4)

if __name__ == "__main__": unittest.main()