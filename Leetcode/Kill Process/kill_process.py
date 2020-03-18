# Given n processes, each process has a unique PID (process id) and its PPID (parent process id).
# Each process only has one parent process, but may have one or more children processes. This is just like a tree structure. 
# Only one process has PPID that is 0, which means this process has no parent process. All the PIDs will be distinct positive integers.
# We use two list of integers to represent a list of processes, where the first list contains PID for each process and the second list contains the corresponding PPID.
# Now given the two lists, and a PID representing a process you want to kill, return a list of PIDs of processes that will be killed in the end. 
# You should assume that when a process is killed, all its children processes will be killed. No order is required for the final answer.
"""
Example 1:
Input: 
pid =  [1, 3, 10, 5]
ppid = [3, 0, 5, 3]
kill = 5
Output: [5,10]
Explanation: 
           3
         /   \
        1     5
             /
            10
Kill 5 will also kill 10.


Approach HashMap + DFS:

HashMap:
{
    3: [1, 5]
    5: [10]
}

----------------------------------

Approach HashMap + BFS:

HashMap:
{
    3: [1, 5]
    5: [10]
}


"""
from collections import defaultdict
def get_parent_children(pid, ppid):
    hm = defaultdict(list)
    for i, v in enumerate(ppid):
        if v > 0:
            hm[v].append(pid[i])
    return hm

def kill_process_dfs(pid, ppid, kill):
    hm = get_parent_children(pid, ppid)
    ans, stack = [], [kill]
    while stack:
        curr = stack.pop()
        ans.append(curr)

        """
        Use extend instead of append =>
        >>> x = defaultdict(list)
        >>> stack = []
        >>> stack.extend(x['a'])
        >>> stack
        []
        >>> stack.append(x['a'])
        >>> stack
        [[]]
        """

        stack.extend(hm[curr])

    return ans

import unittest
class TestKillProcess(unittest.TestCase):
    def test_generic(self):
        self.assertEqual(kill_process_dfs([1, 3, 10, 5], [3, 0, 5, 3], 5), [5, 10])

if __name__ == "__main__": unittest.main()