# 168. Excel Sheet Column Title

## Problem Statement

> Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.
> For example:
>
> ```
> A -> 1
> B -> 2
> C -> 3
> ...
> Z -> 26
> AA -> 27
> AB -> 28
> ...
> ```

> Constraints:
>
> - 1 <= columnNumber <= 231 - 1

## Examples

Example 1:

```
Input: columnNumber = 1
Output: "A"
```

Example 2:

```
Input: columnNumber = 28
Output: "AB"
```

Example 3:

```
Input: columnNumber = 701
Output: "ZY"
```

## Solution

```

1: A        |
2: B        |
3: C        |   * 26 combinations for one character
...         |
26: Z       |


27: AA      |
28: AB      |
29: AC      |
...         |
52: AZ      |       * 26 x 26 combinations for 2 characters = 676
53: BA      |
54: BB      |
55: BC      |
...         |
78: BZ      |
...         |


* The last character is iterates from from A -> Z in any of the above zone while,
* the previous characters  remain constant. For example: AAA, AAB, AAC, ...

* Hence, The last character in the column name can be determined by n % 26.
* For example: n = 53 => 53 % 26 = 1 (i.e "A") result will look like "_ _ ... A"

* Now, for previous characters...
* Once the last character gets filled. The total combinations get divided by 26. Hence, the next column number to compute must be
* 53 // 26 = 2 => (i.e "B")


Example:

Input
column_number = 701

n = 701
last_character = character_map[701 % 26] = character_map[25] = "Y"

n = n // 26 = 701 // 26 = 26
last_character = character_map[26 % 26] = character_map[0] => ERROR

* We need the character_map to start from index 0
* We need to subtract 1 from n and then take modulo to offset this case. i.e (n - 1) % 26

character_map = {
    0: A
    1: B
    2: C
    ...
    25: Z
}

n = 701
last_character = character_map[(701 - 1) % 26] = character_map[24] = "Y"

n = (n - 1) // 26 = 700 // 26 = 26
last_character = character_map[(26 - 1) % 26] = character_map[25] => "Z"

result is reversed => "ZY"
```

## References

[Youtube](https://www.youtube.com/watch?v=UcTKk2y_3s4&t=36s&ab_channel=KnowledgeCenter)
