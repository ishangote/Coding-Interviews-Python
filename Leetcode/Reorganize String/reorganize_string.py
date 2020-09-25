"""
Given a string S, check if the letters can be rearranged so that two characters that are adjacent to each other are not the same.

If possible, output any possible result.  If not possible, return the empty string.

Example 1:

Input: S = "aab"
Output: "aba"
Example 2:

Input: S = "aaab"
Output: ""

aab -> aab, aba, baa

abba -> abba, abab, baba, aabb, bbaa, baab

sort => aabb
                    ""
                a
            aa      ab
        aab             aba
    aabb    aabb            abab

0123
abab


aaaabbbcc

max_heap = 
a:4
b:3
c:2

max_heap.pop()
a:4
max_heap.pop()
b:3

cur = 
ab

max_heap.push(a:3)
max_heap.push(b:2)

max_heap.pop()
a:3
max_heap.pop()
b:2

cur = 
abab

max_heap.push(a:2)
max_heap.push(b:1)

max_heap.pop()
a:2
max_heap.pop()
c:2

cur = 
ababac

max_heap.push(a:1)
max_heap.push(c:1)


max_heap.pop()
a:1
max_heap.pop()
b:1

cur = 
ababacab

max_heap.pop()
c:1

cur = 
ababacabc

"""

import heapq
from collections import Counter
def reorganize_string(S):
    ch_count = Counter(S)
    
    if ch_count.most_common(1)[0][1] > (len(S) + 1) // 2: 
        return ""

    max_heap = []

    for (key, val) in ch_count.items():
        max_heap.append((-val, key))

    heapq.heapify(max_heap)

    ans = ""
    while len(max_heap) >= 2:
        
        cnt1, ch1 = heapq.heappop(max_heap)
        cnt2, ch2 = heapq.heappop(max_heap)
        
        if not ans: 
            
            ans += (ch1 + ch2)
        else:
            ans += (ch1 + ch2) if ch1 != ans[-1] else (ch2 + ch1)
            
        cnt1 += 1
        cnt2 += 1

        if cnt1 != 0: 
            
            heapq.heappush(max_heap, (cnt1, ch1))
        if cnt2 != 0: 
            heapq.heappush(max_heap, (cnt2, ch2))

    return ans + max_heap[0][1] if max_heap else ans