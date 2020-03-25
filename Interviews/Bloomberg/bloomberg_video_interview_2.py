# Question 1: Reverse Singly Linked List
"""
Test1:
Input: 'a'
Expected: 'a'
Actual: 'a'

T2
Input: 'abac'
Expected: 'b'
Actual: 'b'

hm = {
    a: 2
    b: 1
    c: 1
}
Actual: 
"""
    
"""
Input: None
O: None

I:    a -> b -> c -> d
                     ^
runner = None
tmp = None
prev = d

None<-a <- b <- c <- d  <- b <- c <- d
    
O:    d -> c -> b -> a

"""
class SLLNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        
def reverse_sll(head):
    #Input validations
    
    runner = head
    prev = None
    
    while runner:
        tmp = runner.next
        runner.next = prev
        prev = runner
        runner = tmp
        
    return prev 
        
def traverse(head):
    ans = []
    while head:
        ans.append(head.val)
        head = head.next
        
    return ans

import unittest
class TestReverseSLL(unittest.TestCase):
    def test_generic(self):
        a = SLLNode('a')
        b = SLLNode('b')
        a.next = b
        
        self.assertEqual(traverse(reverse_sll(a)), ['b', 'a'])

if __name__ == '__main__': unittest.main()
        
"""
Testing

T1: 
Input: None
Expected: None
Adctual: None

T1: 
Input: a
Expected: a
Adctual: None

T1: 
Input: a -> b
Expected: b
Adctual: b

"""

# Question 2: Scrabble
"""
C,R,B,A,X,Q,L #7 tiles

7*6*5
[C,R,B,A,A,Q,L]
 ^
        []
      /
     [C]
     /
    [CR]    
    /    \
    [CRB]   [CRA]
   /CRBA, CRBAA
list of all the valid English words <= 7 letters

[AXE, ...., CRAB, CABAL]

AXE, AXLE


        -
    A -> EOW = False
  X
E   L
      E -> TRUE
      
axe...le
"""

def is_valid_word(word):    #Return True if word found in Trie

def scrabble(word_list):
    
def backtrack(word_list, curr, ch_idx, ans):
    if len(curr) == 7: return curr
    if not is_valid_word(curr): return
    
    for i, ch in enumerate(word_list):
        if i != ch_idx: if curr += [word_list[i]]