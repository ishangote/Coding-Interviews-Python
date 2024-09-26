# 292. Nim Game

## Problem Statement

> You are playing the following Nim Game with your friend:

> - Initially, there is a heap of stones on the table.
> - You and your friend will alternate taking turns, and you go first.
> - On each turn, the person whose turn it is will remove 1 to 3 stones from the heap.
> - The one who removes the last stone is the winner.
> - Given n, the number of stones in the heap, return true if you can win the game assuming both you and your friend play optimally, otherwise return false.

> Constraints:
>
> - 1 <= n <= 2<sup>31</sup> - 1

## Examples

Example 1:

```
Input: n = 4
Output: false
Explanation: These are the possible outcomes:

1. You remove 1 stone. Your friend removes 3 stones, including the last stone. Your friend wins.
2. You remove 2 stones. Your friend removes 2 stones, including the last stone. Your friend wins.
3. You remove 3 stones. Your friend removes the last stone. Your friend wins.
   In all outcomes, your friend wins.
```

Example 2:

```
Input: n = 1
Output: true
```

Example 3:

```
Input: n = 2
Output: true
```

## Brute Force Solution

```
Input:
n = 4

                    8 * [my_turn = True, win = False]
                /   |   \
               7    6    5


                    8
                /   |   \
               7    6    5 * [my_turn = False, win = False]

                                                    8
                                                /   |   \
              [my_turn = False, win = False] * 7    6    5


                    8
                /   |   \
               7    6    5
                    *
        [my_turn = False, win = False]

                  8
        /         |         \
       7          6          5
     / | \      / | \      / | \
    6  5  4    5  4  3    4  3  2
    *  *  *    *  *  *    *  *  *  [my_turn = True, win = False]


                  8
        /         |         \
       7          6          5
     / | \      / | \      / | \
    6  5  4    5  4  3    4  3  2
   /|\              /|\        /|
  5 6 3 ...        2 1 0      1 0
                       *        * [my_turn = False, win = True]


* Base Conditions:
* If it's your turn and n == 0, you lose. If it's opponent's turn, they lose.
if n == 0 and not my_turn: return True
if n == 0 and my_turn: return False

Output:
False
```

## Optimized Solution

```
n = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12...]
r = [w, w, w, l, w, w, w, l, w, w,  w,  l...]   * win/loss

Pattern:
if n % 4 == 0: Loss
else: Win



```
