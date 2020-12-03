"""
Questions:
1. Singly linked lists? Yes
2. l1 Null? return l2 , l2 Null? return l1, l1 & l2 Null? return Null
3. list vals real nums? Yes

Examples:
             l1
-1 -> 2 -> 7
                    l2
-2 -> 1 -> 3 -> 5 -> 8

dummy -> -2 -> -1 -> 1 -> 2 -> 3 -> 5 -> 7 -> 8

Time: O(n + m)
n => number of nodes in l1
m => number of nodes in l2
Space: O(1)
"""            
from sll import make_list, print_list, SLLNode
def merge_lists(l1, l2):
    dummy = cur = SLLNode("dummy")
        
    while l1 and l2:
        if l1.val <= l2.val:
            cur.next = l1
            l1 = l1.next
        else:
            cur.next = l2
            l2 = l2.next
        cur = cur.next
        
    cur.next = l1 if l1 else l2
    
    return dummy.next

if __name__ == "__main__":
    # number of elements 
    n = int(input("Enter number of nodes in l1: ")) 
    # Below line read inputs from user using map() function  
    nums1 = list(map(int, input("Enter the numbers : ").strip().split()))
    print(nums1)
    l1 = make_list(nums1)

    # number of elements 
    m = int(input("\nEnter number of nodes in l2: ")) 
    # Below line read inputs from user using map() function  
    nums2 = list(map(int, input("Enter the numbers : ").strip().split()))
    print(nums2)
    l2 = make_list(nums2)

    print("Merged Lists: " + str(print_list(merge_lists(l1, l2))))