"""
BT: 0, 1, 2 children
BST: left_child_subtree_nodes <= node.val < right_child_subtree_nodes.val


moving left ->  lower = roots lower
                upper = root.val

moving right ->  lower = root.val
                 upper = roots upper

"""

# Code after interview:
#Recursive Solution
def is_valid_bst(root):
    return is_valid_bst_util(root, -float('inf'), float('inf'))

def is_valid_bst_util(node, lower, upper):
    if not node: return True
    if lower > node.val or upper < node.val: return False
    return is_valid_bst_util(node.left, lower, node.val) and is_valid_bst_util(node.right, node.val, upper)

#iterative Solution
import sys
def is_valid_bst(root):
    if not root: return True

    stack = [(root, -sys.maxsize, sys.maxsize)]

    while stack:
        node, lower, upper = stack.pop()
        if lower > node.val or node.val > upper: return False

        if node.left: stack.append((node.left, lower, node.val))
        if node.right: stack.append((node.right, node.val, upper))
    
    return True

"""
Feedback:
Binary Trees
Binary Search Tree

Instead of assuming stack for DFS, state that it's a concisous choice
Like we can do DFS recurrsively or iteratively. I would prefer iteratively as we can manage the stack explicitly.
Again for DFS, binary search no psuedo code is really necessary.
It kinda wastes time
Did not take enough examples
Interviewer gave a perfect example and asked a question. Candidate did not try to answer that question. 
Did not listen to interviewer's direct question --> RED FLAG
Did not let interviewer speak --> BIG RED FLAG
So what you are trying to hint me at..
Instead...So are you suggesting we can...?
use -sys.maxint and sys.maxint instead
Should not go into code optimization (fail fast for or vs and) in your mind. Most interviewers will think you are struggling with basic code logic. And not know what exactly you are thinking about. Choose and option and move on fluently. Else state clearly what you are thinking, 
possibly at the very end of the interview. Do not spend time on such stuff, it's very risky.
No of nodes in the root. --> Tree
"""