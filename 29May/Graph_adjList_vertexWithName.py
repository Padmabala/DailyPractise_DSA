class Graph:
    def __init__(self,size):
        self.size=size
        self.vertices={}
        self.adjList=[[]for i in range(self.size)]
        self.vertexIndex=0
    def add_Edge(self,v1,v2):
        if v1 not in self.vertices:
            self.vertices[v1]=self.vertexIndex
            self.vertexIndex+=1
        if v2 not in self.vertices:
            self.vertices[v2]=self.vertexIndex
            self.vertexIndex+=1
        self.adjList[self.vertices[v1]].append(v2)
        self.adjList[self.vertices[v2]].append(v1)
    def printMatrix(self):
        for i in self.vertices:
            print(i,"can go to ",self.adjList[self.vertices[i]])
size=int(input("Enter the number of vertices"))
g=Graph(size)
g.add_Edge("mumbai","chennai")
g.add_Edge("london","delhi")
g.add_Edge("california","chennai")
g.add_Edge("delhi","pakistan")
g.add_Edge("srilanka","mumbai")
g.printMatrix()