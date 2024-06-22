#BFS   GRAPH

from collections import deque

def bfs(adjlist,startnode,visited):
    q = deque()
    visited[startnode] = True
    q.append(startnode)
    while q:
        currentNode = q.popleft()
        print(currentNode,end=" ")
        for neighbour in adjlist[currentNode]:
            if not visited[neighbour]:
                visited[neighbour] = True
                q.append(neighbour)


def addEdge(adjlist,u,v):
    adjlist[u].append(v)


def main():
    vertices = 5
    
    adjlist = [[] for _ in range(vertices)]
    addEdge(adjlist,0,1)
    addEdge(adjlist,0,2)
    addEdge(adjlist,1,3)
    addEdge(adjlist,1,4)
    addEdge(adjlist,2,4)
    
    print(adjlist)

    visited = [False]*vertices

    print("BFS traversal starting from vertex 0 :", end=" ")
    bfs(adjlist,0,visited)

    

if __name__ == "__main__":
    main()