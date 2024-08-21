class DisjointSet:
    def __init__(self, n):
        self.rank = [0] * (n + 1)
        self.parent = list(range(n + 1))
        self.size = [1] * (n + 1)

    def findUPar(self, node):
        if node == self.parent[node]:
            return node
        # Path compression
        self.parent[node] = self.findUPar(self.parent[node])
        return self.parent[node]

    def unionByRank(self, u, v):
        ulp_u = self.findUPar(u)
        ulp_v = self.findUPar(v)
        if ulp_u == ulp_v:
            return
        # Union by rank
        if self.rank[ulp_u] < self.rank[ulp_v]:
            self.parent[ulp_u] = ulp_v
        elif self.rank[ulp_v] < self.rank[ulp_u]:
            self.parent[ulp_v] = ulp_u
        else:
            self.parent[ulp_v] = ulp_u
            self.rank[ulp_u] += 1

    def unionBySize(self, u, v):
        ulp_u = self.findUPar(u)
        ulp_v = self.findUPar(v)
        if ulp_u == ulp_v:
            return
        # Union by size
        if self.size[ulp_u] < self.size[ulp_v]:
            self.parent[ulp_u] = ulp_v
            self.size[ulp_v] += self.size[ulp_u]
        else:
            self.parent[ulp_v] = ulp_u
            self.size[ulp_u] += self.size[ulp_v]

if __name__ == "__main__":
    ds = DisjointSet(7)
    ds.unionBySize(1, 2)
    ds.unionBySize(2, 3)
    ds.unionBySize(4, 5)
    ds.unionBySize(6, 7)
    ds.unionBySize(5, 6)
    
    # Check if 3 and 7 are in the same set
    if ds.findUPar(3) == ds.findUPar(7):
        print("Same")
    else:
        print("Not same")

    ds.unionBySize(3, 7)

    # Check again if 3 and 7 are in the same set
    if ds.findUPar(3) == ds.findUPar(7):
        print("Same")
    else:
        print("Not same")
