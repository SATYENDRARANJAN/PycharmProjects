from builtins import range, len, max


def dfs(g ,v , u , parentVertex , max_length_with_root_as_end):

    max_length_without_root_as_end=0
    length_max_1_with_root_as_end = length_max_2_with_root_as_end = 0

    for i in range(len(g[u])):
        if g[u][i] != parentVertex:
            length_without_root = dfs(g,v, g[u][i],u,max_length_with_root_as_end)
            # max length without root from different edges from root
            max_length_without_root_as_end = max(length_without_root,max_length_without_root_as_end)

            # Now get the max length including root of 2 neighbour edges
            if (length_max_1_with_root_as_end < max_length_with_root_as_end[0]):
                length_max_2_with_root_as_end = length_max_1_with_root_as_end
                length_max_1_with_root_as_end = max_length_with_root_as_end[0]
            elif length_max_2_with_root_as_end < max_length_with_root_as_end[0]:
                length_max_2_with_root_as_end = max_length_with_root_as_end[0]

    max_length_with_root_as_end[0] = length_max_1_with_root_as_end +1
    a= max(max_length_without_root_as_end,(length_max_1_with_root_as_end+length_max_2_with_root_as_end))
    return a

def max_prod_non_intersecting_paths(g, v ):
    # for each edge in the adjacency list , remove it
    # do dfs from each of its ends
    # figure out the max_length_edge_without_root and max_length_edge_from_root
    # find the max length edge
    max_dist=0
    max_path_1_length=0
    max_path_2_length=0
    path_1_length=0
    path_2_length=0
    res=0
    for i in range(v+1):
        for j in range(len(g[i])):
                max_length_with_root_as_end=[0]
                path_1_length = dfs(g,v,g[i][j],i,max_length_with_root_as_end)

                max_length_with_root_as_end=[0]
                path_2_length = dfs(g,v,i,g[i][j],max_length_with_root_as_end)
                res= max(res,path_1_length*path_2_length)

    print("Max product :" ,res)
    return res



if __name__ == "__main__":
    edges = [[8, 9],[1,9], [1,10],[10,11],[2, 6], [3, 1], [5, 3], [7, 8],[7,12],[12,7], [8, 4], [8, 6]]
    n = len(edges)
    v = n+1
    # adjacency list for graph
    g =[[] for i in range(v+1)]
    for i in range(n):
        g[edges[i][0]].append(edges[i][1])
        g[edges[i][1]].append(edges[i][0])

    print(max_prod_non_intersecting_paths(g, v ))