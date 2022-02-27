# Python3 program to find the minimum numbers
# of moves needed to move from source to
# destination .
from builtins import len, range


class Graph:
    def __init__(self, V):
        self.V = V
        self.adj = [[] for i in range(V)]

    # add edge to graph
    def addEdge(self, s, d):
        self.adj[s].append(d)
        self.adj[d].append(s)

    # Level BFS function to find minimum
    # path from source to sink
    def BFS(self, s, d):

        # Base case
        if (s == d):
            return 0

        # make initial distance of all
        # vertex -1 from source
        level = [-1] * self.V

        # Create a queue for BFS
        queue = []

        # Mark the source node level[s] = '0'
        level[s] = 0
        queue.append(s)

        # it will be used to get all adjacent
        # vertices of a vertex

        while (len(queue) != 0):

            # Dequeue a vertex from queue
            s = queue.pop()

            # Get all adjacent vertices of the
            # dequeued vertex s. If a adjacent has
            # not been visited ( level[i] < '0') ,
            # then update level[i] == parent_level[s] + 1
            # and enqueue it
            i = 0
            while i < len(self.adj[s]):

                # Else, continue to do BFS
                if (level[self.adj[s][i]] < 0 or
                        level[self.adj[s][i]] > level[s] + 1):
                    level[self.adj[s][i]] = level[s] + 1
                    queue.append(self.adj[s][i])
                i += 1

        # return minimum moves from source
        # to sink
        return level[d]


def isSafe(i, j, M):
    global N
    if ((i < 0 or i >= N) or
            (j < 0 or j >= N) or M[i][j] == 0):
        return False
    return True


# Returns minimum numbers of moves from a
# source (a cell with value 1) to a destination
# (a cell with value 2)
def MinimumPath(M):
    global N
    s, d = None, None  # source and destination
    V = N * N + 2
    g = Graph(V)

    # create graph with n*n node
    # each cell consider as node
    k = 1  # Number of current vertex
    for i in range(N):
        for j in range(N):
            if (M[i][j] != 0):

                # connect all 4 adjacent cell to
                # current cell
                if (isSafe(i, j + 1, M)):
                    g.addEdge(k, k + 1)
                if (isSafe(i, j - 1, M)):
                    g.addEdge(k, k - 1)
                if (j < N - 1 and isSafe(i + 1, j, M)):
                    g.addEdge(k, k + N)
                if (i > 0 and isSafe(i - 1, j, M)):
                    g.addEdge(k, k - N)

                # source index
            if (M[i][j] == 1):
                s = k

            # destination index
            if (M[i][j] == 2):
                d = k
            k += 1
            print(g.adj)

    # find minimum moves
    return g.BFS(s, d)


# Driver Code
N = 4
M = [[3, 3, 1, 0], [3, 0, 3, 3],
     [2, 3, 0, 3], [0, 3, 3, 3]]

print(MinimumPath(M))

# This code is contributed by PranchalK
