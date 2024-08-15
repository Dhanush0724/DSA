
from collections import deque

class Solution:

    def bfs(self,node,adjlist,visited):

        queue = deque([node])
        visited[node] = 1

        while queue:
            current = queue.popleft()
            for neighbour in adjlist[current]:
                if not visited[neighbour]:
                    visited[neighbour] = 1
                    queue.append(neighbour)
    
    def numprovied(self,adj,V):
        adjlist = [[] for _ in range(V)] 

        for i in range(V):
            for j in range(V):
                if adj[i][j] == 1 and i!=j:
                    adjlist[i].append(i)
                    adjlist[j].append(j)
        
        visited = [0]*V
        count  = 0
        for i in range(V):
            if not visited[i]:
                count+=1
                self.bfs(i,adjlist,visited)
        
        return count

adj = [
    [1, 0, 1],
    [0, 1, 0],
    [1, 0, 1]
]

ob = Solution()
print(ob.numprovied(adj, 3))