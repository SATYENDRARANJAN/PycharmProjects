
def count_all_subsequences(a,k):
    n = len(a)
    dp =[[0 for j in range(n+1)] for i in range(k+1)]
    for i in range(1,k+1):
        for j in range(1,n+1):
            dp[i][j] = dp [i][j-1] # when last no is excluded from the nos forming the product
            if a[j-1] <= i and a[j-1]>0:
                dp[i][j] += dp[i//a[j-1]][j-1]+1 # when the last no. is included in the nos. forming the product

    return dp[k][n]





if __name__ == "__main__":
    a=[4,3,2,1]
    k =10
    print(count_all_subsequences(a,k))