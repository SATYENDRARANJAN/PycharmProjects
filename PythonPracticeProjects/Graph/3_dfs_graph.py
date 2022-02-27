from builtins import max, list
from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self,u , v):
        self.graph[u].append(v)


    # TC: O(V+E)  , SC =O(V)
    # Handles only connected graph
    def DFS(self,v):
        # start from vth vertex
        visited = [False]  * (max(self.graph) + 1)
        self.DFSUtil(v,visited)


    # TC: O(V+E)  , SC =O(V)
    # Handles also  disconnected graph
    def DFS_disconnected(self):
        v = (max(self.graph) +1)
        visited = [False] * v

        for i in range(v):
            if not visited[i]:
                self.DFSUtil(i , visited)

    def DFSUtil(self,v,visited):
        visited[v] = True
        print(v, end ='  ')

        for i in self.graph[v]:
            if not visited[i]:
                self.DFSUtil(i,visited)



if __name__ == "__main__":
    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)

    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    # g.addEdge(2, 3)
    g.addEdge(3, 3)

    g.DFS(0)
    print("")
    g.DFS_disconnected()