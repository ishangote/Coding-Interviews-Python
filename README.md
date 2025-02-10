# Coding Interviews Prep

> This repository is a collection of solutions to coding problems sourced from platforms like Leetcode, InterviewBit, Pramp, and more. It serves as a comprehensive resource to systematically prepare for coding interviews, providing clean, well-documented solutions and patterns that frequently appear in technical interviews.
>
> The solutions are designed to improve problem-solving skills and familiarity with common coding challenges, covering topics such as algorithms, data structures, system design, and optimization techniques.

## MMR (Minimum Memory Requirement)

> This section focuses on critical code snippets with syntax that can be easily forgotten under pressure during interviews. By memorizing these minimal yet essential patterns, you can avoid small syntactic mistakes and speed up implementation during coding challenges.

#### ASCII Letters

```
UPPER CASE LETTERS                  LOWER CASE LETTERS
A → 65                              a → 97
B → 66                              b → 98
C → 67                              c → 99
D → 68                              d → 100
E → 69                              e → 101
F → 70                              f → 102
G → 71                              g → 103
H → 72                              h → 104
I → 73                              i → 105
J → 74                              j → 106
K → 75                              k → 107
L → 76                              l → 108
M → 77                              m → 109
N → 78                              n → 110
O → 79                              o → 111
P → 80                              p → 112
Q → 81                              q → 113
R → 82                              r → 114
S → 83                              s → 115
T → 84                              t → 116
U → 85                              u → 117
V → 86                              v → 118
W → 87                              w → 119
X → 88                              x → 120
Y → 89                              y → 121
Z → 90                              z → 122
```

- To find ASCII value of uppercase from ASCII value of lowercase: `uppercase_ascii = lowercase_ascii - 32`
- To find ASCII value of lowercase from ASCII value of uppercase: `lowercase_ascii = uppercase_ascii + 32`

#### Binary Numbers

```
0       0000

1       0001

          * (MSB)
2       0010
3       0011

         *
4       0100
5       0101
6       0110
7       0111

        *
8       1000
9       1001
...

Note:
- Most significant bit shifts at numbers [1, 2, 4, 8, 16, 32...]
- The remaining bits to the right repeat with the above offsets
```

#### Intrinsic String Methods:

- `isalnum()`: Returns True if all characters are alphanumeric (letters and digits).

```
"abc123".isalnum() # True
```

- `isalpha()`: Returns True if all characters are alphabetic (letters only).

```
"abc".isalpha() # True
```

- `isdigit()`: Returns True if all characters are digits. (Works only for positive numbers)

```
"123".isdigit() # True
```

- `strip("-").isdigit()`: Returns True if all characters are digits (Works for both positive and negative numbers)

```
"-4".strip("-").isdigit() # True
```

- `islower()`: Returns True if all cased characters are lowercase.

```
"abc".islower() # True
```

- `lower()`: Converts a character or string to lowercase.

```
'A'.lower()  # 'a'
```

- `isupper()`: Returns True if all cased characters are uppercase.

```
"ABC".isupper() # True
```

- `upper()`: Converts a character or string to uppercase.

```
'a'.upper()  # 'A'
```

- `istitle()`: Returns True if the string follows title case (first letter of each word is capitalized).

```
"Hello World".istitle() # True
```

- `isspace()`: Returns True if all characters are whitespace.

```
" ".isspace() # True
```

- `isdecimal()`: Returns True if all characters are decimal characters (0-9, used in digit-based numbers).

```
"123".isdecimal() # True
```

- `isnumeric()`: Returns True if all characters are numeric (includes digits and characters like fractions).

```
"½".isnumeric()  # True
```

- `isascii()`: Returns True if all characters are ASCII (in the range of 0-127).

```
"abc123".isascii()  # True
```

#### `string` Module

`import string`

