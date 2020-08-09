"""
REF: https://github.com/aman-a-agarwal/coding/blob/10fff53f1832ad4dec1d041fd604141a23be064f/Arrays/restoreArray.py

pairs = 
[[5, 3], [1, 5], [7, 3], [4, 6], [2, 1], [2, 4]]
                                           ^

*
6 <-> 4 <-> 2 <-> 1 <-> 5 <-> 3 <-> 7

Properties of head:
one adjacent_count 
head.prev == None

"""

class DLLNode:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None
        self.adjacent_count = 1
        
def restore_array(pairs):
    nodes = {}
    for pair in pairs:
        num1 = pair[0]
        num2 = pair[1]

        num1_node = None
        num2_node = None

        if num1 not in nodes:
            num1_node = DLLNode(num1)
            nodes[num1] = num1_node
        else:
            num1_node = nodes[num1]
            num1_node.adjacent_count += 1

        if num2 not in nodes:
            num2_node = DLLNode(num2)
            nodes[num2] = num2_node
        else:
            num2_node = nodes[num2]
            num2_node.adjacent_count += 1

        if num1_node.next is None and num2_node.prev is None:
            num1_node.next = num2_node
            num2_node.prev = num1_node
        elif num2_node.next is None and num1_node.prev is None:
            num2_node.next = num1_node
            num1_node.prev = num2_node
        else:
            if num1_node.next is None:
                node = num2_node
                while node is not None:
                    tempNode = node.prev
                    node.next = tempNode
                    node = tempNode
            elif num1_node.prev is None:
                node = num2_node
                while node is not None:
                    tempNode = node.next
                    node.prev = tempNode
                    node = tempNode
    ans = []
    for node_val in nodes.keys():
        node = nodes.get(node_val)
        if node.adjacent_count == 1 and node.prev is not None:
            while (node is not None):
                ans.append(node.val)
                node = node.prev

    return ans

import unittest
class TestRestoreArray(unittest.TestCase):
    def test_generic(self):
        self.assertEqual(restore_array([[5, 3], [1, 5], [7, 3], [4, 6], [2, 1], [2, 4]]), [6, 4, 2, 1, 5, 3, 7])
        self.assertEqual(restore_array([[3, 5], [1, 4], [2, 4], [1, 5]]), [3, 5, 1, 4, 2])

if __name__ == "__main__": unittest.main()