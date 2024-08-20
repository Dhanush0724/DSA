from collections import deque, defaultdict

class Solution:

    def shortestpath(self,edges,N,M,src):

        adj = defaultdict(list)
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        dist = [float('inf')]*N

        dist[src] = 0
        q = deque([src])

        while q:
            node = q.popleft()
            for neighbour in adj[node]:
                if dist[node]+1<dist[neighbour]:
                    dist[neighbour] = dist[node]+1
                    q.append(neighbour)
        
        res = [-1]*N
        for i in range(N):
            if dist[i]!= float('inf'):
                res[i] = dist[i]
        return res




if __name__ == "__main__":
    N, M = 9, 10
    edges = [[0, 1], [0, 3], [3, 4], [4, 5], [5, 6], [1, 2], [2, 6], [6, 7], [7, 8], [6, 8]]
    
    obj = Solution()
    ans = obj.shortestpath(edges, N, M, 0)
    
    for distance in ans:
        print(distance, end=" ")