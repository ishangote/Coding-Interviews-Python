# 528. Random Pick with Weight

## Problem Statement

> You are given a 0-indexed array of positive integers w where w[i] describes the weight of the ith index.
> You need to implement the function pickIndex(), which randomly picks an index in the range [0, w.length - 1] (inclusive) and returns it. The probability of picking an index i is w[i] / sum(w).
>
> - For example, if w = [1, 3], the probability of picking index 0 is 1 / (1 + 3) = 0.25 (i.e., 25%), and the probability of picking index 1 is 3 / (1 + 3) = 0.75 (i.e., 75%).

> Constraints:
>
> 1 <= w.length <= 10<sup>4</sup>
> 1 <= w[i] <= 10<sup>5</sup>
> pickIndex will be called at most 10<sup>4</sup> times.

## Examples

Example 1:

```
Input
["Solution","pickIndex"]
[[[1]],[]]
Output
[null,0]

Explanation
Solution solution = new Solution([1]);
solution.pickIndex(); // return 0. The only option is to return 0 since there is only one element in w.
```

Example 2:

```
Input
["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]
[[[1,3]],[],[],[],[],[]]
Output
[null,1,1,1,1,0]

Explanation
Solution solution = new Solution([1, 3]);
solution.pickIndex(); // return 1. It is returning the second element (index = 1) that has a probability of 3/4.
solution.pickIndex(); // return 1
solution.pickIndex(); // return 1
solution.pickIndex(); // return 1
solution.pickIndex(); // return 0. It is returning the first element (index = 0) that has a probability of 1/4.

Since this is a randomization problem, multiple answers are allowed.
All of the following outputs can be considered correct:
[null,1,1,1,1,0]
[null,1,1,1,1,1]
[null,1,1,1,0,0]
[null,1,1,1,0,1]
[null,1,0,1,0,0]
......
and so on.
```

## Solution

Intuition

- Given a list of positive values, we are asked to randomly pick up a value based on the weight of each value. To put it simple, the task is to do sampling with weight.
- Let us look at a simple example. Given an input list of values [1, 9], when we pick up a number out of it, the chance is that 9 times out of 10 we should pick the number 9 as the answer.
- In other words, the probability that a number got picked is proportional to the value of the number, with regards to the total sum of all numbers.
- To understand the problem better, let us imagine that there is a line in the space, we then project each number into the line according to its value, i.e. a large number would occupy a broader range on the line compared to a small number. For example, the range for the number 9 should be exactly nine times as the range for the number 1.

![Solution](https://leetcode.com/problems/random-pick-with-weight/Figures/528/528_throw_ball.png)

Now, let us throw a ball randomly onto the line, then it is safe to say there is a good chance that the ball will fall into the range occupied by the number 9. In fact, if we repeat this experiment for a large number of times, then statistically speaking, 9 out of 10 times the ball will fall into the range for the number 9. Voila. That is the intuition behind this problem.

```
Example:
           0  1  2
weights = [2, 1, 4]


   w0     w1       w2
********||||xxxxxxxxxxxxxxxx
----------------------------
0   1   2   3   4   5   6   7

=> pick random number between [0, 7)

pick        res
0           w0
1           w0
2           w1
3           w2
4           w2
5           w2
6           w2

   w0     w1       w2
********||||xxxxxxxxxxxxxxxx
---------------------------------
0   1   2   3   4   5   6   7   8
        ^   ^               ^
        * the offsets of the ranges are basically the prefix sums

           0  1  2
weights = [2, 1, 4]
prefix_ = [2, 3, 7]
sums

pick = 4

* We can use binary search to find index smallest index that satisfies:
pick < self.prefix_sums[lo]
```

## References

- https://youtu.be/fWS0TCcr-lE?si=Z-m8qpBz_J6EoKcm
- https://leetcode.com/problems/random-pick-with-weight/editorial/
- https://en.wikipedia.org/wiki/Prefix_sum
