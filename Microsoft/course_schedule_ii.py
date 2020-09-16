"""
There are a total of n courses you have to take labelled from 0 to n - 1.

Some courses may have prerequisites, for example, if prerequisites[i] = [ai, bi] this means you must take the course bi before the course ai.

Given the total number of courses numCourses and a list of the prerequisite pairs, return the ordering of courses you should take to finish all courses.

If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.


Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].
Example 2:

Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].


[[1,0],[2,0],[3,1],[3,2]]

        2 > 3
        ^   ^
        0 > 1


            0 1 2 3 
indegree = [0 1 1 2]
stack = [0]

            0 1 2 3 
indegree = [0 0 0 2]
stack = [1, 2]
ans = [0]

            0 1 2 3 
indegree = [0 0 0 1]
stack = [1]
ans = [0, 2]


            0 1 2 3 
indegree = [0 0 0 0]
stack = [3]
ans = [0, 2, 1]

            0 1 2 3 
indegree = [0 0 0 0]
stack = []
ans = [0, 2, 1, 3]

"""
from collections import defaultdict
def course_schedule_ii(n, prerequisites):
    indegree = [0] * n
    graph = defaultdict(list)

    for courses in prerequisites:
        indegree[courses[0]] += 1
        graph[courses[1]].append(courses[0])

    stack = [i for i, v in enumerate(indegree) if v == 0]
    ans = []
    while stack:
        cur = stack.pop()
        ans.append(cur)
        for nbr in graph[cur]:
            indegree[nbr] -= 1
            if indegree[nbr] == 0: stack.append(nbr)
    
    for id in indegree: 
        if id != 0: return []
    return ans