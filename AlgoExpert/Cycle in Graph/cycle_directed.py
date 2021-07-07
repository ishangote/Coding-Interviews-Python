"""
Questions:
1. Is a single node considered a graph? yes if it is connected to itself
2. Are the node values integers? yes

Examples:

	   2
	  * *
	 /   \
	0  -* 1
	
Not a cycle
Topological sort approach:

start_node = 0
            0. 1. 2. 
indegree = [0, 1, 2]

init = 
stack = [0]
indegree = [0, 1, 2]


stack = []
indegree = [0, 0, 0]
indegree all 0, Hence DAG -> no cycle


--------------------------------


   	   2
	  / *
	 *   \
	0  -* 1
    *
	|
	3

Expect: cycle

indegree = [2, 1, 1, 0]
start_node = 3

stack = []
indegree = [1, 1, 1, 0]

indegree not all 0, Hence not a cycle

Time: O(v x e)
Space: O(v x e)
"""

def is_cyclic(edges):
    indegree = [0] * len(edges)
    stack = []

    for nbrs in edges:
        for nbr in nbrs:
            indegree[nbr] += 1
    
    for vertex, degree in enumerate(indegree):
        if degree == 0: stack.append(vertex)
    
    while stack:
        node = stack.pop()
        for nbr in edges[node]:
            indegree[nbr] -= 1
            if indegree[nbr] == 0: stack.append(nbr)
    
    for degree in indegree:
        if degree != 0: return True
    
    return False