# find the matrix



from math import sqrt

def min_dist_util(a,v,g,visited,list,m,n,dist):
    print("       " ,"for {0} and {1}".format(m,n) )
    visited[m]=True
    visited[n]=True
    list.append([m,n])
    print("               " ,visited)
    print("               " ,list)
    dist = g[m][n]
    print("               " ,dist)
    min_child_dist=9999
    child_added=False
    for i in range(v):
        for j in range(i,v):
            if i!=j and not visited[i]:
                if not visited[j]:
                    child_dist = min_dist_util(a,v,g,visited,list,i,j,dist)
                    if (child_dist<min_child_dist):
                        min_child_dist = child_dist
                        child_added=True
    if child_added:
        return dist+min_child_dist
    else:
        return dist


def find_min_dist(a,v,g,visited,list):
    # visit all neighbours of root
    # pair it with each neighbour :-- call min_dist_util() -- pass local array "visited[]" to each call .
    # mark the edge visited -- add it to the list -- and store the total sum
    # and pass everything to a call again
    min_d=999999
    for i in range(v):
        for j in range(i+1,v):
            print("******************** Starting for {0} and {1} ************************".format(i,j))
            visited = [False for i in range(v)]
            list = []
            dst = min_dist_util(a,v,g,visited,list,i,j,0)
            print("               dst for {0} and {1} = {2}".format(i,j,dst))
            if min_d >dst :
                min_d = dst
    return (min_d)


if __name__=="__main__":
    #  input vertices .
    # a = [[1.0, 1.0], [5.0, 2.0], [4.0, 3.0], [3.0, 3.0]]
    # a =[[2.0, 3.0], [5.0, 6.0]]
    a=[[8, 6], [6, 8], [1,3], [1, 1]]
    # form adjacency matrix for the given vertices
    V = len(a)
    visited = [False for i in range(V)]
    g =[[0 for j in range(V)]for j in range(V)]

    # Calculating dist from each vertex to other vertex and saving in g array
    for i in range(V):
        for j in range(0,V):
                g[i][j] = sqrt((a[i][0]-a[j][0])**2 + (a[i][1]-a[j][1])**2)
    list =[]
    # finding min dist of vertex starting from 0
    d = find_min_dist(a,V,g,visited,list)
    print("Answer is " ,d)



