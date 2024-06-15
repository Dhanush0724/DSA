#adjacency matrix graph
class Graph:
    
    def __init__(self,graph):
        self.__g = graph
        self.__n = len(graph)

    def create_adjaceny_matrix(self):

        num_vertices = self.__n
        
        adj_matrix = [[0]*num_vertices for _ in range(num_vertices)]

        for i in range(num_vertices):
            for j in range(num_vertices):
                if graph[i][j] == 1:
                    adj_matrix[i][j] = 1
                    
        return adj_matrix
    
    def add_vertex(self):

        self.__n +=1

        for row in self.__g:
            row.append(0)
        
        self.__g.append([0]*self.__n)
    
    def add_edge(self,u,v):
        if u <self.__n and v<self.__n:
            self.__g[u][v] = 1
            self.__g[u][v] = 1

    def print_graph(self):
        adj = self.create_adjaceny_matrix()

        for row in adj:
            print(' '.join(map(str,row)))


graph = [
        [0,1,0,0],
        [1,0,1,0],
        [0,1,0,1],
        [0,0,1,0]
    ]

g = Graph(graph)
print("Intial Graph:")
g.print_graph()

print("\nAdding a new verex:")
g.add_vertex()
g.print_graph()

print("\nAdding an edge between vertex 4 and vertex 1:")
g.add_edge(4,1)
g.print_graph()


    