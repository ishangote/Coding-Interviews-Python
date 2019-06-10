# Design and implement a data structure for Least Recently Used (LRU) cache.
# It should support the following operations: get and put.
# get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
# put(key, value) - Set or insert the value if the key is not already present.
# When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.
# The cache is initialized with a positive capacity.
# Follow up:
# Could you do both operations in O(1)
from DLL_Class import *
class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.hm = {}
        self.dll = DLL()
        self.size = 0
    
    def put(self, key, value):
        if key in self.hm:
            self.hm[key].value = value
            self.update_node_position(self.hm[key])
        else:
            self.size += 1
            if self.size > self.capacity:
                self.pop_lru()

            node = DLL_Node(key, value)
            self.hm[key] = node
            self.dll.add_node(node)
        
        return self.get_current_lru()

    def get(self, key):
        if key not in self.hm: return
        node = self.hm[key]
        yield node.value
        self.update_node_position(node)

    def pop_lru(self):
        key = self.dll.tail.key
        del self.hm[key]
        if self.dll.tail == self.dll.head: self.dll.head = self.dll.tail = None
        else: 
            self.dll.tail = self.dll.tail.prev
            self.dll.tail.next = None
        self.size -= 1
        return self.get_current_lru()

    def update_node_position(self, node):
        if node == self.dll.head: return
        elif node == self.dll.tail:
            self.dll.tail.next = self.dll.head
            self.dll.head.prev = self.dll.tail
            self.dll.head = self.dll.tail
            self.dll.tail = self.dll.tail.prev
            self.dll.tail.next = None
            self.dll.head.prev = None
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
            node.prev = None
            node.next = self.dll.head
            self.dll.head.prev = node
            self.dll.head = self.dll.head.prev
        return self.get_current_lru()

    def get_current_lru(self):
        if self.dll.tail: return (self.dll.tail.key, self.dll.tail.value)

import unittest
class TestLRUCache(unittest.TestCase):
    def test_lru_cache_generic(self):
        lru = LRUCache(3)
        self.assertEqual(list(lru.get(2)), [])
        self.assertEqual(lru.put(1, 1), (1, 1))
        self.assertEqual(list(lru.get(1)), [1])
        self.assertEqual(lru.put(2, 2), (1, 1))
        self.assertEqual(lru.put(3, 3), (1, 1))
        self.assertEqual(lru.put(4, 4), (2, 2))
        self.assertEqual(list(lru.get(2)), [2])
        self.assertEqual(lru.put(2, 18), (3, 3))
        self.assertEqual(list(lru.get(2)), [18])
        self.assertEqual(list(lru.get(11)), [])
        self.assertEqual(list(lru.get(3)), [3])

if __name__ == "__main__": unittest.main()