"""
Design and implement a data structure for Least Frequently Used (LFU) cache. It should support the following operations: get and put.
get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reaches its capacity, it should invalidate the least frequently used item before inserting a new item. 
For the purpose of this problem, when there is a tie (i.e., two or more keys that have the same frequency), the least recently used key would be evicted.
Note that the number of times an item is used is the number of calls to the get and put functions for that item since it was inserted. This number is set to zero when the item is removed.

Follow up:
Could you do both operations in O(1) time complexity?

Example:
LFUCache cache = new LFUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.get(3);       // returns 3.
cache.put(4, 4);    // evicts key 1.
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4

lfu - mfu
put 1
1

put 2
2 - 1

get 1
2 - 1

put 3
3 - 1

get 2

get 3
1 - 3

put 4
4 - 3

get 1

get 3
4 - 3

get 4
3 - 4


capacity = 3

put 1
1

put 2
2 - 1

get 1
2 - 1

get 2
1 - 2

put 3
3 - 1 - 2

get 1
3 - 2 - 1



"""
class DLLNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class DLL:
    def __init__(self):
        self.sentinel = DLLNode("s", "s")
        self.sentinel.next = self.sentinel
        self.sentinel.prev = self.sentinel
        
class LFUCache:
    def __init__(self, capacity):
        self.lfu_map = {}
        self.lfu_dll = DLL()
        self.capacity = capacity

    def delete_lfu(self):
        tmp = self.lfu_dll.sentinel.next
        self.lfu_dll.sentinel.next = tmp.prev
        tmp.prev.next = tmp.next
        del self.lfu_map[tmp.key]
        

    def update_mfu(self, mfu_node):
        mfu_node.prev.next = mfu_node.next
        mfu_node.next.prev = mfu_node.prev
        
        tmp = self.lfu_dll.sentinel.prev
        self.lfu_dll.sentinel.prev = mfu_node
        mfu_node.next = self.lfu_dll.sentinel
        mfu_node.prev = tmp
        tmp.next = mfu_node
        
    def get(self, key):
        if key not in self.lfu_map: return -1
        self.update_mfu(self.lfu_map[key])
        return self.lfu_map[key].val

    def put(self, key, value):
        if key in self.lfu_map:
            self.update_mfu(self.lfu_map[key])
        
        else:
            mfu_node = DLLNode(key, value)

            if len(self.lfu_map) == self.capacity:
                self.delete_lfu()

            tmp = self.lfu_dll.sentinel.prev
            self.lfu_dll.sentinel.prev = mfu_node
            mfu_node.next = self.lfu_dll.sentinel
            mfu_node.prev = tmp
            tmp.next = mfu_node
            
            self.lfu_map[key] = mfu_node

    def show_lfu_params(self):
        dll = []
        cur = self.lfu_dll.sentinel
        while len(dll) <= len(self.lfu_map):
            dll.append([cur.key, cur.val])
            cur = cur.prev
        print(dll, self.lfu_map)        

import unittest
class TestLFUCache(unittest.TestCase):
    def test_lfu_cache(self):
        lfu = LFUCache(3)
        self.assertEqual(lfu.put(2, 2), None)
        lfu.show_lfu_params()
        self.assertEqual(lfu.put(1, 1), None)
        lfu.show_lfu_params()
        self.assertEqual(lfu.get(2), 2)
        lfu.show_lfu_params()
        self.assertEqual(lfu.get(1), 1)
        lfu.show_lfu_params()
        self.assertEqual(lfu.get(2), 2)
        lfu.show_lfu_params()
        self.assertEqual(lfu.put(3, 3), None)
        lfu.show_lfu_params()
        self.assertEqual(lfu.put(4, 4), None)
        lfu.show_lfu_params()
        self.assertEqual(lfu.get(3), 3)
        lfu.show_lfu_params()
        self.assertEqual(lfu.get(2), 2)
        lfu.show_lfu_params()
        self.assertEqual(lfu.get(1), -1)
        lfu.show_lfu_params()
        self.assertEqual(lfu.get(4), 4)
        lfu.show_lfu_params()

if __name__ == "__main__": unittest.main()