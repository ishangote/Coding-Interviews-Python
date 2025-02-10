# 853. Car Fleet

## Problem Statement

> There are n cars at given miles away from the starting mile 0, traveling to reach the mile target.
>
> You are given two integer array `position` and `speed`, both of length `n`, where `position[i]` is the starting mile of the ith car and `speed[i]` is the speed of the ith car in miles per hour.
>
> A car cannot pass another car, but it can catch up and then travel next to it at the speed of the slower car.
>
> A car fleet is a car or cars driving next to each other. The speed of the car fleet is the minimum speed of any car in the fleet.
>
> If a car catches up to a car fleet at the mile `target`, it will still be considered as part of the car fleet.
>
> Return the number of car fleets that will arrive at the destination.

> Constraints:
>
> - n == position.length == speed.length
> - 1 <= n <= 10<sup>5</sup>
> - 0 < target <= 10<sup>6</sup>
> - 0 <= position[i] < target
> - All the values of position are unique.
> - 0 < speed[i] <= 10<sup>6</sup>

## Examples

Example 1:

```
Input: target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]
Output: 3
Explanation:
The cars starting at 10 (speed 2) and 8 (speed 4) become a fleet, meeting each other at 12. The fleet forms at target.
The car starting at 0 (speed 1) does not catch up to any other car, so it is a fleet by itself.
The cars starting at 5 (speed 1) and 3 (speed 3) become a fleet, meeting each other at 6. The fleet moves at speed 1 until it reaches target.
```

Example 2:

```
Input: target = 10, position = [3], speed = [3]
Output: 1
Explanation:
There is only one car, hence there is only one fleet.
```

Example 3:

```
Input: target = 100, position = [0,2,4], speed = [4,2,1]
Output: 1
Explanation:
The cars starting at 0 (speed 4) and 2 (speed 2) become a fleet, meeting each other at 4. The car starting at 4 (speed 1) travels to 5.
Then, the fleet at 4 (speed 2) and the car at position 5 (speed 1) become one fleet, meeting each other at 6. The fleet moves at speed 1 until it reaches target.
```

## Stack Solution

```
Input:
target = 10
position = [0, 5]
speed    = [10, 5]

speed = distance / time
time = distance / speed

car 1 =>
distance = 10 - 0 = 10
speed = 10
* time = 1

car 2 =>
distance = 10 - 5 = 5
speed = 5
* time = 1

=> both cars reach 10 at 1, hence forming one fleet

Output:
1
```

```
Input
target = 10
(position, speed) =
[(3, 3), (5, 2), (7, 1)]

* ttd => time to destination = distance to destination / speed


                        cars will meet before destination (ttd2 <= ttd3)
                                /        \
                       ttd2 = 2.5          ttd3 = 3
   3mph ->             2mph ->             1mph ->
   c1                  c2                  c3
---3-------------------5-------------------7-----------------------10---->
                                                                      position



                        we no longer have to track c2
                                /        \
                       ttd2 = 2.5          ttd3 = 3
   3mph ->             2mph ->             1mph ->
   c1                  c2                  c3
---3-------------------5-------------------7-----------------------10---->
                                                                      position



             cars will meet before destination (ttd3 <= ttd1)
             /                            \
   ttd1 = 2.3                              ttd3 = 3
   3mph ->             2mph ->             1mph ->
   c1                  c2                  c3
---3-------------------5-------------------7-----------------------10---->
                                                                      position

              we no longer have to track c1
             /                            \
   ttd1 = 2.3                              ttd3 = 3
   3mph ->             2mph ->             1mph ->
   c1                  c2                  c3
---3-------------------5-------------------7-----------------------10---->
                                                                      position

Output:
1
```

## References

- https://www.youtube.com/watch?v=Pr6T-3yB9RM&ab_channel=NeetCode
