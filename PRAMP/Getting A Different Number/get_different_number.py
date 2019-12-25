"""
Given an array arr of unique nonnegative integers, implement a function getDifferentNumber 
that finds the smallest nonnegative integer that is NOT in the array.

Solve first for the case when you’re NOT allowed to modify the input arr. 
If successful and still have time, see if you can come up with an algorithm with an improved space complexity when modifying arr is allowed. 
Do so without trading off the time complexity.

Approach 1: Brute Force:
Sort the array in-place if possible to modify array and check which number isn't present

Approach 2: Using Set for O(1) lookup
Create Set store all elements of array in it. Iterate over length of arr and check for iterator in set

Approach 3: Most efficient O(n) time, O(1) space

 0  1  2  3
[1, 0, 3, 2]
 ^
Special in-place sort -> put each number in its corresponding index, kicking out the original number, until the target index is out of range.

    for i from 0 to n-1:
        temp = arr[i]
        while (temp < n and temp != arr[temp]):
            swap(temp, arr[temp])


At first glance, one might think that due to the two nested loops (a while loop inside a for loop) that we use to sort the array,the time complexity is O(N^2). 
However, this is incorrect. The actual time complexity of the two nested loops is linear.
The reason is that every number is at most moved once. For those already in their target indices, 
the while loop will end immediately since the condition arr[temp] != temp isn’t met. In the second part of the code we have another loop whose time complexity is linear. 
The total time complexity is therefore O(N).

"""

def get_different_number(arr):
    if not arr: return None

    