import heapq

class Solution:

    def countpaths(self,n,roads):
        adj  = [[] for _ in range(n)]
        for u,v,w in roads:
            adj[u].append((v,w))
            adj[v].append((u,w))

        pq = []
        heapq.heappush(pq,(0,0))

        dist = [float('inf')]*n
        ways = [0]*n
        dist[0] = 0
        ways[0] = 1

        mod = int(1e9+7)

        while pq:

            dis,node = heapq.heappop(pq)

            for adjnode, edW in adj[node]:

                if dis+edW <dist[adjnode]:
                    dist[adjnode] = dis+edW
                    heapq.heappush(pq,(dist[adjnode],adjnode))
                    ways[adjnode] = ways[node]

                elif dis + edW == dist[adjnode]:
                    ways[adjnode] = (ways[adjnode]+ways[node])%mod
        return ways[n-1]%mod
        
if __name__ == "__main__":
    n = 7
    roads = [
        [0, 6, 7], [0, 1, 2], [1, 2, 3], [1, 3, 3],
        [6, 3, 3], [3, 5, 1], [6, 5, 1], [2, 5, 1],
        [0, 4, 5], [4, 6, 2]
    ]

    obj = Solution()
    ans = obj.countpaths(n, roads)
    print(ans)