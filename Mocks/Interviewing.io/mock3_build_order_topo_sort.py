"""
app.c     lib.c     app2.c
   |       |         |
app.obj   lib.obj   app2.obj
   |    /         \   |
app.exe              app2.exe


0 -> 1
   /   \
 3       2
 
 
 0 3 1 2
        
        0    1
        0 -> 1



GraphNode 
obj.val = 'app.c'
obj.inorder = 0
 
graph = {
        'app.c': ['app.obj']
        'app.obj': ['app.exe']
        'lib.c': ['lib.obj']
        'lib.obj': ['app.exe', 'app2.exe']
        'app2.c': ['app2.obj']
        'app2.obj': ['app2.exe']
        }
        
        
graph2 = {
        'app.exe': ['app.obj', 'lib.obj']}
        'app.obj': ['app.c']
        'lib.obj': ['lib.c']
        'app2.obj': ['app2.c']
        'app2.exe': ['app2.obj', 'lib.obj']
        }
        
        
all_ancestors_of_input = set(..)
        
'app.c' = [0]
'app.obj' = [1]
'lib.obj' = [1]
'lib.c' = [0]
'app.exe' = [2]
'app2.obj' = [1]
'app2.c'   = [0]
'app2.exe' = [2]

'app.c' = [0]
'app.obj' = [1]
'lib.obj' = [0]
'lib.c' = [0]
'app.exe' = [2]
'app2.obj' = [1]
'app2.c'   = [0]
'app2.exe' = [2]


input = 'app.exe'
out3 == ["lib.c", "app.c", "lib.obj", "app.obj", "app.exe"]

stack = []
"""
from typing import List

class GraphVertex:
    def __init(self, val):
        self.val = val
        self.inorder = 0

def dfs(input_node):
    ans = set()
    return ans #Set of all ancestors

def depends(file: str, input_files: List[str]) -> None:
    """candidate to implement"""
    
def get_build_order(file):
    """candidate to implement"""
    all_nodes = dfs(file)
    graph = depends(file)
    ans = []
    
    stack = [vertex for vertex in all_nodes if vertex.inorder == 0]
    
    while stack:
        vertex = stack.pop()
        ans.append(vertex)
        
        for adj in graph[vertex]:
            adj.inorder -= 1
            if adj in all_nodes and adj.inorder == 0:
                stack.append(adj)
                
    for vertex in all_nodes: 
        if vertex.inorder > 0: return []
    
    return ans

depends("app.obj", ["app.c"])
depends("lib.obj", ["lib.c"])
depends("app.exe", ["lib.obj", "app.obj"])
depends("app2.obj", ["app2.c"])
depends("app2.exe", ["lib.obj", "app2.obj"])

# user is finished called depends()

out1 = get_build_order("app.c")
# out1 == ["app.c"]

out2 = get_build_order("app.obj")
# out2 == ["app.c", "app.obj"]

out3 = get_build_order("app.exe")
# out3 == ["app.c", "app.obj", "lib.c", "lib.obj", "app.exe"]
# out3 == ["lib.c", "lib.obj", "app.c", "app.obj", "app.exe"]
# out3 == ["lib.c", "app.c", "lib.obj", "app.obj", "app.exe"]