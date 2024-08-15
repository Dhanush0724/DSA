from collections import deque,defaultdict

def isCycle(V,adj):

    def bfs(start):
        queue = deque(([(start, -1)]))
        visited[start] = True

        while queue:
            node,parent = queue.popleft()
            for neigbour in adj[node]:
                if not visited[neigbour]:
                    visited[neigbour] = True
                    queue.append((neigbour,node))
                elif neigbour!=parent:
                    return True
                
        return False

    
    visited = [False]*V
    for i in range(V):
        if not visited[i]:
            if bfs(i):
                return True
    return False
        




V = 8
edges = [(0, 1), (0, 2), (1, 3), (2, 4), (3, 5), (4, 5), (6, 7)]
adj = defaultdict(list)


for u, v in edges:
    adj[u].append(v)
    adj[v].append(u)

print(isCycle(V, adj)) 