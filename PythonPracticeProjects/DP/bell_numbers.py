# Let S(n, k) be total number of partitions of n elements into k sets. The value of nth Bell Number is sum of S(n, k) for k = 1 to n.
# no of ways of partitioning a set
# S(n+1, k) = k*S(n, k) + S(n, k-1)
# When we add a (n+1)’th element to k partitions, there are two possibilities.
# 1) It is added as a single element set to existing partitions, i.e, S(n, k-1)
# 2) It is added to all sets of every partition, i.e., k*S(n, k)

# when we add n+1 th element to k partitions , there are 2 possibilities
# it is added as a single element set to existing partition .S(N,K-1)
# it is added to all sets of every partition .K * S(N,K)

# S(n+1, k) = k*S(n, k) + S(n, k-1)
# S(n, k) is called Stirling numbers of the second kind

#Question : Count no. of ways to partition a set in k subsets .

# a python program to find no. of partitions of n elements into k subsets .
# N=2 , K =2
# N=3 , K =5
# N=4 , K =15

# S(n+1, k) = k*S(n, k) + S(n, k-1)
# S(4,K) =  K * S(3,K)

def find_partitions_for_n_elements_into_k_subsets(n,k):
    if (n==0 or k ==0 or k>n):
        return 0
    if (k ==1 or n==k):return 1
    c= k * find_partitions_for_n_elements_into_k_subsets(n-1,k) + find_partitions_for_n_elements_into_k_subsets(n-1,k-1)
    return c


# # from the bell triangle
# def find_partitions_for_n_elements_into_k_subsets_tabulated(n,k):
#     bell  =  [[0 for i in range(n+1)]for j in range(n+1)]
#
#     if n==0 or k==0 or k>n:
#         return bell[n][k]
#     if (k==1 or n==k): return 1
#     if bell[n][k] == 0:
#         bell[n][k] = k * bell[n-1][k] + bell[n-1][k-1]
#     return bell[n][k]


# from the bell triangle
def find_partitions_for_n_elements_into_k_subsets_tabulated(n,k):
    bell  = [[0 for i in range(k+1)]for j in range(n+1)]

    for i in range(k+1):
        bell[0][i] = 0

    for j in range(n+1):
        bell[j][0] = 0

    for i in range(1,n+1):
        for j in range(1,k+1):
            if (j==1 or i == j):
                bell[i][j] = 1
            else:
                bell[i][j] = j* bell[i-1][j] + bell[i-1][j-1]

    printdd_arr(bell,n,k)

def printdd_arr(dp,n,k):
    for i in range(0, n):
        list  =[]
        for j in range(0, k):
            list.append(dp[i][j])
            if i==j:
                print("bell nos.: {0}".format( dp[i][j]))
# 1
# 1 2
# 2 3 5
# 5 7 10 15
def find_partitions_for_n_elements_into_k_subsets_from_bell_nos(n,k):
    dp=[[0 for i in range(n+1)] for j in range(k+1)]
    dp[0][0]= 1
    for i in range(1,n):
        for j in range(0,k):
            print("{0} .. {1}".format(i ,j) )
            if j ==0 :
                dp[i][j]= dp[i-1][i-1]
            elif j<=i:
                print(dp[i-1][j],dp[i-1][j-1])
                dp[i][j] = dp[i][j-1] + dp[i-1][j-1]
    printdd_arr(dp,n,k)
    return dp[i][j]




if __name__ == '__main__':
    n=5
    k=5
    print(find_partitions_for_n_elements_into_k_subsets_tabulated(n,k))
    print(find_partitions_for_n_elements_into_k_subsets_from_bell_nos(n,k))


