"""
Questions:
1. Can there be duplicates? yes
2. If duplicates then ans should contain them? yes
3. array size >= 3? yes
4. Can not sort the input array? yes

Examples:
input = 
[-3, 2, -1, 1, -4, 7, 1]
                      ^
ans =
[1, 2, 7]

min_heap = [1, 2, 7]
"""
import heapq
def findThreeLargestNumbers(array):
    min_heap = []
        
    for num in array:
        heapq.heappush(min_heap, num)
        if len(min_heap) > 3: heapq.heappop(min_heap)
    # Do not return min_heap -> It is not necessarily sorted
    ans = []
    while min_heap:
        ans.append(heapq.heappop(min_heap))

    return ans

"""
Time: O(nlog3) ~ O(n), n => length of input array
Space: O(3) ~ O(1)
"""
