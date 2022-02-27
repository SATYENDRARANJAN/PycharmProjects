# In this problem if the count of coin is changed into smaller parts like 10 is divided into (1,2, 3, 5], then :
# how many ways can we make the change in the infinite supplies of [1,2,3,5]
# N=4 , S={1,2,3}
#
# ways to change n Rs = f()
# for mth coin : if coin Sm  is included  atleast once :- S(m-1, n)
# for mth coin : if coin Sm is not included :- S(m,m-Sm)


def count(arr, m , n):
    #base cases
    # print (arr , m)
    if n==0 :
        return 1
    if n <0 :
        return 0
    elif m <= 0 and n >=1:
        return 0

    # print("{0} = {1} + {2}".format(count(arr , m-1 , n) + count(arr , m-1, n-arr[m-1]) , count(arr , m-1 , n),count(arr , m-1, n-arr[m-1])))
    c  = count(arr , m-1 , n) + count(arr , m, n-arr[m-1])
    # print (c)
    return c


# complexity = O(mn)
def count_tabulated(arr , m , n ):
    dp = [[0 for i in range(n+1)] for j in range(m+1)]
    if n ==0 : return 1
    if n <0 : return 0
    if n >0 :
        if m<0:return 0
        if m==0: return 0
    # print(m, n)
    for i in range(m+1): # arr element count
        for j in range(n+1): #
            # print(i,j)
            if i == 0 and j==0:
                dp[i][j] = 1
            elif i ==0 :
                dp[i][j] = 0
            elif j == 0 :
                dp[i][j] = 1
            else:
                # print("{0} = {1} + {2}".format(dp[i][j]  ,  dp[i-1][j]  , dp[i][j-arr[i-1]]))
                dp[i][j] = dp[i-1][j] + dp[i][j-arr[i-1]]
    return dp[m][n]



# count memoized (O(mn))
def count_memoized(arr , m , n , dpmemo):
    if n==0 :
        dpmemo[m][n] =1
    elif n<0:
        dpmemo[m][n] =0

    elif n>0:
        if m < 0 : return 0
        if m == 0:
            dpmemo[m][n] = 0
            return 0
        if m > 0:
            if dpmemo[m][n] !=0:
                return dpmemo[m][n]
            # print("{0} = {1} +{2}".format(dpmemo[m][n] ,dpmemo[m-1][n] , dpmemo[m][n-arr[m-1]]  )  )
            dpmemo[m][n] =count_memoized(arr,m-1,n,dpmemo) + count_memoized(arr,m,n-arr[m-1],dpmemo)
    return dpmemo[m][n]




if __name__ == "__main__":
    n = 10
    arr = [2,5,3,6]
    m = len(arr)
    print(count(arr , m  ,n))
    print(count_tabulated(arr,m,n))
    dpmemo =[[0 for i in range(n+1)] for j in range(m+1)]
    print(count_memoized(arr, m , n,dpmemo ))