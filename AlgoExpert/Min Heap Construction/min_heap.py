"""
Min heap => complete binary tree where root is always smaller than children

                 8
               /   \
              12    23
             /  \   / \
            17  31 30  44
           / \
        102   18

Rules:
array representation => [8, 12, 23, 17, 31, 30, 44, 102, 18]
cur_node at i then,
child1 at 2i + 1
child2 at 2i + 2
parent at floot((i - 1) / 2)

Methods:
1. Insert: Time: O(logn)
    1.1 Sift Up: O(logn), n => number of values in the min_heap
    eg:
    insert(9)
     0  1   2   3   4   5   6   7    8   9
    [8, 12, 23, 17, 31, 30, 44, 102, 18, 9]
                    p                    ^

     0  1   2   3   4   5   6   7    8   9
    [8, 12, 23, 17, 9, 30, 44, 102, 18, 31]
        p           ^

     0  1  2   3   4   5   6   7    8   9
    [8, 9, 23, 17, 12, 30, 44, 102, 18, 31]
     p  ^

     p < ^ : hence stop sift up

2. Remove: Time: O(logn)
    2.1 Sift Down: Time: O(logn), n => number of values in the min_heap

    eg: 
    remove(8)
    
     0  1  2   3   4   5   6   7    8   9
    [8, 9, 23, 17, 12, 30, 44, 102, 18, 31]
     ^
    Swap with last element and pop ->
     0   1  2   3   4   5   6   7    8  
    [31, 9, 23, 17, 12, 30, 44, 102, 18]
     ^   c1 c2

    Swap with smaller child
     0   1  2   3   4   5   6   7    8  
    [9, 31, 23, 17, 12, 30, 44, 102, 18]
        ^       c1  c2

    Swap with smaller child
     0  1   2   3   4   5   6   7    8  
    [9, 12, 23, 17, 31, 30, 44, 102, 18]
                    ^                    c1  c2
    
    ^ > c1 and ^ > c2: hence stop sift down
    
3. Build Heap: Time: O(n)
    From fitst parent i.e 
"""
# Space: O(1) for all methods
class MinHeap:
    def __init__(self, array):
        self.heap = self.build_heap(array)
    
    # Time: O(logn)
    def sift_up(self, cur_idx, heap):
        parent_idx = (cur_idx - 1) // 2
        while cur_idx > 0 and heap[cur_idx] < heap[parent_idx]:
            self.swap(cur_idx, parent_idx, heap)
            cur_idx = parent_idx
            parent_idx = (cur_idx - 1) // 2

    # Time: O(logn)
    def sift_down(self, cur_idx, end_idx, heap):
        child1_idx = cur_idx * 2 + 1
        while child1_idx <= end_idx:
            child2_idx = cur_idx * 2 + 2 if cur_idx * 2 + 2 <= end_idx else -1
            if child2_idx != -1 and heap[child2_idx] < heap[child1_idx]: 
                idx_to_swap = child2_idx
            else:
                idx_to_swap = child1_idx
            
            if heap[idx_to_swap] < heap[cur_idx]: 
                self.swap(cur_idx, idx_to_swap, heap)
                cur_idx = idx_to_swap
                child1_idx = 2 * cur_idx + 1
            
            else: break
    
    # Time: O(n)
    def build_heap(self, array):
        first_parent_idx = (len(array) - 2) // 2
        
        for cur_idx in reversed(range(first_parent_idx + 1)):
            self.sift_down(cur_idx, len(array) - 1, array)
        
        return array
    
    # Time: O(logn)
    def insert(self, value):
        self.heap.append(value)
        self.sift_up(len(self.heap) - 1, self.heap)
    
    # Time: O(logn)
    def remove(self):
        self.swap(0, len(self.heap) - 1, self.heap)
        value = self.heap.pop()
        self.sift_down(0, len(self.heap) - 1, self.heap)
        return value
    
    # Time: O(1)
    def peek(self):
        return self.heap[0]
    
    # Time: O(1)
    def swap(self, i, j, heap):
        heap[i], heap[j] = heap[j], heap[i]