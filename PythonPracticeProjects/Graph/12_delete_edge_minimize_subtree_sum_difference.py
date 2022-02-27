from builtins import range, len


def dfs(g,node,u,parent,vertex,addChild):
    sum=0
    # print(node , u )
    for i in range(len(g[u])):
        # print("in loop->",g[u][i], u,i)
        if g[u][i]!=parent:
            if u==node:
                sum += dfs(g,node,g[u][i],u,vertex,True)
            else:
                sum += dfs(g, node, g[u][i], u, vertex, addChild)

    if addChild:
        # print("u=={0}: sum:{1}".format(u,vertex[u] + sum))
        return vertex[u] + sum
    else:
        # print("not equal .sum:{0}".format(sum))
        return sum


def subtreeSum1(g,u,vertex):
    if u==0:
        return dfs(g,u,0,-1,vertex,True)
    else:
        return dfs(g,u,0,-1,vertex,False)


def minSubtreeSumDifference1(g,vertex,edges,N):
    totalSum =0
    # total sum
    for i in range(N):
        totalSum += vertex[i]

    print(totalSum)

    minSumDiff=9999999
    # To find the min subtree sum difference
    # we need to calculate Total tree sum - Subtree Sum
    for i in range(N):
        print("for {0} --> {1} - 2 * {2}".format(i,totalSum,subtreeSum(g,i,vertex)))
        sumDiff = abs(totalSum - 2*subtreeSum(g,i,vertex))
        # print(subtreeSum(g,2,vertex))
        if minSumDiff>sumDiff:
            minSumDiff=sumDiff

    return minSumDiff



def subtreeSum(g,u,parent):
    sum=0
    print(g[u], u)
    for i in range(len(g[u])):
        if g[u][i]!=parent:
            sum += subtreeSum(g,g[u][i],u)
    return vertex[u] + sum


# total sum
# for each edge : take its starting and ending index
# now diff =(total_sum - dfs(starting edge))    -   (dfs(starting_Edge))
def minSubtreeSumDifference(g,vertex,edges,N):
    t=0
    min_sum=99999
    # totalsum
    for i in range(N):
        t += vertex[i]

    for edge in edges:
        v1 = edge[0]
        v2=edge[1]
        diff = t - 2* subtreeSum(g,v1,v2)
        print (diff)
        if abs(diff)<min_sum:
            min_sum=abs(diff)

    return min_sum





if __name__=="__main__":
    vertex=[4,2,1,6,3,5,2]
    edges = [[0, 1], [0, 2], [0, 3], [2, 4], [2, 5], [3, 6]]
    N = len(vertex)

    # Create adjacency list with edges
    g =[[] for i in range(N)]
    for i in range(len(edges)):
        g[edges[i][0]].append(edges[i][1])
        g[edges[i][1]].append(edges[i][0])
    print (g)

    print(minSubtreeSumDifference(g,vertex, edges, N))