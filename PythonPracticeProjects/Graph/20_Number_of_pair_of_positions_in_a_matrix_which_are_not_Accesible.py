# No. of pair of positions = No. of connected nodes in a graph  * No. of disconnected nodes . = Connected node * (Total nodes - connected nodes)

# Algorithm
# Find the total nodes in a graph.
# Start from each vertice
# Find all connected nodes
# Calculate no. of pair of positions only for vertices which are not traversed .


def dfs(graph,N,visited,x,k):
    print(x)
    print (visited)
    for i in range(0,len(graph[x])):
        if not visited[graph[x][i]]:
            visited[graph[x][i]] =True
            print(graph[x][i])
            # print(visited)
            k[0]+=1
            dfs(graph,N,visited,graph[x][i],k)



def countNoOfNonAccessibleNodes(graph, N):
    visited =[False] * N * N
    # k=[1] # by default no. of connected vertices for a single vertex is 1
    ans =0
    for i in range(0,N*N):
        if not visited[i]:
            visited[i]=True
            k = [1]
            dfs(graph,N,visited,i,k)
            ans += k[0] * (N*N - k[0])
            print("ans",ans)
    return ans



def insertpath(graph,N, x1, y1, x2, y2):
    #  Considering each vertex as a cell , Numbering  each cell , total N**2  NUMBER OF ROWS IN GRAPH
    a = ((x1-1)* N+y1)-1
    b = ((x2-1)* N+y2)-1
    graph[a].append(b)
    graph[b].append(a)



if __name__ == "__main__":
    N = 2
    graph = [[] for i in range(N*N)]

    insertpath(graph, N , 1,1,1,2)
    insertpath(graph, N , 1,2,2,2)
    print (graph)

    print(countNoOfNonAccessibleNodes(graph, N))