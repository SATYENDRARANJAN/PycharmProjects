# Find the lvl of each node in a tree from source node using BFS

import queue

class Graph:
    def __init__(self,v):
        self.V=v
        self.adj = [[]  for i in range(v)]

    def addEdge(self,u , v):
        self.adj[u].append(v)
        self.adj[v].append(u)

    def printLevels(self,item):
        # array to store level of each node
        level = [None] * self.V
        visited = [False] * self.V
        que = queue.Queue()
        que.put(item)
        # initialize level of source node to 0
        level[item] = 0
        while(not que.empty()):
            x = que.get()
            for i in range(len(graph[x])):
                adj_node = graph[x][i]
                if not visited[adj_node]:
                    que.put(adj_node)
                    level[adj_node]=level[x]+1
                    visited[adj_node]=True
        # printing levels
        for i in range(self.V):
            print(" ",i,"-->",level[i])






if __name__=="__main__":
    graph = Graph(8)
    graph[0].append(1)
    graph[0].append(2)
    graph[1].append(3)
    graph[1].append(4)
    graph[1].append(5)
    graph[2].append(5)
    graph[2].append(6)
    graph[6].append(7)
    # call levels function with source as 0
    graph.printLevels( 0)