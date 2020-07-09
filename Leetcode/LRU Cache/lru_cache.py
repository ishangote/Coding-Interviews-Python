# Design and implement a data structure for Least Recently Used (LRU) cache.
# It should support the following operations: get and put.
# get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
# put(key, value) - Set or insert the value if the key is not already present.
# When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.
# The cache is initialized with a positive capacity.
# Follow up:
# Could you do both operations in O(1)

"""
Design:

              MRU   dll     LRU
put           h     1       t
put           h   2   1     t
get 1         h   1   2     t
put 3         h   3   1     t   
get 2         -1
put 4         h   4   3     t


delete from tail
add from head

"""
class DLLNode:
    def __init__(self, key, val):
        #key required to store as a parameter to object for deletion from hm later
        self.key = key
        self.val = val
        self.next = None
        self.prev = None
        
    def set_node_val(self, val):
        self.val = val
        
class DLL:
    def __init__(self):
        self.size = 0
        #head.next is MRU and tail.prev is LRU
        self.head = DLLNode(None, "head")
        self.tail = DLLNode(None, "tail")    
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def move_node_to_head(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        
        node.prev = self.head
        node.next = self.head.next
        node.next.prev = node
        self.head.next = node
        

    def delete_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

        del_val = node.val
        del node        

        self.size -= 1

        #Returns value of deleted node to delete from hm later
        return del_val

    def add_heads_next(self, key, val):
        node = DLLNode(key, val)
        tmp = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = tmp
        tmp.prev = node
        
        self.size += 1
        
        return node

    def print_list(self):
        cur = self.head.next
        ans = []
        while cur != self.tail:
            ans.append(cur.val)
            cur = cur.next
        return ans

        
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dll = DLL()
        self.hm = {}

    def get(self, key: int) -> int:
        if key not in self.hm: return -1 
        #Make node MRU
        self.dll.move_node_to_head(self.hm[key])
        return self.hm[key].val
    
    def put(self, key: int, value: int) -> None:
        if key in self.hm:
            self.dll.delete_node(self.hm[key])
            del self.hm[key]

        if self.dll.size == self.capacity:
            #key required here
            del self.hm[self.dll.tail.prev.key]
            self.dll.delete_node(self.dll.tail.prev)
            
        self.hm[key] = self.dll.add_heads_next(key, value)

    def print_lru(self):
        return self.dll.print_list()

import unittest
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

        self.assertEqual(lru.print_lru(), [4, 3])


if __name__ == "__main__": unittest.main()