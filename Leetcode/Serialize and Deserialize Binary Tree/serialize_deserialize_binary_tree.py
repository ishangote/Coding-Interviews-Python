# Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, 
# or transmitted across a network connection link to be reconstructed later in the same or another computer environment.
# Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. 
# You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.
"""
Example: 
You may serialize the following tree:

    1
   / \
  2   3
     / \
    4   5

as "[1,2,3,null,null,4,5]"
Clarification: The above format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.

Note: Do not use class member/global/static variables to store states. Your serialize and deserialize algorithms should be stateless.

Serialization: Level order traversal

Deserialization:
ser = [1, 2, 3, None, None, 4, 5]
             i
root = 1
q = [2, 3]
->
        1
    2       3

"""
class BTNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

from collections import deque
class SerializationDeserialization:
    #Level order
    def serialize(self, root):
        if not root: return ""
        ans = ""
        queue = deque([root])

        while queue:
            node = queue.pop()
            if not node:
                ans += "None,"
                continue
            ans += str(node.val) + ','
            queue.appendleft(node.left)
            queue.appendleft(node.right)

        return ans

    def deserialize(self, data):
        if not data: return None
        data = data.split(',')
        
        root = BTNode(int(data[0]))
        queue = deque([root])

        i = 1
        while queue and i < len(data):
            node = queue.pop()

            left = data[i]
            if left != "None":
                node.left = BTNode(int(left))
                queue.appendleft(node.left)
            
            i += 1
            right = data[i]
            if right != "None":
                node.right = BTNode(int(right))
                queue.appendleft(node.right)
            i += 1

        return root