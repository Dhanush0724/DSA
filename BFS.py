from collections import deque

class Graph:

    def __init__(self,V):
        self.V = V
        self.adjacent_list = [[] for _ in range(V)]

    def add_edge(self,u,v):
        self.adjacent_list[u].append(v)

    def bfs(self,start_vartex):
        visited = [False]*self.V
        queue = deque([start_vartex])
        visited[start_vartex] = True
        bfs_order = []

        while queue:
            vertex = queue.popleft()
            bfs_order.append(vertex)

            for neighbour in self.adjacent_list[vertex]:
                if not visited[neighbour]:
                    queue.append(neighbour)
                    visited[neighbour] = True
        return bfs_order
    
V = 5
edge  = [(0, 1), (0, 2), (0, 3), (2, 4)]

graph1 = Graph(V)
for u,v in edge:
    graph1.add_edge(u,v)

print("BFS TRAVERSAL",graph1.bfs(0))




