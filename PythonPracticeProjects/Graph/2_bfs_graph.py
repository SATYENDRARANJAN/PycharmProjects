
class Graph:
    def __init__(self,vertices):
        self.V = vertices
        self.graph = [None] * self.V

    def addEdge(self, u , v):
        node = AdjNode(v)
        node.next = self.graph[u]
        self.graph[u] = node

        node = AdjNode(u)
        node.next = self.graph[v]
        self.graph[v] = node

    def bfs(self):
        self.bfs_util( self.graph[0])

    def bfs_util(self, src):
        queue = []
        visited = [None] * self.V
        # print("src ind: ",src.index)
        queue.append(src)
        visited[src.index] = True
        while(queue):
            node = queue.pop(0)
            print( node.index )

            temp = self.graph[node.index]
            # print("temp",temp.index)
            # print(visited)
            # print(temp)
            while temp:
                if not visited[temp.index]:
                    queue.append(temp)
                    # print("Added ->",temp.index)
                    visited[temp.index] = True
                temp=temp.next

    def print_graph(self):
        for i in range(self.V):
            print("[{0}]".format(i) + " =>", end = "")
            temp = self.graph[i]
            while temp:
                print(temp.index, "--->", end = "")
                temp = temp.next
            print("End ")

class AdjNode:
    def __init__(self,data):
        self.index = data
        self.next = None


if __name__ == "__main__":
    g =Graph(3)
    g.addEdge(1, 0)
    g.addEdge(2, 0)
    g.addEdge(1, 2)
    g.bfs()
    g.print_graph()
