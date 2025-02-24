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

#### How It Works

1. Initialize the Solution Class:

   - Store the given nums array.

2. Implement the pick(target) Method:
   - Iterate through nums and find all indices where nums[i] == target.
   - Use Reservoir Sampling to randomly select one of these indices while ensuring equal probability.

#### Correctness

1. Iterate through nums, tracking indices where nums[i] == target.
2. Use Reservoir Sampling:
   - When the first occurrence is found, store it.
   - When the second occurrence is found, replace the stored index with a probability of `1/2`
   - When the third occurrence is found, replace with probability `1/3`, and so on.
   - This ensures that each index with target is selected with equal probability.

Consider `nums = [1, 2, 3, 3, 3]`, and we call `pick(3)`. The goal is to randomly pick one of the indices `{2, 3, 4}` with equal probability.

Why Does This Work?

- The first occurrence of `3 (index 2)` is always chosen initially.
- The second occurrence of `3 (index 3)` has a `1/2` chance of replacing index 2.
- The third occurrence of `3 (index 4)` has a `1/3` chance of replacing whatever is stored.
- Thus, each index `{2, 3, 4}` has an equal probability of being picked in the end.
- The key is that `random.randint(1, count)` generates a uniformly random number from 1 to count.
- We check if the result is `1` —which happens with a probability of `1/count`.

## Variation: Pick K Numbers [Reservoir Sampling Solution]

#### How It Works

1. Initialize Reservoir: The first `k` elements of `self.nums` are added to `res`.
2. Replace with Probability: For each subsequent element at index idx:
   - Generate a random index `pick_idx` in the range `[0, idx]`.
   - If `pick_idx` is within the first `k` elements, replace `res[pick_idx]` with `self.nums[idx]`.

#### Correctness

- Every element has a `k / idx` chance of being included.
- Elements in the reservoir are replaced with the correct probability.
- Ensures uniform selection over the entire list.

#### Edge Cases

- You should handle edge case by checking if k > len(self.nums): return self.nums[:].

## Syntax

- Selecting a Random Element from a List: `random_item = random.choice(my_list)`
- Generating a Random Integer Between Two Values (Inclusive): `random_int = random.randint(a, b)`

## References

- https://www.youtube.com/watch?v=paCJBO-yi9Q&ab_channel=CodingwithMinmer
