class Graph:
    def __init__(self,size):
        self.size=size
        self.adjMatrix=[]
        for i in range(size):
            self.adjMatrix.append([0 for i in range(size)])
        print(self.adjMatrix)
    def add_edge(self,v1,v2):
        if v1==v2:
            print("Same Vertex %d,%d",v1,v2)
        self.adjMatrix[v1][v2]=1
        self.adjMatrix[v2][v1]=1
    def printMatrix(self):
        for row in self.adjMatrix:
            for val in row:
                print(val,end=" ")
            print(end="\n")
    def removeEdge(self,v1,v2):
        if(self.adjMatrix[v1][v2]==0):
            print("No Edge between %d and %d",v1,v2)
            return
        self.adjMatrix[v1][v2]=0
        self.adjMatrix[v2][v1] = 0



n=int(input("No.of vertices"))
g=Graph(n)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.printMatrix()
g.removeEdge(2, 3)
g.printMatrix()
