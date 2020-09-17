"""
Given a characters array tasks, representing the tasks a CPU needs to do, where each letter represents a different task. 
Tasks could be done in any order. Each task is done in one unit of time. For each unit of time, the CPU could complete either one task or just be idle.
However, there is a non-negative integer n that represents the cooldown period between two same tasks (the same letter in the array), 
that is that there must be at least n units of time between any two same tasks.

Return the least number of units of times that the CPU will take to finish all the given tasks.

Constraints:

1 <= task.length <= 104
tasks[i] is upper-case English letter.
The integer n is in the range [0, 100].

--------------------

n = 2
A:6
B:1
C:1
D:1

A _ _ A _ _ A _ _ A _ _ A _ _ A

                total_spaces between A = (6 - 1) * n = 10
                total sum of other tasks excluding A = 3
                A B _ A C _ A D _ A _ _ A _ _ A
                cnt_idle_slots = 10 - 3 = 7
                
                Hence we return len(input) + 7 = 9 + 7 = 16

--------------------

n = 2
A:6
B:1
C:1
D:1
E:1
F:1
G:1

A _ _ A _ _ A _ _ A _ _ A _ _ A

                total_spaces between A = (6 - 1) * n = 10
                total sum of other tasks excluding A = 6
                A B C A D _ A E _ A F _ A G _ A
                cnt_idle_slots = 10 - 6 = 4
                
                Hence we return len(input) + 4 = 12 + 4 = 16

--------------------
n = 1
A:3
B:3

A _ A _ A

                total_spaces between A = (3 - 1) * n = 2
                total sum of other tasks excluding A = 3
                cnt_idle_slots = 2 - 3 = -1 => -ve Hence return len(input) = 6

--------------------
VERY GOOD EDGE CASE!
n = 2
A:3
B:3

NOTE: number of tasks having highest freq = 2 (A, B)

A B _ A B _ A B

                total_spaces between A = (3 - 1) * n = 4
                number of tasks having highest freq excluding A = 1 (B) 
                total sum of other tasks excluding A = 3
                cnt_idle_slots = 4 - 3 + number of tasks having highest freq excluding = 4 - 3 + 1 = 2

                return len(tasks) + cnt_idle_slots = 6 + 2 = 8

n = 1
A:2
B:2
C:2


A C A B C B

                total_spaces between A = (2 - 1) * n = 1
                number of tasks having highest freq excluding A = 3 (B, C D E) 
                total sum of other tasks excluding A = 4
                cnt_idle_slots = 1 - 4 + number of tasks having highest freq excluding A = 1 - 4 + 2 = -1 (-ve)
                return len(tasks)


"""
# Time: O(n)
# Space: O(1)
from collections import Counter
def task_scheduler(tasks, n):
    if not tasks or n == 0: return len(tasks)

    char_count = [0] * 26
    
    for ch in tasks:
        char_count[ord(ch) - ord('A')] += 1
    
    # A count
    cnt_most_freq_task = max(char_count)

    # total_spaces between A
    cnt_spaces = (cnt_most_freq_task - 1) * n

    # number of tasks having highest freq excluding A
    num_most_freq_tasks = char_count.count(cnt_most_freq_task) - 1

    # total sum of other tasks excluding A
    cnt_all_other_tasks = sum(char_count) - cnt_most_freq_task

    cnt_idle_slots = cnt_spaces - cnt_all_other_tasks + num_most_freq_tasks

    if cnt_idle_slots < 0: return len(tasks)
    
    return len(tasks) + cnt_idle_slots

import unittest
class TestTaskScheduler(unittest.TestCase):
    def test_generic(self):
        self.assertEqual(task_scheduler(["A","A","A","B","B","B"], 2), 8)
        self.assertEqual(task_scheduler(["A","A","A","B","B","B"], 0), 6)
        self.assertEqual(task_scheduler(["A","A","A","A","A","A","B","C","D","E","F","G"], 2), 16)

if __name__ == "__main__": unittest.main()