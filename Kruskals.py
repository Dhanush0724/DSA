import heapq

class Disjoint:

    def __init__(self,n):
        self.parent = list(range(n))
        self.rank  = [0]*n

    def find(self,u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]
    
    def union(self,u,v):
        root_u = self.find(u)
        root_v = self.find(v)

        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else :
                self.parent[root_v] = root_u
                self.rank[root_u] += 1

class Solution:
    @staticmethod

    def spanningtree(V,adj):
        edges = []

        for u in range(V):
            for neigh in adj[u]:
                v,weight = neigh
                edges.append((weight,u,v))

        heapq.heapify(edges)

        ds = Disjoint(V)
        mst_weight =  0
        edges_used = 0

        while edges and edges_used < V-1:
            weight, u, v = heapq.heappop(edges)
            if ds.find(u) != ds.find(v):
                ds.union(u,v)
                mst_weight += weight
                edges_used +=1
        return mst_weight

if __name__ == "__main__":
    V = 5
    adj = [
        [(1, 2), (2, 1)],  
        [(0, 2), (2, 1)],  
        [(0, 1), (1, 1), (3, 2), (4, 2)], 
        [(2, 2), (4, 1)],  
        [(3, 1), (2, 2)],  
    ]

    solution = Solution()
    mst_weight = solution.spanningtree(V, adj)
    print("The sum of all the edge weights in the MST is:", mst_weight)