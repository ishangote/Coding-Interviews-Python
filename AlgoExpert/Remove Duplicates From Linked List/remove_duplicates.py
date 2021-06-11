"""
Questions:
1. input == None? return None
2. node value integer? yes
3. SLL? yes
4. inplace? yes

Examples:
head = 
1 -> 2 -> 2 -> 3
ans = 
1 -> 2 -> 3

    d -> 1 -> 2 -> 2 -> 2 -> 3
                                c
                                p

Time: O(n), n => number of nodes
Space: O(1)
"""
class SLLNode():
    def __init__(self, val):
        self.value = val
        self.next = None

def remove_duplicates(head):
    # Input validations
    cur_node = head
    while cur_node:
        next_distinct_node = cur_node.next
        while next_distinct_node and cur_node.value == next_distinct_node.value:
            next_distinct_node = next_distinct_node.next
        
        cur_node.next = next_distinct_node
        cur_node = cur_node.next

    return head