# Design and implement a data structure for Least Recently Used (LRU) cache.
# It should support the following operations: get and put.
# get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
# put(key, value) - Set or insert the value if the key is not already present.
# When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.
# The cache is initialized with a positive capacity.
# Follow up:
# Could you do both operations in O(1)
class DLLNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None
        
    def set_new_val(self, new_val):
        self.val = new_val
    
    def get_val(self):
        return self.val


class DLL:
    def __init__(self, capacity):
        self.capacity = capacity
        self.head = self.tail = None
    
    def add_node(self, val):
        if self.capacity == 0:
            self.pop_head()
            
        if not self.head: 
            self.head = self.tail = DLLNode(val)
        else:
            self.tail.next = DLLNode(val)
            self.tail.next.prev = self.tail
            self.tail = self.tail.next
            
        self.capacity -= 1
        return self.tail
            
    def pop_head(self):
        if self.head == self.tail:
            self.head = self.tail = None

        else:
            self.head = self.head.next
            self.head.prev = None
            
        self.capacity += 1
        
    def update_node(self, node, new_val):
        if not node: return

        node = self.make_node_tail(node)
        if node.val != new_val: node.set_new_val(new_val)
        
    def make_node_tail(self, node):
        if node == self.tail: return node
        if node == self.head:
            self.tail.next = self.head
            self.head.prev = self.tail
            
            self.head = self.head.next
            self.head.prev = None
            
            self.tail = self.tail.next
            self.tail.next = None
        
            
class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.dll = DLL(capacity)
        self.hm = {}

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.hm:
            self.dll.make_node_tail(self.hm[key])
            return self.hm[key].get_val()
        return -1
        
    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.hm: 
            self.dll.update_node(node, value)
        else:
            self.dll.add_node(value)
            if self.dll.capacity == 0: del self.hm[key]

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