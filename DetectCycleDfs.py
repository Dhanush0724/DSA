from collections import defaultdict

def isCycle(V,adj):

    def dfs(node,parent):

        visited[node] = True

        for neighbours in adj[node]:

            if not visited[neighbours]:
                if dfs(neighbours,node):
                    return True
            elif neighbours!=parent:
                return True
        return False
        


    #### for multiple componenet
    visited = [False]*V
    for i in range(V):
        if not visited[i]:
            if dfs(i,-1):
                return True
    return False
        




V = 8
edges = [(0, 1), (0, 2), (1, 3), (2, 4), (3, 5), (4, 5), (6, 7)]
adj = defaultdict(list)


for u, v in edges:
    adj[u].append(v)
    adj[v].append(u)

print(isCycle(V, adj)) 