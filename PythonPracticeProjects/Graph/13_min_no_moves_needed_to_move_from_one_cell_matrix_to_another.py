from builtins import range, len


def bfs(g,N,s,d,dist):
    q=[]
    q.append(s)
    path=[]
    parent=[-10 for i in range(N*N)]
    parent[s]=-1
    dist[s] =0
    path.append(s)
    print(g)
    while(len(q)!=0):
        i = q.pop()
        print("Popping:",i)
        j=0
        for j in range(len(g[i])):
            print("  Traverse ",g[i][j])
            if dist[g[i][j]]==-1 or dist[g[i][j]]>dist[i]+1:
                parent[g[i][j]]=i
                print(  dist[g[i][j]]  ,dist[i]+1    )
                dist[g[i][j]] = dist[i]+1
                q.append(g[i][j])

    print (parent)

    # printing path
    path=[]
    path.append(d)
    node =parent[d]
    while(node!=-1):
        path.append(node)
        node=parent[node]
    print(path)
    return dist[d]

def min_moves_util(g,N , s, d,dist):
    return bfs(g,N,s,d,dist)




# form adjacency list using the array .
# traverse bfs and  record level at each move
# Question is whether recording min level is important or bfs by default will move according to the min level
def min_moves(a , N):
    k= 0
    s=0
    d=0

    dist =[-1 for i in range(N*N)]
    # form adjacency list
    g=[[] for i in range(N*N)]
    for i in range(N):
        for j in range(N):

            if does_exist(a,i,j-1):
                g[k].append(k-1)
                g[k-1].append(k)
                print("1",i, j, g)
            if does_exist(a,i,j+1):
                g[k].append(k+1)
                g[k+1].append(k)
                print("2",i, j, g)
            if does_exist(a,i-1,j) and i>0 : # i>0 or k>N
                g[k].append(k-N)
                g[k-N].append(k)
                print("3",i, j, g)
            if does_exist(a,i+1,j) and j<N-1:
                g[k].append(k+N)
                g[k+N].append(k)
                print("4",i, j, g)

            # find source
            if a[i][j]==1:
                s=k
            # find destination
            if a[i][j]==2:
                d=k
            k=k+1
            print(" ")

    print("source:{0} dest:{1} k:{2}".format(s,d,k))

    # find min moves
    print(min_moves_util(g,N,s,d,dist))


def does_exist(a, i , j):
    if i<0 or j <0 or j>N-1 or i>N-1 or a[i][j]==0:
        return False
    return True


if __name__=="__main__":
    a = [[3 , 3 , 1 , 0 ], [3 , 0 , 3 , 3 ],
     [2 , 3 , 0 , 3 ], [0 , 3 , 3 , 3]]
    N =4

    min_moves(a, N )