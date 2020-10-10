"""
a = 
[1, 0, 0, 0, 1, 0]

alloc x:

"""
from collections import defaultdict
class MemoryAllocator:
    def __init__(self, mem):
        self.mem = mem
        self.alloc_count = 1
        self.ids = defaultdict(list)
    
    def alloc(self, size):
        