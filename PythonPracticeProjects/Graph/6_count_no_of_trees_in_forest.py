# To find the no. of trees in the forest , we DFS on a node and increment count by 1
# Visit one of the remaining vertices now till each of them is visited .
# Total count is the no of trees in a forest


def addEdge(adj,u,v):
    adj[u].append(v)
    adj[v].append(u)



def DFSUtil(adj , visited, i):
    visited[i] =True
    for j in range(len(adj[i])):
        if visited[adj[i][j]] == False:
            visited[adj[i][j]]=True
            DFSUtil(adj , visited, j)



def countTrees(adj,V):
    visited =[False] * 5
    count =0
    for i in range(V):
        if visited[i] == False:
            DFSUtil(adj,visited,i)
            count +=1
    return count







if __name__ == "__main__":
    V=5
    adj = [[]  for i in range(V)]
    addEdge(adj, 0 , 1)
    addEdge(adj , 0, 2)
    addEdge(adj , 3, 4)
    print(countTrees(adj,V))