# find the shortest path from source to all vertices in a given graph
# The graph may contain negative weight edges .
# Djikstra - Greedy = O(VLOGV) (with use of fibonacci heap )

# Djikstra doesnt work for graph with negative weight edges .
# Bellman Ford( 0(VE))

# Input - Graph and sourvce vertex src
# Output - Shortest distance from src to all vertex .
#        - If there is a negative weight cycle then shortest dist is not calculated and  An "error" is ouputted -"NEGATIVE WEIGHT CYCLES PRESENT"

# Algo :
# Initialize all edges dist in dist =[] as 0 for src , INF for others .
# Calculate shortest distance  from each vertex to each vertex now  . Do following (|v|-1) times  where |v| is the no. of vertices in the graph.
#   for each edge e :
#       1..  if dist[v] > dist[u]+ weight ([u,v])
#                 dist [v] = dist[u] +  weight([u,v])
# This step reports if there is a negative weight edge cycle in the graph .
#           for each edge u-v
#               if dist[v] > dist[u] + weight(u,v)
#                   "GRAPH HAS NEGATIVE WEIGHT CYCLES"
#

# like any other dynamic programming problem, the algorithm calculates shortest path in a bottom up manner
#   1st iteration gives shortest path which are atmost 1 edge long .
#   2nd iteration gives shortest pathe which are atmost 2 edge long .
#   ...
#   vth iteration gives shortest path which are atmost 3 edge long .

# The standard Bellman-Ford algorithm reports the shortest path only if there are no negative weight cycles.
# Modify it so that it reports minimum distances even if there is a negative weight cycle.


class Graph:
    def __init__(self,vertices):
        self.V = vertices
        self.graph = []

    def addEdge (self , u  , v , w):
        self.graph.append([u,v,w])


# The function finds shortest path from src to all vertices using Bellman Ford algorithm
# The function also detects negative edge cycle.
def BellmanFord(self, src):
    # Step 1: Initialize dist from src to all other vertices as INF
    dist = [float("INF")] * self.V
    dist[src] = 0

    # Step 2 : Relax all edges |V|-1 times .  A simple shortest path from src to any other vertex can have atmost |v|-1 edges .
    for count in range(self.V-1):
        # Update dist values and parent index of adjacent vertices of the picked vertex.
        # Consider only those vertices which are still in queue .
        for u,v,w in self.graph:
            if dist[u]!= float("inf") and  dist[u] + w < dist[v] :
                dist[v] = dist[u] + w

    # Step 3 : Detecting negative weight cycles .
    for u,v,w in self.graph:
        if dist[u] != float("inf") and dist[u] + w < dist[v]:
            print("Graph contains negative weight cycles ")

    # dist[] stores the shortest distances to all vertices .
    print(dist)


if __name__ == "__main__":
    g = Graph(5)
    g.addEdge(0, 1, -1)
    g.addEdge(0, 2, 4)
    g.addEdge(1, 2, 3)
    g.addEdge(1, 3, 2)
    g.addEdge(1, 4, 2)
    g.addEdge(3, 2, 5)
    g.addEdge(3, 1, 1)
    g.addEdge(4, 3, -3)

    # Print the solution
    g.BellmanFord(0)