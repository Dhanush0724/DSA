from collections import deque

class Graph:

    def __init__(self,V):
        self.V = V
        self.adjacent_list = [[] for _ in range(V)]

    def add_edge(self,u,v):
        self.adjacent_list[u].append(v)

    def dfs_util(self,vertex,visited,dfs_order):
        visited[vertex] = True
        dfs_order.append(vertex)

        for neighbour in self.adjacent_list[vertex]:
            if not visited[neighbour]:
                self.dfs_util(neighbour,visited,dfs_order)

    def dfs(self,start_vartex):
        
        visited = [False]*self.V
        dfs_order = []
        self.dfs_util(start_vartex,visited,dfs_order)
        return dfs_order


            
    
V = 5
edge  = [(0, 1), (0, 2), (0, 3), (2, 4)]

graph1 = Graph(V)
for u,v in edge:
    graph1.add_edge(u,v)

print("BFS TRAVERSAL",graph1.dfs(0))




