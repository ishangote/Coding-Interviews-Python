# Reverse a singly linked list

"""
Questions:
1. Is it a singly linked list? Yes

Examples:

input
h
1 -> 2 -> 3 -> None
output
None <- 1 <- 2 <- 3
                  h

1 -> 2 -> 3 -> None
c    t
prev = None

Logic:
tmp = c.next
cur.next = prev
prev = cur
cur = tmp

Time: O(n) n is number of nodes
Space: O(1)

"""
from sll import make_list, print_list
def reverse_sll(head):
    if not head: return None
    prev, cur = None, head
    
    while cur:
        tmp = cur.next
        cur.next = prev
        prev = cur
        cur = tmp
    
    return prev

if __name__ == "__main__":
    # number of elements 
    n = int(input("Enter number of nodes: ")) 
    # Below line read inputs from user using map() function  
    nums = list(map(int, input("Enter the values : ").strip().split()))[:n]
    head = make_list(nums)

    print("Original List: " + str(print_list(head)))
    print("Reversed List: " + str(print_list(reverse_sll(head))))