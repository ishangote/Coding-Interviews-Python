# Coding Interviews Prep

> This repository is a collection of solutions to coding problems sourced from platforms like Leetcode, InterviewBit, Pramp, and more. It serves as a comprehensive resource to systematically prepare for coding interviews, providing clean, well-documented solutions and patterns that frequently appear in technical interviews.
>
> The solutions are designed to improve problem-solving skills and familiarity with common coding challenges, covering topics such as algorithms, data structures, system design, and optimization techniques.

## MMR (Minimum Memory Requirement)

> This section focuses on critical code snippets with syntax that can be easily forgotten under pressure during interviews. By memorizing these minimal yet essential patterns, you can avoid small syntactic mistakes and speed up implementation during coding challenges.

#### f-strings

F-strings provide a way to format strings using embedded expressions, introduced in Python 3.6.

```
# Syntax:

f"some text {expression}"
```

```
# Basic Example:

name = "Alice"
age = 30
greeting = f"My name is {name} and I am {age} years old."
# Output: "My name is Alice and I am 30 years old."
```

```
# Formatting Numbers:

pi = 3.14159
formatted_pi = f"Pi to 2 decimal places: {pi:.2f}"
# Output: "Pi to 2 decimal places: 3.14"
```

```
# Padding

h = 5
m = 7
time = f"{h}:{m:02d}"
# Output: "5:07"

Breakdown of :02d:
0: Pads the number with leading zeros if it's less than 2 digits.
2: Specifies the total width (2 digits).
d: Stands for decimal, ensuring the value is treated as an integer.
```

#### `heapq` Module

```
import heapq

# Basic min-heap operations
heap = []
heapq.heappush(heap, 10)
heapq.heappush(heap, 1)
heapq.heappush(heap, 5)
smallest = heapq.heappop(heap)  # Pops the smallest

# Convert list to heap
data = [10, 5, 7, 9, 3]
heapq.heapify(data)

# Find n largest/smallest elements
largest = heapq.nlargest(3, data)
smallest = heapq.nsmallest(2, data)

# Max-heap simulation (store negatives)
max_heap = []
heapq.heappush(max_heap, -10)
largest = -heapq.heappop(max_heap)

# Merge sorted lists
merged = list(heapq.merge([1, 4, 7], [2, 5, 6], [3, 8, 9]))

# Priority queue (push with priority)
priority_queue = []
heapq.heappush(priority_queue, (2, "low"))
heapq.heappush(priority_queue, (1, "high"))
task = heapq.heappop(priority_queue)
```

#### `bin()` Function

The `bin()` function converts an integer to its binary representation as a **string**.

```
# Convert integer to binary
bin_rep = bin(10)  # '0b1010'

# Convert Back to Integer:
integer = int('1010', 2)  # 10
```

#### `ord()` Function

The ord() function converts a character into its numeric ASCII value. For example, `ord('a')` returns `97`.

#### `chr()` Function

The `chr()` function converts numeric value back to a character, returning the letter.

#### Custom Sorting Intervals:

```
def custom_sort(intervals):
    return sorted(intervals, key=lambda x: x[0])

# Example usage
sorted_intervals = custom_sort([[7, 10], [2, 4]])
print(sorted_intervals)
# Output: [[2, 4], [7, 10]]
```

#### Zip Method

```
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
zipped = zip(list1, list2)
print(list(zipped))  # Output: [(1, 'a'), (2, 'b'), (3, 'c')]


list1 = ["cat", "dog", "dog"]
my_string = "abb"
zipped = zip(list1, my_string)
print(list(zipped))  # Output: [("cat", 'a'), ("dog", 'b'), ("dog", 'c')]


list1 = [1, 2, 3]
list2 = ['a', 'b']
zipped = zip(list1, list2)
print(list(zipped))  # Output: [(1, 'a'), (2, 'b')]


tuple1 = (1, 2, 3)
tuple2 = ('a', 'b', 'c')
zipped = zip(tuple1, tuple2)
print(list(zipped))  # Output: [(1, 'a'), (2, 'b'), (3, 'c')]
```

#### Counter Module

```
from collections import Counter

my_list = [1, 2, 3, 2, 1, 4, 5, 1]
counter = Counter(my_list)
print(counter)  # Output: Counter({1: 3, 2: 2, 3: 1, 4: 1, 5: 1})

my_string = "hello world"
counter = Counter(my_string)
print(counter)  # Output: Counter({'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1})

my_tuple = (1, 2, 3, 1, 2)
counter = Counter(my_tuple)
print(counter)  # Output: Counter({1: 2, 2: 2, 3: 1})
```

#### Definition of Binary Tree Node

```
class BTNode:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value
```

#### Definition of Singly Linked List Node

```
class SLLNode:
    def __init__(self, value):
        self.next = None
        self.value = value
```

#### Definition of Doubly Linked List Node

```
class DLLNode:
    def __init__(self, value):
        self.prev = None
        self.next = None
        self.value = value
```

#### Unit Testing in Python3

```
import unittest

class TestSomething(unittest.TestCase):
    def test_some_function(self):
        self.assertEqual(some_function(input), expected_output)
```
