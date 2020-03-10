# There are a total of n courses you have to take, labeled from 0 to n-1.
# Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]
# Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should take to finish all courses.
# There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses, return an empty array.

"""
Example 1:
Input: 2, [[1,0]] 
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished   
             course 0. So the correct course order is [0,1] .

Example 2:
Input: 4, [[1,0],[2,0],[3,1],[3,2]]
Output: [0,1,2,3] or [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both     
             courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0. 
             So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3] .
"""
from collections import defaultdict
def course_schedule_ii(n, prerequisites):
    in_degree = [0 for i in range(n)]
    graph = defaultdict(set)
    ans = []

    """
          i j
        [[1,0]]
        To take course 1 you should have finished course 0.
                 j   i
        graph = {0: {1}}
    """

    for i, j in prerequisites:
        graph[j].add(i)
        in_degree[i] += 1

    stack = [vertex for vertex in range(n) if in_degree[vertex] == 0]

    while stack:
        vertex = stack.pop()
        ans.append(vertex)
        for adjacent in graph[vertex]:
            in_degree[adjacent] -= 1
            if in_degree[adjacent] == 0: stack.append(adjacent)

    for vertex in range(n):
        if in_degree[vertex] > 0: return []
        
    return ans
            
import unittest
class TestCourseScheduleII(unittest.TestCase):
    def test_generic(self):
        self.assertEqual(course_schedule_ii(2, [[1,0]]), [0, 1])
        self.assertEqual(course_schedule_ii(4, [[1,0],[2,0],[3,1],[3,2]]), [0,2,1,3])

if __name__ == "__main__": unittest.main()