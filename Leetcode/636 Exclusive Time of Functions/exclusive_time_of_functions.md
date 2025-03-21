# 636. Exclusive Time of Functions

## Problem Statement

> On a single-threaded CPU, we execute a program containing n functions. Each function has a unique ID between 0 and n-1.
>
> Function calls are stored in a [call stack](https://en.wikipedia.org/wiki/Call_stack): when a function call starts, its ID is pushed onto the stack, and when a function call ends, its ID is popped off the stack. The function whose ID is at the top of the stack is the current function being executed. Each time a function starts or ends, we write a log with the ID, whether it started or ended, and the timestamp.
>
> You are given a list logs, where logs[i] represents the ith log message formatted as a string "{function_id}:{"start" | "end"}:{timestamp}". For example, "0:start:3" means a function call with function ID 0 started at the beginning of timestamp 3, and "1 : end : 2" means a function call with function ID 1 ended at the end of timestamp 2. Note that a function can be called multiple times, possibly recursively.
>
> A function's exclusive time is the sum of execution times for all function calls in the program. For example, if a function is called twice, one call executing for 2 time units and another call executing for 1 time unit, the exclusive time is 2 + 1 = 3.
>
> Return the exclusive time of each function in an array, where the value at the ith index represents the exclusive time for the function with ID i.

> Constraints:
>
> 1 <= n <= 100
> 1 <= logs.length <= 500
> 0 <= function_id < n
> 0 <= timestamp <= 10<sup>9</sup>
> No two start events will happen at the same timestamp.
> No two end events will happen at the same timestamp.
> Each function has an "end" log for each "start" log.

## Examples

Example 1:

![Example 1](https://assets.leetcode.com/uploads/2019/04/05/diag1b.png)

```
Input: n = 2, logs = ["0:start:0","1:start:2","1:end:5","0:end:6"]
Output: [3,4]
Explanation:
Function 0 starts at the beginning of time 0, then it executes 2 for units of time and reaches the end of time 1.
Function 1 starts at the beginning of time 2, executes for 4 units of time, and ends at the end of time 5.
Function 0 resumes execution at the beginning of time 6 and executes for 1 unit of time.
So function 0 spends 2 + 1 = 3 units of total time executing, and function 1 spends 4 units of total time executing.
```

Example 2:

```
Input: n = 1, logs = ["0:start:0","0:start:2","0:end:5","0:start:6","0:end:6","0:end:7"]
Output: [8]
Explanation:
Function 0 starts at the beginning of time 0, executes for 2 units of time, and recursively calls itself.
Function 0 (recursive call) starts at the beginning of time 2 and executes for 4 units of time.
Function 0 (initial call) resumes execution then immediately calls itself again.
Function 0 (2nd recursive call) starts at the beginning of time 6 and executes for 1 unit of time.
Function 0 (initial call) resumes execution at the beginning of time 7 and executes for 1 unit of time.
So function 0 spends 2 + 4 + 1 + 1 = 8 units of total time executing.
```

Example 3:

```
Input: n = 2, logs = ["0:start:0","0:start:2","0:end:5","1:start:6","1:end:6","0:end:7"]
Output: [7,1]
Explanation:
Function 0 starts at the beginning of time 0, executes for 2 units of time, and recursively calls itself.
Function 0 (recursive call) starts at the beginning of time 2 and executes for 4 units of time.
Function 0 (initial call) resumes execution then immediately calls function 1.
Function 1 starts at the beginning of time 6, executes 1 unit of time, and ends at the end of time 6.
Function 0 resumes execution at the beginning of time 6 and executes for 2 units of time.
So function 0 spends 2 + 4 + 1 = 7 units of total time executing, and function 1 spends 1 unit of total time executing.
```

## Stack Solution

**Problem Recap**
You’re given a list of logs that record when functions start and end on a single-threaded CPU. Functions can call other functions (even recursively), so the logs form a nested structure. The task is to compute the exclusive time for each function, meaning the time spent in the function itself excluding the time spent in its nested function calls.

**Key Observations**

- _Call Stack Behavior_: Since the program is executed on a single-threaded CPU, functions follow a call stack. The function that starts last is the one currently executing.
- _Inclusive Timestamps_: The problem specifies that when a function ends, the timestamp is inclusive (i.e., if a function starts at time 3 and ends at time 3, it takes 1 time unit).
- _Nested Time Accounting_: When a function calls another function, the time spent in the called function should not be counted toward the caller’s exclusive time.

**Algorithm Walkthrough**

1. Initialize:

   - Create a result list res of size n (number of functions) with all values set to 0.
   - Use a stack to simulate the function call stack.

2. Process Each Log:

- For a "start" log:

  - Parse the function ID, the operation ("start"), and the timestamp.
  - Push a record onto the stack. The record is a list containing:
    - `func_id`: The function’s ID.
    - `start_time`: The timestamp when the function started.
    - `nested_time`: Initially set to 0; this will accumulate the total time taken by functions called within this function.

- For an "end" log:
  - Parse the function ID, the operation ("end"), and the timestamp.
  - Pop the top record from the stack (this corresponds to the function that is ending).
  - Compute the total time the function was active as:
    `total_time=(timestamp−start_time+1)` (The +1 accounts for the inclusive timestamp.)
  - The exclusive time for this function call is: `exclusive_time=total_time−nested_time`
  - Add the computed exclusive time to `res[func_id]`.
  - If there is still a function on the stack (i.e., the current function was nested inside another), add the entire total_time (including nested calls) to the nested_time of the function on top of the stack. This way, when that function eventually ends, it will subtract out the time spent in nested calls.

3. Return the Result:

   - After processing all logs, `res` will contain the exclusive time for each function, indexed by their IDs.

**Example Walkthrough**

```
Input:
n = 2
logs = [
    "0:start:0"
    "1:start:2"
    "0:start:4"
    "0:end:5"
    "0:start:6"
    "0:end:7"
    "1:end:8"
    "0:end:10"
]

* run time = (end time - start time) - child processes run time
* stack definition = (id, start, child_runtime)

logs = [
    "0:start:0"     *
    "1:start:2"
    "0:start:4"
    "0:end:5"
    "0:start:6"
    "0:end:7"
    "1:end:8"
    "0:end:10"
]

       0  1
res = [0, 0]
stack = [(0, 0, 0)]


logs = [
    "0:start:0"
    "1:start:2"     *
    "0:start:4"
    "0:end:5"
    "0:start:6"
    "0:end:7"
    "1:end:8"
    "0:end:10"
]

       0  1
res = [0, 0]
stack = [(0, 0, 0), (1, 2, 0)]


logs = [
    "0:start:0"
    "1:start:2"
    "0:start:4"     *
    "0:end:5"
    "0:start:6"
    "0:end:7"
    "1:end:8"
    "0:end:10"
]

       0  1
res = [0, 0]
stack = [(0, 0, 0), (1, 2, 0), (0, 4, 0)]


logs = [
    "0:start:0"
    "1:start:2"
    "0:start:4"
    "0:end:5"       *   function at top of the stack stopped processing
    "0:start:6"
    "0:end:7"
    "1:end:8"
    "0:end:10"
]

       0  1
res = [2, 0]
stack = [(0, 0, 0), (1, 2, 2)]
                           ^
stack.pop() => (0, 4, 0)    => update res[id] = 5 - 4 + 1 (function ran for second 4 and second 5)

update child_runtime of the top of the stack function


logs = [
    "0:start:0"
    "1:start:2"
    "0:start:4"
    "0:end:5"
    "0:start:6"     *
    "0:end:7"
    "1:end:8"
    "0:end:10"
]

       0  1
res = [2, 0]
stack = [(0, 0, 0), (1, 2, 2), (0, 6, 0)]


logs = [
    "0:start:0"
    "1:start:2"
    "0:start:4"
    "0:end:5"
    "0:start:6"
    "0:end:7"       *
    "1:end:8"
    "0:end:10"
]

       0  1
res = [4, 0]
stack = [(0, 0, 0), (1, 2, 4)]


logs = [
    "0:start:0"
    "1:start:2"
    "0:start:4"
    "0:end:5"
    "0:start:6"
    "0:end:7"
    "1:end:8"       *   function 1 stops processing
    "0:end:10"
]

       0  1
res = [4, 3]
stack = [(0, 0, 8)]
                ^
stack.pop() => (1, 2, 4)    => update res = end - start + 1 - child_runtime = 8 - 2 + 1 - 4

update child runtime of 0 (top of stack) +=  runtime of 1 + child_runtime of 1 = 3 + 4


logs = [
    "0:start:0"
    "1:start:2"
    "0:start:4"
    "0:end:5"
    "0:start:6"
    "0:end:7"
    "1:end:8"
    "0:end:10"      *
]

       0  1
res = [7, 3]
stack = []

res[0] += 10 - 0 + 1 - 8 = 3
```

## References

- https://www.youtube.com/watch?v=dsusgzffTDA&ab_channel=Pepcoding
