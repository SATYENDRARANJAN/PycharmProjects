# Adjacency list representation of a graph

class AdjNode:
    def __init__(self,data):
        self.data= data
        self.next = None


# vertices param is denoting count of vertices
class Graph:
    def __init__(self,vertices):
        self.V = vertices
        self.graph = [None] * self.V

    def addEdge(self,u ,v):
        # create a node , append it to adjacent node's adjacency list ,
        # Adding v to u's LL
        node = AdjNode(v)
        node.next = self.graph[u]
        self.graph[u] = node
        # Adding u to v's LL
        node = AdjNode(u)
        node.next = self.graph[v]
        self.graph[v] = node

    def print_graph(self):
        for i in range(self.V):
            print("[{0}]".format(i) + " =>",end = "")
            temp = self.graph[i]
            while temp:
                print(temp.data , "--->",end = "")
                temp = temp.next
            print("End " )



if __name__ == "__main__":
    g = Graph(3)
    g.addEdge(1,0)
    g.addEdge(2,0)
    g.addEdge(1,2)
    g.print_graph()
