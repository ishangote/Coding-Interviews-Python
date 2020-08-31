# Design a data structure that supports all following operations in average O(1) time.
# insert(val): Inserts an item val to the set if not already present.
# remove(val): Removes an item val from the set if present.
# getRandom: Returns a random element from current set of elements 
# (it's guaranteed that at least one element exists when this method is called). 
# Each element must have the same probability of being returned.

import random
class RandomSet:
    def __init__(self):
        self.hash_set = set()
    
    def insert(self, val):
        if val not in self.hash_set: 
            self.hash_set.add(val)
            return True
        return False

    def remove(self, val):
        if val in self.hash_set: 
            self.hash_set.remove(val)
            return True
        return False
        
    def get_random(self):
        if self.hash_set:
            return random.choice(tuple(self.hash_set))
        return False