'''
Given the list of IDs, which contains many duplicate integers and one unique integer, find the unique integer.

 0   1  2  3  4
[12, 3, 4, 3, 12]


[3, 3, 3, 4, 12]
          ^
 ans = 4
              
 ans= set() ={}

 to check if num has occured before      
              
 hash_map = {
 12: 2
 3: 2
 4: 1
 }
 
XOR
0 1 1
1 0 1
1 1 0
0 0 0
 
[12,3,4,3]
 ^


'''

from collections import Counter
def get_unique(ids):
    
    count_map = Counter(ids)
    for id in count_map: 
        if count_map[id] != 1: continue
        return id 
   return 0

# Even number of duplicates
def get_unique_xor(ids):
    
    ans = 0
    for id in ids:
        ans = ans ^ id
    
    return ans
    
 
 """
 #Pairs Duplicates
 In           expected        Actual
 []             0              0      
 [1]            1              1
 [2, 2]         0              0
 [2, 3, 2]      3              3
 
 
 """
        
    
   
              
        
"""
In            Expected            Actual
[]             0                   0
[1]            1                   1

[2, 3, 2]      3                   3

[2, 2]         0                  0

[12,3,4,3,12]  4                   4


{
12:2
3:2
4:1
}
"""