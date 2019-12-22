from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph = defaultdict(list) 
        self.all_vertex_values = set()

    def add_edge(self, u , v): 
        self.graph[u].append(v)
        self.all_vertex_values.add(u)
        self.all_vertex_values.add(v)
    
    def get_adjacent_vertices(self, v):
        return self.graph[v]