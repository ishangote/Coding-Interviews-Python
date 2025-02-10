# 875. Koko Eating Bananas

## Problem Statement

> Koko loves to eat bananas. There are `n` piles of bananas, the ith pile has `piles[i]` bananas. The guards have gone and will come back in `h` hours.
>
> Koko can decide her bananas-per-hour eating speed of `k`. Each hour, she chooses some pile of bananas and eats `k` bananas from that pile. If the pile has less than `k` bananas, she eats all of them instead and will not eat any more bananas during this hour.
>
> Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.
>
> Return the minimum integer `k` such that she can eat all the bananas within `h` hours.

> Constraints:
>
> - 1 <= piles.length <= 10<sup>4</sup>
> - piles.length <= h <= 10<sup>9</sup>
> - 1 <= piles[i] <= 10<sup>9</sup>

## Examples

Example 1:

```
Input: piles = [3,6,7,11], h = 8
Output: 4
```

Example 2:

```
Input: piles = [30,11,23,4,20], h = 5
Output: 30
```

Example 3:

```
Input: piles = [30,11,23,4,20], h = 6
Output: 23
```

## Binary Search Solution

```
Input:
h = 8
piles =
 0  1  2  3
[3, 6, 7, 11]

* Important constraint piles.length <= h <= 10^9
* To finish each pile in exactly one hour, Koko will need speed of max(piles)
* k is bound by [1, 11], we should minimize it s.t Koko eats all bananas within h => Binary Search


k =
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
 l                              h
                k

          piles =
          [3, 6, 7, 11]
hours ->   1  1  2  2   -> 6 < h (8)
to
consume
pile
(pile/k)


k =
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
 l              h
       k

          piles =
          [3, 6, 7, 11]
hours ->   1  2  3  4  -> 10 > h (8)
to
consume
pile


k =
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
          l     h
             k

          piles =
          [3, 6, 7, 11]
hours ->   1  2  2  3  -> 8 == h (8)
to
consume
pile


k =
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
          l
             h
          k

          piles =
          [3, 6, 7, 11]
hours ->   1  2  2  3  -> 8 == h (8)
to
consume
pile

Output: 4
```
