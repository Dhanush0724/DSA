# Detecting cycle in a directed graph

from collections import defaultdict

class Graph():
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices
    
    def addEdge(self, u, v):
        self.graph[u].append(v)

    def isCyclicUtil(self, V, visited, recstack):
        visited[V] = True
        recstack[V] = True

        for neighbour in self.graph[V]:
            if not visited[neighbour]:
                if self.isCyclicUtil(neighbour, visited, recstack):
                    return True
            elif recstack[neighbour]:
                return True

        recstack[V] = False
        return False

    def isCyclic(self):
        visited = [False] * (self.V)
        recStack = [False] * (self.V)

        for node in range(self.V):
            if not visited[node]:
                if self.isCyclicUtil(node, visited, recStack):
                    return True

        return False

if __name__ == "__main__":
    g = Graph(6)
    # g.addEdge(0, 1)
    # g.addEdge(0, 2)
    # g.addEdge(1, 2)
    # g.addEdge(2, 0)
    # g.addEdge(2, 3)
    # g.addEdge(3, 3)
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 3)
    g.addEdge(4, 1)
    g.addEdge(4, 5)
    g.addEdge(5, 3)

    if g.isCyclic():
        print("Graph contains Cycle")
    else:
        print("Graph doesn't contain cycle")
