# 604. Design Compressed String Iterator

## Problem Statement

> Design and implement a data structure for a compressed string iterator. The given compressed string will be in the form of each letter followed by a positive integer representing the number of this letter existing in the original uncompressed string.

> Implement the StringIterator class:
>
> - next() Returns the next character if the original string still has uncompressed characters, otherwise returns a white space.
> - hasNext() Returns true if there is any letter needs to be uncompressed in the original string, otherwise returns false.

> Constraints:
>
> - 1 <= compressedString.length <= 1000
> - compressedString consists of lower-case an upper-case English letters and digits.
> - The number of a single character repetitions in compressedString is in the range [1, 10<sup>9</sup>]
> - At most 100 calls will be made to next and hasNext.

## Examples

Example 1:

```
Input
["StringIterator", "next", "next", "next", "next", "next", "next", "hasNext", "next", "hasNext"]
[["L1e2t1C1o1d1e1"], [], [], [], [], [], [], [], [], []]
Output
[null, "L", "e", "e", "t", "C", "o", true, "d", true]

Explanation
StringIterator stringIterator = new StringIterator("L1e2t1C1o1d1e1");
stringIterator.next(); // return "L"
stringIterator.next(); // return "e"
stringIterator.next(); // return "e"
stringIterator.next(); // return "t"
stringIterator.next(); // return "C"
stringIterator.next(); // return "o"
stringIterator.hasNext(); // return True
stringIterator.next(); // return "d"
stringIterator.hasNext(); // return True
```

## Brute Force Solution

```
input_string =
"L1e2t1C1o1d1e1"
stack = []
itr = 0

=> next()

input_string =
"L1e2t1C1o1d1e1"
 ^
   ^
stack = [L] => []   * return L
itr = 0 => 0 + 2 = 2


input_string =
"L1e2t1C1o1d1e1"
   ^
stack = []
itr = 2

=> next()

input_string =
"L1e2t1C1o1d1e1"
     ^
stack = [e, e] => [e]
itr = 4
...

```

## Space Optimized Solution

```
input_string =
"L1e1234t1C1o1d1e1"
itr = -1
count = 0
cur_char = ""

next() =>

input_string =
"L1e1234t1C1o1d1e1"
 ^
itr = 1
count = 1
cur_char "L"

return L


input_string =
"L1e1234t1C1o1d1e1"
   ^
itr = 2
cur_char = 2
cur_char_count = 1

...

```
