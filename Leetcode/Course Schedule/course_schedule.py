# There are a total of n courses you have to take, labeled from 0 to n-1.
# Some courses may have prerequisites, for example to take course 0 you have to first take course 1, 
# which is expressed as a pair: [0,1]
# Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

# Note:
# The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
# You may assume that there are no duplicate edges in the input prerequisites.


"""
Example 1:

Input: 2, [[1,0]] 
Output: true
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: 2, [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0, and to take course 0 you should
             also have finished course 1. So it is impossible.
"""

#Topological Sort Solution
def course_schedule_topo(n, prerequisites):
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
        if in_degree[vertex] > 0: return False
        
    return True

from has_cycle_graph import *
def course_schedule(prerequisites):
    g = Graph()
    for courses in prerequisites:
        u, v = courses[0], courses[1]
        g.add_edge(v, u)
    return True if not has_cycle(g) else False

import unittest
class TestCourseSchedule(unittest.TestCase):
    def test_course_schedule_generic(self):
        p1 = [[1, 0]]
        p2 = [[1, 0], [3, 2]]

        p3 = [[1, 0], [0, 1]]
        p4 = [[1, 0], [3, 2], [2, 0], [0, 3]]

        self.assertEqual(course_schedule(p1), True)
        self.assertEqual(course_schedule(p2), True)

        self.assertEqual(course_schedule_topo(2, p1), True)
        self.assertEqual(course_schedule_topo(4, p2), True)

        self.assertEqual(course_schedule(p3), False)
        self.assertEqual(course_schedule(p4), False)

        self.assertEqual(course_schedule_topo(2, p3), False)
        self.assertEqual(course_schedule_topo(4, p4), False)

if __name__ == '__main__': unittest.main()