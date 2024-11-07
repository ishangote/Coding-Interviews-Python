# 1011. Capacity To Ship Packages Within D Days

## Problem Statement

> A conveyor belt has packages that must be shipped from one port to another within days days.
>
> The ith package on the conveyor belt has a weight of weights[i]. Each day, we load the ship with packages on the conveyor belt (in the order given by weights). We may not load more weight than the maximum weight capacity of the ship.
>
> Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being shipped within days days.

> Constraints:
>
> - 1 <= days <= weights.length <= 5 \* 10<sup>4</sup>
> - 1 <= weights[i] <= 500

Example 1:

```
Input: weights = [1,2,3,4,5,6,7,8,9,10], days = 5
Output: 15
Explanation: A ship capacity of 15 is the minimum to ship all the packages in 5 days like this:
1st day: 1, 2, 3, 4, 5
2nd day: 6, 7
3rd day: 8
4th day: 9
5th day: 10

Note that the cargo must be shipped in the order given, so using a ship of capacity 14 and splitting the packages into parts like (2, 3, 4, 5), (1, 6, 7), (8), (9), (10) is not allowed.
```

Example 2:

```
Input: weights = [3,2,2,4,1,4], days = 3
Output: 6
Explanation: A ship capacity of 6 is the minimum to ship all the packages in 3 days like this:
1st day: 3, 2
2nd day: 2, 4
3rd day: 1, 4
```

Example 3:

```
Input: weights = [1,2,3,1,1], days = 4
Output: 3
Explanation:
1st day: 1
2nd day: 2
3rd day: 3
4th day: 1, 1
```

## Binary Search Solution

To find the minimum ship capacity, we use a binary search within the range [max(weights), sum(weights)].

Key Observations

1. Capacity Range:
   The optimal ship capacity will be within [max(weights), sum(weights)]:

   - Lower bound (lb) = max(weights), since the ship must at least be able to carry the heaviest package.
   - Upper bound (hb) = sum(weights), as this is the total weight of all packages.

2. Binary Search for Capacity: We perform binary search on this range to find the minimal feasible capacity that meets the shipping requirements within the given days.

```
Input:
weights = [1, 2, 3, 1, 1]
days/ships = 4

------------------------
lb = 3, hb = 8
mid = 5

Shipment =>
Day 1: [1, 2, 3]
Day 2: [1, 1]

We can ship within 4 days, try reducing capacity.
------------------------

lb = 3, hb = 5
mid = 4

Shipment =>
Day 1: [1, 2]
Day 2: [3]
Day 3: [1, 1]

We can ship within 4 days, try reducing capacity.
------------------------

lb = 3, hb = 4
mid = 3

Shipment =>
Day 1: [1, 2]
Day 2: [3]
Day 3: [1, 1]

We can ship within 4 days, try reducing capacity.
------------------------

lb = 3, hb = 3 => return 3

Output: 3
```

```
Input:
weights = [3, 2, 2, 4, 1, 4]
days = 3

lb = 4, hb = 16
mid = 10

Shipment =>
Day 1: [3, 2, 2]
Day 2: [4]
Day 3: [1, 4]

We can ship within 3 days, try reducing capacity
------------------------

lb = 4, hb = 10
mid = 7

Shipment =>
Day1: [3, 2]
Day2: [2, 4, 1]
Day3: [4]

We can ship within 3 days, try reducing capacity
------------------------

lb = 4, hb = 7
mid = 5

Shipment =>
Day1: [3, 2]
Day2: [2]
Day3: [4, 1]
Day4: [4]

We can NOT ship within 3 days, try increasing capacity
------------------------

lb = 5, hb = 7
mid = 6

Shipment =>
Day1: [3, 2]
Day2: [2, 4]
Day3: [1, 4]

We can ship within 3 days, try reducing capacity
------------------------

lb = 5, hb = 6
mid = 5
Shipment =>
Day1: [3, 2]
Day2: [2]
Day3: [4, 1]
Day4: [4]

We can NOT ship within 3 days, try increasing capacity
------------------------

lb = 6, hb = 6 => return res = 6

Output: 6
```

## References

- https://www.youtube.com/watch?v=ER_oLmdc-nw&ab_channel=NeetCodeIO
