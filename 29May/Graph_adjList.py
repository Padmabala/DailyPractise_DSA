class Graph:
    def __init__(self,size):
        self.size=size
        self.adjList=[[] for i in range(size)]
        print(self.adjList)
        self.visited=[False for i in range(size)]
    def add_edge(self,v1,v2):
        if(v1 not in self.adjList[v2]):
            self.adjList[v2].append(v1)
        if(v2 not in self.adjList[v1]):
            self.adjList[v1].append((v2))
    def print_graph(self):
        for i in range(len(self.adjList)):
            print(self.adjList[i])
    def BFS(self,vertice):
        q=[]
        q.append(vertice)
        self.visited[vertice] = True
        while(q):
            vertice=q.pop(0)
            print(vertice, end=" ")
            for i in self.adjList[vertice]:
                if self.visited[i]==False:
                    q.append(i)
                    self.visited[i] = True
    def BFS_traversal(self):
        self.BFS(3)
    def DFS(self,vertice):
        self.visited[vertice]=True
        print(vertice,end=" ")
        for i in self.adjList[vertice]:
            if self.visited[i]!=True:
                self.DFS(i)

    def DFS_traversal(self):
        self.visited = [False for i in range(size)]
        print("\n")
        self.DFS(1)
size=int(input("Enter the no. of vertices"))
g=Graph(size)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.print_graph()
g.BFS_traversal()
g.DFS_traversal()