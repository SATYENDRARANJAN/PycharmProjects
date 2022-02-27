from builtins import range, min, len


def editDistance(str1, str2 , m , n ):
    dp = [ [0 for x in range(m+1)] for x in range(2)]
    print(dp)
    for j in range(m+1):
        dp[0][j] =  j
    for i in range(1,n+1):
        for j in range(m+1):
            if j == 0:
                dp[i%2][j] = i
            elif str1[j-1] == str2[i-1]:
                dp[i%2][j] = dp[(i-1)%2][j-1]
            else:
                dp[i%2][j] = 1 + min(min(dp[(i-1)%2][j-1] ,dp[(i-1)%2][j]) ,dp[i%2][j-1])
    print(dp)
    return(dp[((n+1)%2)][m])
if __name__ == "__main__":
    str1 = "sunday"
    str2 = "saturday"
    m = len(str1)
    n = len(str2)
    print(editDistance(str1 ,str2 , m ,n))