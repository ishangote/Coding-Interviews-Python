"""
Questions:
1. len(tasks) = 2*k? yes
2. Any order of completing tasks? No
3. Multiple optimal solutions? return any one
4. Tasks time -ve/0? No
5. Is the input mutable? Yes

Examples:
k = 3    
tasks = 
 0. 1. 2. 3. 4. 5
[1, 3, 5, 3, 1, 4]

Brute Force:
[1, 3] [5, 3] [1, 4]
[1, 5] [3, 3] [1, 4]
...
k subsets of size 2 => Time: nC2 => n! / (2 (n - 2)!) ~ O(n^2)

sorted tasks = 
[1, 1, 3, 3, 4, 5]
 ^				^
 w1
 [1, 5]
 w2
 [1, 4]
 w3
 [3, 3]
"""

from collections import defaultdict
def get_index(tasks_map, task):
    return tasks_map[task].pop()

def task_assignment(k, tasks):
    tasks_map = defaultdict(list)
    for idx, task in enumerate(tasks):
        tasks_map[task].append(idx)
    
    sorted_tasks = sorted(tasks)
    res = []

    i, j = 0, len(sorted_tasks) - 1
    while i < j:
        res.append([get_index(tasks_map, sorted_tasks[i]), get_index(tasks_map, sorted_tasks[j])])
        i += 1
        j -= 1

    return res