- `string.ascii_letters`: Concatenation of lowercase and uppercase letters. ('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
- `string.ascii_lowercase`: Lowercase letters ('abcdefghijklmnopqrstuvwxyz').
- `string.ascii_uppercase`: Uppercase letters ('ABCDEFGHIJKLMNOPQRSTUVWXYZ').
- `string.digits`: The digits '0123456789'.
- `string.hexdigits`: Hexadecimal digits ('0123456789abcdefABCDEF').
- `string.octdigits`: Octal digits ('01234567').
- `string.punctuation`: String of punctuation characters.
- `string.printable`: Combination of digits, letters, punctuation, and whitespace.
- `string.whitespace`: Characters considered as whitespace.

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

#### Most Frequent Key Based on Value in Python Dictionary (Shorthand)

1. Single Most Frequent Key

```
most_frequent_key = max(my_dict, key=my_dict.get)
```

2. All Keys with Maximum Value

```
most_frequent_keys = [k for k, v in my_dict.items() if v == max(my_dict.values())]
```

#### Python 3 Division Operators

1. True Division (/): Always returns a float, even for integer operands.

```
Example:
print(5 / 2) # 2.5
print(-5 / 2) # -2.5 (No rounding towards 0)
```

2. Floor Division (//): Rounds down (towards negative infinity).

```
Example:
print(5 // 2) # 2
print(-5 // 2) # -3 (Not -2)
```

3. `math.ceil` Rounding Towards positive infinity

```
math.ceil(5 / 2)  # Output: 3
math.ceil(-5 / 2)  # Output: -2
```

4. Rounding Towards Zero: Use int() to truncate instead of floor rounding.

```
Example:
print(int(5 / 2)) # 2
print(int(-5 / 2)) # -2
```

#### Custom Sorting Intervals:

```
def custom_sort(intervals):
    return sorted(intervals, key=lambda x: x[0])

# Example usage
sorted_intervals = custom_sort([[7, 10], [2, 4]])
print(sorted_intervals)
# Output: [[2, 4], [7, 10]]
```

#### Summary of Monotonic Stack Behavior:

```

Problem          |  Traversal Direction  |   Stack
-------------------------------------------------------
Next Greater     |  Left to Right        |   Decreasing
Previous Greater |  Right to Left        |   Decreasing
Next Smaller     |  Left to Right        |   Increasing
Previous Smaller |  Right to Left        |   Increasing
```

#### Subarrays vs Subsequences

- Subarray: Contiguous portion of an array.

  - Example: [1, 2, 3] → [1], [1, 2], [2, 3], etc.
  - Count: n \* (n + 1) / 2.

- Subsequence: Sequence from the array by deleting any number of elements while maintaining order.

  - Example: [1, 2, 3] → [1], [2], [1, 3], etc.
  - Count: 2^n.

```
def compute_subarrays(nums):
    return [nums[i:j+1] for i in range(len(nums)) for j in range(i, len(nums))]

-----------------------------------------------------------------------------

from itertools import combinations
def compute_subsequences(nums):
    return [list(comb) for i in range(len(nums)+1) for comb in combinations(nums, i)]
```

#### Zip Method

```
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
zipped = zip(list1, list2)
print(list(zipped)) # Output: [(1, 'a'), (2, 'b'), (3, 'c')]

list1 = ["cat", "dog", "dog"]
my_string = "abb"
zipped = zip(list1, my_string)
print(list(zipped)) # Output: [("cat", 'a'), ("dog", 'b'), ("dog", 'c')]

list1 = [1, 2, 3]
list2 = ['a', 'b']
zipped = zip(list1, list2)
print(list(zipped)) # Output: [(1, 'a'), (2, 'b')]

tuple1 = (1, 2, 3)
tuple2 = ('a', 'b', 'c')
zipped = zip(tuple1, tuple2)
print(list(zipped)) # Output: [(1, 'a'), (2, 'b'), (3, 'c')]
```

#### Character Frequency Counting Using a Fixed-Size Array

When dealing with problems where characters are strictly lowercase ('a'-'z') or strictly uppercase ('A'-'Z'), we can efficiently count occurrences using a fixed-size array of length 26.

```
# Lowercase Letters ('a'-'z'):
counts = [0] * 26
for char in s:
    counts[ord(char) - ord('a')] += 1
```

```
# Uppercase Letters ('A'-'Z')
counts = [0] * 26
for char in s:
    counts[ord(char) - ord('A')] += 1
```

This technique ensures O(1) space and O(n) time complexity, making it optimal for frequency-based string problems

#### Check for Overlapping Intervals

Two intervals overlap if:

1. The start of one interval is less than the end of the other.
2. This condition needs to be true for both intervals.

Condition: Two intervals `[start1, end1)` and `[start2, end2)` overlap if: `start1 < end2 and start2 < end1`

```
def is_overlapping(current, given):
    return current[0] < given[1] and given[0] < current[1]
```

#### Random Library in Python

```
import random

# Selecting a Random Element from a List:
random_item = random.choice(my_list)

# Generating a Random Integer Between Two Values (Inclusive):
random_int = random.randint(a, b)

# Shuffling a List in Place:
random.shuffle(my_list)

# Generating a Random Float Between 0 and 1:
random_float = random.random()
```

#### Counter Module

```
from collections import Counter

my_list = [1, 2, 3, 2, 1, 4, 5, 1]
counter = Counter(my_list)
=> Counter({1: 3, 2: 2, 3: 1, 4: 1, 5: 1})

my_string = "hello world"
counter = Counter(my_string)
=> Counter({'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1})

my_tuple = (1, 2, 3, 1, 2)
counter = Counter(my_tuple)
=> Counter({1: 2, 2: 2, 3: 1})
```

#### SortedList in Python (`sortedcontainers` Library)

SortedList is a dynamically sorted list that maintains order automatically and supports fast insertions, deletions, and lookups.

Key Operations & Time Complexity

- Insert (`add`): `O(log n)`
- Delete (`remove`): `O(log n)`
- Indexing (`sl[i]`): `O(1)`

```
from sortedcontainers import SortedList

> sl = SortedList([5, 3, 8, 1])
> sl.add(4) # Inserts 4 in sorted order
> sl.remove(3) # Removes 3
> print(sl[0]) # Output: 1 (smallest)
> print(sl[-1]) # Output: 8 (largest)
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
