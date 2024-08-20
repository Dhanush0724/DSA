import heapq
from collections import defaultdict

class Solution:

    def dijkstra(self,edges,N,src):

        adj = defaultdict(list)
        for u,v,w in edges:
            adj[u].append((v,w))
            adj[v].append((u,w))

        dist = [float('inf')]*N
        dist[src] = 0

        pq = [(0,src)]
        while pq:
            current_dist,node  = heapq.heappop(pq)

            if current_dist>dist[node]:
                continue

            for neighbour,weight in adj[node]:

                distance = current_dist+weight

                if distance< dist[neighbour]:
                    dist[neighbour] = distance
                    heapq.heappush(pq,(distance,neighbour))
        
        res = [-1 if d == float('inf') else d for d in dist]
        return res
if __name__ == "__main__":
    N = 9
    edges = [
        (0, 1, 4), (0, 3, 1), (3, 4, 3), (4, 5, 1), (5, 6, 6),
        (1, 2, 1), (2, 6, 5), (6, 7, 2), (7, 8, 3), (6, 8, 1)
    ]
    obj = Solution()
    ans = obj.dijkstra(edges, N, 0)
    for distance in ans:
        print(distance, end=" ")

    