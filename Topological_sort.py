
from collections import deque
class Solution:


    def dfs(self,node,visited,st,adj):

        visited[node] = True
        for neighbour in adj[node]:
            if not visited[neighbour]:
                self.dfs(neighbour,visited,st,adj)
        st.append(node)

    def topoSort(self,V,adj):
        visisted = [False]*V
        st = deque()
        for i in range(V):
            if not visisted[i]:
                self.dfs(i,visisted,st,adj)
        
        ans = []
        while st:
            ans.append(st.pop())
        return ans



if __name__ == "__main__":
    adj_list = {0: [], 1: [], 2: [3], 3: [1], 4: [0, 1], 5: [0, 2]}
    V = 6
    solution = Solution()
    result = solution.topoSort(V, adj_list)
    
    print("Topological Sort of the graph:")
    for node in result:
        print(node, end=" ")
    print()