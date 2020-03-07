"""
1 -> 8 -> 3  # 123              183
4 -> 5       #  45               45
                                228
1 -> 6 -> 8  # 168

carry = 1
3 -> 8 -> 1
^
5 -> 4
^

8 -> 2 -> 2

  1
99
1
00
    None<-1 <-2 <- 3     1 <- 2 <- 3   
                     ^
tmp = None
prev = 3

"""

class SLLNode:
    def _init_(self, val):
        self.val = val
        self.next = None


def reverse_sll(head):
    #Reverse List
    if not head: return None
    runner = head
    prev = None
    
    while runner:
        tmp = runner.next
        runner.next = prev
        prev = runner
        runner = tmp
    
    return prev
    
"""
Input       Expected op         Actual op
None        None                None

1->2        2                   2

None<-1<-2
        

runner = None
prev = 2
tmp = None


O(n)    n   -> len of sll
O(1)    

"""
    
def add_two_sll(l1, l2):
    if not l1: return l2
    if not l2: return l1
    
    l1 = reverse_sll(l1)
    l2 = reverse_sll(l2)
    
    dummy = ans = SLLNode('dummy')
    carry = 0
    
    while l1 or l2:
        tmp = 0
        if l1:
            tmp += l1.val
            l1 = l1.next
        if l2:
            tmp += l2.val
            l2 = l2.next
            
        ans.next = SLLNode((tmp + carry) % 10)
        carry = (tmp + carry) // 10
        
        ans = ans.next
        
        if not l1 and not l2 and carry:
            ans.next = SLLNode(carry)
            
    return reverse_sll(dummy.next)
    
    
"""
Input       Expected OP     Actual OP
l1 None     l1              l1
9->9 -> 1   1->0->0         reverse(0 -> 0 -> 1)

tmp = 9 + 1 % 10 = 0 

carry = 1

10

O(n)    n ->length of larger sll
O(n)    n -> 1 + len of larger sll
"""