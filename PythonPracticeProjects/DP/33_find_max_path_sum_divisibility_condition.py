# to find the max path sum where each consecutive index in path is divisible by the previous index .
# Complexity = O(n* sqrt(n))

def max_path_sum(a , n):
    dp = [0] * n
    if n ==0 : return 0
    dp[0] = a[0]
    if n == 1 :
        dp[0] = a[0]
        return dp[0]
    x = 0
    for i in range(1, n):
        maxsum = 0
        for j in range(0 , int((i)**0.5)+1):
            if (i+1) % (j+1)==0:
                if dp[j]>maxsum:
                    maxsum = dp[j]
                    x = j+1
        dp[i] = max(maxsum,a[i] + dp[(x-1)])
    print(dp)
    return dp[n-1]





if __name__ == "__main__":
    arr = [2, 3,9,9,16,9,9,9,9]
    n = len(arr)
    print(max_path_sum(arr, n))

