# First Non Repeating Character in STREAM of Integers

"""

1 2 3 1 4 5 6 7 1 2 8 9 6 7
                  ^

fnr = 3

hs = (1, 2, 3, 4, 5, 6, 7)
DLL: 3


Optimization => Use Hash Map (hm) instead of set. 

"""
import unittest
#Doubly Linked list to track sequence of non-repeating integers appearing
class DLLNode:
    def __init__(self, data, next, prev):
        self.data = data
        self.next = next
        self.prev = prev

#Deletion and Addition to the doubly linked list
class DLL:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def append_number(self, num):
        if self.tail:
            self.tail.next = DLLNode(num, None, self.tail)
            self.tail = self.tail.next

        else:
            self.head = self.tail = DLLNode(num, None, None)

    def delete_num(self, del_node):
        if del_node == self.head: self.head = del_node.next
        if del_node == self.tail: self.tail = del_node.prev
        if del_node.next: del_node.next.prev = del_node.prev
        if del_node.prev: del_node.prev.next = del_node.next

#To initialize the doubly linked list and hm
class FNR:
    def __init__(self):
        self.dll = DLL()
        self.hm = {}            

    def first_non_repeating(self, stream_input):
        
        if type(stream_input) != int: return None

        if stream_input in self.hm.keys():
            self.dll.delete_num(self.hm[stream_input])
            if self.dll.head: return self.dll.head.data
        
        else:
            self.dll.append_number(stream_input)
            self.hm[stream_input] = self.dll.tail


        if self.dll.head: return self.dll.head.data
        return None


class TestFirstNonRepeatingInteger(unittest.TestCase):

    def test_invalid_input(self):
        fnr = FNR()
        self.assertEqual(fnr.first_non_repeating(None), None)
        self.assertEqual(fnr.first_non_repeating("a"), None)
        self.assertEqual(fnr.first_non_repeating(4.5), None)

    def test_all_equal(self):
        fnr = FNR()
        self.assertEqual(fnr.first_non_repeating(1), 1)
        self.assertEqual(fnr.first_non_repeating(1), None)
        self.assertEqual(fnr.first_non_repeating(1), None)
        self.assertEqual(fnr.first_non_repeating(1), None)

    def test_head_delete(self):
        fnr = FNR()
        self.assertEqual(fnr.first_non_repeating(1), 1)
        self.assertEqual(fnr.first_non_repeating(2), 1)
        self.assertEqual(fnr.first_non_repeating(3), 1)
        self.assertEqual(fnr.first_non_repeating(1), 2)
    
    def test_generic(self):
        fnr = FNR()
        self.assertEqual(fnr.first_non_repeating(1), 1)
        self.assertEqual(fnr.first_non_repeating(2), 1)
        self.assertEqual(fnr.first_non_repeating(3), 1)
        self.assertEqual(fnr.first_non_repeating(2), 1)
        self.assertEqual(fnr.first_non_repeating(4), 1)
        self.assertEqual(fnr.first_non_repeating(1), 3)

if __name__ == "__main__": unittest.main()    