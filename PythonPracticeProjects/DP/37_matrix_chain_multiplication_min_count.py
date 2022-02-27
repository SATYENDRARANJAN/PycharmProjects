import sys


def count(a,i,j):
    if i ==j :
        return 0

    min_c = sys.maxsize
    for k in range(i , j):
        c = a[i-1] * a[k] * a[j] + count(a,i,k) + count(a, k+1,j)
        if c < min_c:
            min_c = c
    return min_c


def count_dp(a , m, n ):
    dp = [[0 for j in range((n))]for i in range(m)]

    # count will be 0 for all cases when length of matrix is only 1*1 which means only one item present in the dd array
    for i in range(1,n)
        dp[i][i] = 0

    for i in range(m):
        for j in range(n):
            dp[i][j] = a[dp[]



if __name__ == "__main__" :
    global a
    a = [40 , 60 , 20]
    a = [1, 2, 3, 4, 3];

    n = len(a)
    print(count(a,1,n-1))
    print(count_dp(a,1,n-1))