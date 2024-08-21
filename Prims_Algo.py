import heapq

class Solution:
    
    def prims(self,edges,V):

        adj = [[] for _ in range(V)]

        for u,v,w in edges:
            adj[u].append((v,w))
            adj[v].append((u,w))
        
        

        visited = [0]*V

        pq = []
        total_weight_sum = 0
        visited = [False]*V
        heapq.heappush(pq,(0,0))

        while pq:

            wt,node= heapq.heappop(pq)

            if visited[node]:
                continue

            visited[node] = True
            total_weight_sum+=wt

            for adjnode,edw in adj[node]:
                if not visited[adjnode]:
                    heapq.heappush(pq,(edw,adjnode))
        
        return total_weight_sum
            




    



if __name__ == "__main__":

    V = 5
    edges = [(0, 1, 2), (0, 2, 1), (1, 2, 1), (2, 3, 2), (3, 4, 1), (4, 2, 2)]
    solution = Solution()
    res = solution.prims(edges,V)
    print(res)

    
    