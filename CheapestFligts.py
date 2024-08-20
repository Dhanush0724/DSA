
from collections import deque
import sys
class Solution:
    def CheapestFlight(self,n,flights,src,dst,K):
        adj = [[] for _ in range(n)]
        for u,v,w in flights:
            adj[u].append((v,w))

        q = deque([(0,src,0)])
        
        dist = [float('inf')]*n
        dist[src]  = 0

        while q:
            stops,node,cost = q.popleft()

            if stops>K:
                continue

            for adjNode, edge in adj[node]:

                if cost + edge <dist[adjNode] and stops <= K:
                    dist[adjNode]  = cost + edge
                    q.append((stops+1,adjNode,cost+edge))
        
        return dist[dst] if  dist[dst] != float('inf') else -1



if __name__ == "__main__":
    n = 4
    src = 0
    dst = 3
    K = 1

    flights = [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]]

    obj = Solution()
    ans = obj.CheapestFlight(n, flights, src, dst, K)

    print(ans)