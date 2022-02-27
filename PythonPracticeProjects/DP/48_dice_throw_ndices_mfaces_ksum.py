# 1-1,6
# 2-1,6
# 3-1,6
# sum(x,n) -> sum(x-1,n-1)  -> sum(x-1-1,n-2) --------------- sum(x-1,1)
#                              sum(x-1-2,n-2)
#                              sum(x-1-3,n-2)
#                              sum(x-1-4,n-2)
#                              sum(x-1-5,n-1)
#                              sum(x-1-6,n-1)
#             sum(x-2,n-1)  -> sum(x-2-1,n-2)
#                              sum(x-2-2,n-2)
#                              sum(x-2-3,n-1)
#                              sum(x-2-4,n-1)
#                              sum(x-2-5,n-1)
#                              sum(x-2-6,n-1)
#             sum(x-3,n-1)  -> sum(x-3-1,n-2)
#                              sum(x-3-2,n-2)
#                              sum(x-3-3,n-2)
#                              sum(x-3-4,n-2)
#                              sum(x-3-5,n-2)
#                              sum(x-3-6,n-2)
#             sum(x-4,n-1)
#             ...
#             sum(x-6,n-1)

# To find sum 'x' with n dices where every dice has m faces .
# frist draw the tree to reach edge cases .
from builtins import range


def findways(n,x):
    print(n,x)
    if n ==0 and x==0: return 1
    # if n ==1 and x<m: return x
    if x<0: return 0
    ways =0
    for i in range(1,m+1):
        # if x-i>0 :
        ways += findways(n-1,x-i)
    return ways

def print_dd_array(a, m, n):
    for i in range(m):
        for j in range(n):
            print(a[i][j],end=" ")
        print("")

def findways_dp(n,x):
    # rows - i - sum
    # columns - j - number of dices
    dp = [[0 for j in range(n+1)] for i in range(x+1)]
    dp[0][0]=1
    for i in range(1,m+1):
        dp[i][1] =1
    for i in range(x+1):
        for j in range(2,n+1):
            for k in range(1,m+1):
                if i>=k:
                    dp[i][j] += dp[i-k][j-1]
    print_dd_array(dp,x+1,n+1)
    print(dp[x][n])


m =6
if __name__=="__main__":
    print(findways(3,8))
    print(findways_dp(3,8))