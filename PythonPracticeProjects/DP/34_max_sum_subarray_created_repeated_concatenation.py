


def max_sum_subarray_created_repeated_concatenation(a , n , k):
    dp = [ [0 for j in range(k) ] for i in range(n) ]
    sum = 0
    for i in range(n):
        for j in range(k):
            dp[i][j] = max( max (dp[i-1][j] + a[i],dp[i-1][j]), 0 )
    print(dp[0])
    return dp[n-1][k-1]





if __name__ == "__main__":
    a = [10, 20, -30, -1]
    n = len(a)
    k = 3
    print(max_sum_subarray_created_repeated_concatenation(a,n,k))