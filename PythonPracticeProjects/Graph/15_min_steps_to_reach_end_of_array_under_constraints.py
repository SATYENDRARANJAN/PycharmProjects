# Reach end under constraint to access next or next-same-valued element
# create an adjacency list with elements and their indeces where they are present
# start from 0 and access next element and n-s-v element i.e. element at index from adjancency list .
# if not visited , vist two options and add them to queue
# set dist +=1
# check if reached end return dist
# check if more than end : return Cant reach
#
from builtins import range, len


def bfs(a,g,N):
    visited=[False for i in range(N)]
    dist =[0 for i in range(N)]
    q=[]
    q.append([a[0],0])
    while(len(q)!=0):
        i = q.pop()
        # append next unvisited same elemebt
        for j in len(range(g[i])):
            if not visited[g[i][j]]:
                visited[g[i][j]]==True
                q.append(g[i][j])
                dist[arr[i]]+=1
                break;
        # append next element
        q.append(arr[i+1])






def getMinStepsToReachEnd(a, N):

    # counting and storing frequency of a  number and its indexes
    g = [[] for i in range(10)]

    # form adjacency list which tells the same element index
    for i in range(N):
        g[a[i]].append(i)

    # BFS
    min_steps = bfs(a,g, N)






if __name__ == "__main__":
    arr = [0, 1, 2, 3, 4, 5, 6, 7, 5, 4, 3, 6, 0, 1, 2, 3, 4, 5, 7]
    N = len(arr)
    print(getMinStepToReachEnd(arr, N))
