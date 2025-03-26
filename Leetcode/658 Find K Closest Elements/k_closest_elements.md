# 658. Find K Closest Elements

## Problem Statement

> Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. The result should also be sorted in ascending order.
>
> An integer a is closer to x than an integer b if:
>
> - `|a - x| < |b - x|`, or
> - `|a - x| == |b - x| and a < b`

> Constraints:
>
> - 1 <= k <= arr.length
> - 1 <= arr.length <= 10<sup>4</sup>
> - arr is sorted in ascending order.
> - -10<sup>4</sup> <= arr[i], x <= 10<sup>4</sup>

## Examples

Example 1:

```
Input: arr = [1,2,3,4,5], k = 4, x = 3
Output: [1,2,3,4]
```

Example 2:

```
Input: arr = [1,1,2,3,4,5], k = 4, x = -1
Output: [1,1,2,3]
```

## Binary Search + Two Pointers Solution

### Explanation of the Approach

1. **Finding the Insertion Point (Binary Search Helper):**

   - **Goal:**  
     The function `binary_search_helper(arr, target)` locates the first index in the sorted array where the value is **greater than or equal to** the target. This is the "first occurrence" (or "threshold") binary search.
   - **How It Works:**
     - It initializes two pointers: `lo = 0` and `hi = len(arr) - 1`.
     - In each iteration, it calculates the mid index.
     - If `arr[mid]` is greater than or equal to the target, it narrows the search to the left half by setting `hi = mid`.
     - Otherwise, it moves to the right half with `lo = mid + 1`.
     - When the loop ends, `lo` (or `hi`) points to the first element that meets the condition.
   - **Insight:**  
     If the target isn’t present, this function returns the index of the smallest element that is greater than the target.

2. **Expanding Outward to Find k Closest Elements:**

   - **Initialization:**
     - **Left Pointer:** Set to `pivot - 1`, which is the element immediately to the left of the insertion point.
     - **Right Pointer:** Set to `pivot`, starting at the insertion point.
   - **Two-Pointer Expansion:**
     - Run a loop `k` times to select the k closest elements.
     - **Distance Comparison:**
       - Compute `distance_left` as `target - arr[left]` (if `left` is in bounds) and `distance_right` as `arr[right] - target` (if `right` is in bounds).
       - If `left` is out of bounds, treat its distance as infinite (`sys.maxsize`), and similarly for `right`.
     - **Choosing Elements:**
       - If the left element is closer (or equally close, thus honoring the tie-breaker that favors the smaller element), decrement `left`.
       - Otherwise, increment `right`.
   - **Final Window:**  
     Since the array is sorted, the window `[left+1:right]` (which is contiguous) contains exactly the k closest elements in ascending order.

3. **Time and Space Complexity:**
   - **Time Complexity:** \(O(\log n + k)\)
     - \(O(\log n)\) for the binary search.
     - \(O(k)\) for the two-pointer expansion.
   - **Space Complexity:** \(O(k)\) for the output slice (assuming slicing produces a new list).

### Key Takeaways

- **Binary Search for the First Occurrence:**  
  By using a threshold binary search, you find the position where the target would be inserted. This splits the array into two parts, even if the target isn't present.
- **Contiguous Window of k Elements:**  
  Expanding outward using two pointers from the pivot ensures that the k closest elements form a contiguous subarray. This guarantees that the final output is already sorted, eliminating the need for an additional sort.
- **Handling Edge Cases:**  
  The use of `sys.maxsize` ensures that when one pointer goes out of bounds, the other side is chosen automatically.
