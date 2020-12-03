# Return True if SLL is Palindorm else False => O(n) space
"""
Questions:
1. Is input a singly linked list? Yes
2. If head == None? return True
3. If head.next == None? return True
4. Can input be manipulated inplace? Yes

Examples:
Even Case
1 -> 2 -> 2 -> 1
              i
length = 4
iterate (length // 2) times and store on stack
start iterating immediately 
stack = []
if not stack: return True

Odd case
1 -> 2 -> 3 -> 2 -> 1
length = 5
start iterating from mid + 1 
stack = []
if not stack: return True

Time: O(n + n) ~ O(n) where n is number of nodes
Space: O(n)

-----------------------------
Find mid => 
Even case
1 -> 2 -> 2 -> 1 -> None
          s  
                    f 
                    
Reverse second half and compare

1 -> 2   1 -> 2 -> None
l1       l2

                    
Odd case
1 -> 2 -> 3    1 -> 2 -> None
l1             l2   

Time: ~O(n)
Space: O(1)
"""
from sll import make_list
def are_equal_lists(l1, l2):
    while l2:
        if l2.val != l1.val: return False
        l1 = l1.next
        l2 = l2.next
    return True

def reverse_sll(head):
    prev, cur = None, head
    while cur:
        tmp = cur.next
        cur.next = prev
        prev = cur
        cur = tmp
    return prev

def get_mid(head):
    slow, fast = head, head
    while fast and fast.next: 
        slow, fast = slow.next, fast.next.next
    if not fast: return slow
    return slow.next
    
def is_palindrome(head):
    if not head or not head.next: return True
    mid = get_mid(head)
    second_half = reverse_sll(mid)
    return are_equal_lists(head, second_half)

if __name__ == "__main__":
    n = int(input("Enter number of nodes: ")) 
    nums = list(map(int, input("Enter the values: ").strip().split()))
    ll = make_list(nums)
    print("Is Palindrome? " + str(is_palindrome(ll)))