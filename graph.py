import sys

class Graph:
    def __init__(self):
        self.nodes = []
        self.graph = []
        self.nodeCount = 0

    def addNode(self, v):
        if v in self.nodes:
            print(v, "is already present..")
        else:
            self.nodeCount += 1
            self.nodes.append(v)
            for x in self.graph:
                x.append(0)
            temp = []
            for x in range(self.nodeCount):
                temp.append(0)
            self.graph.append(temp)
            print(v, "is added..")

    def addEdge_Undirected_Unweighted(self,v1,v2):
        if v1 not in self.nodes:
            print(" not found")
            return
        if v2 not in self.nodes:
            print(" not found")
            return
        index1 = self.nodes.index(v1)
        index2 = self.nodes.index(v2)
        self.graph[index1][index2] = 1
        self.graph[index2][index1] = 1

    def addEdge_Undirected_Weighted(self,v1,v2,w):
        if v1 not in self.nodes:
            print(" not found")
            return
        if v2 not in self.nodes:
            print(" not found")
            return
        index1 = self.nodes.index(v1)
        index2 = self.nodes.index(v2)
        self.graph[index1][index2] = w
        self.graph[index2][index1] = w

    def addEdge_Directed_Weighted(self,v1,v2,w):
        if v1 not in self.nodes:
            print(" not found")
            return
        if v2 not in self.nodes:
            print(" not found")
            return
        index1 = self.nodes.index(v1)
        index2 = self.nodes.index(v2)
        self.graph[index1][index2] = w
        self.graph[index2][index1] = w

        
    def printGraph(self):
        print("  ", end=" ")
        for node in self.nodes:
            print(node, end=" ")
        print()
        for i in range(self.nodeCount):
            print(self.nodes[i], end=" ")
            for j in range(self.nodeCount):
                print(self.graph[i][j], end=" ")
            print()

    def deleteGraph(self,v):
        if v not in self.nodes:
            print(v,"not present")
        else:
            self.nodeCount-=1
            index1=self.nodes.index(v)
            self.nodes.pop(index1)
            self.graph.pop(index1)
            for x in self.graph:
                x.pop(index1)
            print(v,"is deleted")

if __name__ == "__main__":

    obj = Graph()

    while True:

        print("\n1. Add Node")
        print("2. Add Edge Undirected Unweighted")
        print("3. Add Edge Undirected Weighted")
        print("4. Add Edge Directed Weighted")
        print("5. Print Graph")
        print("6. Delete Graph")
        print("0. Exit")

        n = int(input("Enter your choice: "))

        if n == 1:
            v = input("Enter vertex: ")
            obj.addNode(v)
        elif n == 2:
            v1 = input("Enter vertex 1: ")
            v2 = input("Enter vertex 2: ")
            obj.addEdge_Undirected_Unweighted(v1,v2)
        elif n == 3:
            v1 = input("Enter vertex 1: ")
            v2 = input("Enter vertex 2: ")
            w = int(input("Enter weight: "))
            obj.addEdge_Undirected_Weighted(v1,v2,w)
        elif n == 4:
            v1 = input("Enter vertex 1: ")
            v2 = input("Enter vertex 2: ")
            w = int(input("Enter weight: "))
            obj.addEdge_Directed_Weighted(v1,v2,w)
        elif n == 5:
            obj.printGraph()
        elif n == 6:
            v = input("Enter vertex: ")
            obj.deleteGraph(v)

        elif n == 0:
            sys.exit(0)

        else:
            print("Invalid Choice")