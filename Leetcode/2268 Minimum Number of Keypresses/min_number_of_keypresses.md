# 2268. Minimum Number of Keypresses

## Problem Statement

> You have a keypad with 9 buttons, numbered from 1 to 9, each mapped to lowercase English letters. You can choose which characters each button is matched to as long as:
>
> - All 26 lowercase English letters are mapped to.
> - Each character is mapped to by exactly 1 button.
> - Each button maps to at most 3 characters.
>
> To type the first character matched to a button, you press the button once. To type the second character, you press the button twice, and so on.
>
> Given a string s, return the minimum number of keypresses needed to type s using your keypad.
>
> Note that the characters mapped to by each button, and the order they are mapped in cannot be changed.

> Constraints:
>
> - 1 <= s.length <= 10<sup>5</sup>
> - s consists of lowercase English letters.

## Examples

Example 1:

![Example 1](https://assets.leetcode.com/uploads/2022/05/05/image-20220505184346-1.png)

```
Input: s = "apple"
Output: 5
Explanation: One optimal way to setup your keypad is shown above.
Type 'a' by pressing button 1 once.
Type 'p' by pressing button 6 once.
Type 'p' by pressing button 6 once.
Type 'l' by pressing button 5 once.
Type 'e' by pressing button 3 once.
A total of 5 button presses are needed, so return 5.
```

Example 2:

![Example 2](https://assets.leetcode.com/uploads/2022/05/05/image-20220505203823-1.png)

```
Input: s = "abcdefghijkl"
Output: 15
Explanation: One optimal way to setup your keypad is shown above.
The letters 'a' to 'i' can each be typed by pressing a button once.
Type 'j' by pressing button 1 twice.
Type 'k' by pressing button 2 twice.
Type 'l' by pressing button 3 twice.
A total of 15 button presses are needed, so return 15.
```

## Greedy Solution

```
s = "ababpqrmzzyxtlvq"

unique_chars_set = {a, b, p, q, r, m, z, y, x, t, l, v}

* First 9 chars can be mapped such that there is only 1 keypress to get them

chars_to_keypresses = {
    a: 1
    b: 1
    p: 1
    q: 1
    r: 1
    m: 1
    z: 1
    y: 1
    x: 1
    t: 2
    l: 2
    v: 2
    ...
    next 9 unique chars will have keypresses of 2
    ...
    next 9 unique chars will have keypresses of 3
}


* However, if we have char "v" being pressed n times then for each v we would need 2 keypresses. This is not optimal.
* Idea: Always make the letters with higher frequency to be easier accessible.

```

```
s = "abbzzydqqzcab"

sorted_char_count = {
    b: 3        *  keypresses = 3 * 1
    z: 3        *  keypresses = 3 * 1
    a: 2        *  keypresses = 2 * 1
    q: 2        *  keypresses = 2 * 1
    y: 1        *  keypresses = 1 * 1
    d: 1        *  keypresses = 1 * 1
    c: 1        *  keypresses = 1 * 1
    t: 1        *  keypresses = 1 * 1
    m: 1        *  keypresses = 1 * 1
    n: 1        *  keypresses = 1 * 2
                              ... * 2

}

* Iterate over sorted_char_count while maintaining the keypresses required:
    count * (1 or 2 or 3) depending on current keypresses


0 - 9 => keypresses = 1
9 - 18 => keypresses = 2
18 - 25 => keypresses = 3
```
