# 398. Random Pick Index

## Problem Statement

> Given an integer array nums with possible duplicates, randomly output the index of a given target number. You can assume that the given target number must exist in the array.
>
> Implement the Solution class:
>
> - Solution(int[] nums) Initializes the object with the array nums.
> - int pick(int target) Picks a random index i from nums where nums[i] == target. If there are multiple valid i's, then each index should have an equal probability of returning.

> Constraints:
>
> - 1 <= nums.length <= 2 \* 10<sup>4</sup>
> - -2<sup>31</sup> <= nums[i] <= 2<sup>31</sup> - 1
> - target is an integer from nums.
> - At most 10<sup>4</sup> calls will be made to pick.

## Examples

Example 1:

```
Input
["Solution", "pick", "pick", "pick"]
[[[1, 2, 3, 3, 3]], [3], [1], [3]]
Output
[null, 4, 0, 2]

Explanation
Solution solution = new Solution([1, 2, 3, 3, 3]);
solution.pick(3); // It should return either index 2, 3, or 4 randomly. Each index should have equal probability of returning.
solution.pick(1); // It should return 0. Since in the array only nums[0] is equal to 1.
solution.pick(3); // It should return either index 2, 3, or 4 randomly. Each index should have equal probability of returning.
```

## Brute Force Solution

```
        0  1  2  3  4
nums = [1, 2, 3, 3, 3]

hm = {
    1: [0]
    2: [1]
    3: [2, 3, 4]
}

return random.choice(hm[target])

Time: O(n)
Space: O(n)
```

## Reservoir Sampling Solution

For this problem, we can use a variation of Reservoir Sampling because we only need one sample from a known list of indices that match the target. Here's the approach:

Iterate through the array and keep track of each index where nums[i] == target.
Select the target index with equal probability by adjusting the selection process as we find new matches.
For each matching index, with a probability of (1 / count of matches so far), we replace the previously selected index. This way, each index has an equal chance of being the result.

## Syntax

- Selecting a Random Element from a List: `random_item = random.choice(my_list)`

## References

- https://www.youtube.com/watch?v=paCJBO-yi9Q&ab_channel=CodingwithMinmer
