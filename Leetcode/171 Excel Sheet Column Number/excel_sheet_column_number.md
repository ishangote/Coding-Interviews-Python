# 171. Excel Sheet Column Number

## Problem Statement

> Given a string columnTitle that represents the column title as appears in an Excel sheet, return its corresponding column number.
>
> For example:
>
> ```
> A -> 1
> B -> 2
> C -> 3
> ...v
> Z -> 26
> AA -> 27
> AB -> 28
> ...
> ```

> Constraints:
>
> - 1 <= columnTitle.length <= 7
> - columnTitle consists only of uppercase English letters.
> - columnTitle is in the range ["A", "FXSHRXW"].

## Examples

Example 1:

```
Input: columnTitle = "A"
Output: 1
```

Example 2:

```
Input: columnTitle = "AB"
Output: 28
```

Example 3:

```
Input: columnTitle = "ZY"
Output: 701
```

## Solution

**Intuition**

- How do we convert hexadecimal numbers to decimal?
  - 0xA9 => A x 16<sup>1</sup> + 9 x 16<sup>0</sup>
  - A is represented as 10 in hex
  - Hence => 10 x 16<sup>1</sup> + 9 x 16<sup>0</sup> = 169
- This problem becomes converting base 26 to decimal
  - Hence the map looks like
    - ` {A: 1, ... Z: 26, AA: 27, ... AZ: 52}` i.e blocks of 26
    - and the next number (53) would be "BZ" (similar to numbers; for example next number of 19 is 20 => 9 gets set back to 0 and 1 is incremented)
    - So each position has 26 possible characters

**Algorithm**

- Initialize `res = 0`, `position = 0`
- Iterate backwards in column_title: `char`
  - `res = res + character_map[char] * (26 ** position)`
  - Increment `position`
- Return `res`

## References

- [Youtube](https://www.youtube.com/watch?v=g-l4UpF62x0&t=138s&ab_channel=KnowledgeCenter)
