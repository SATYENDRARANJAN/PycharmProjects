#  permutation coeff is used to have an ordered subset having k elements from a  set of n elements .
# P(n,k) = P(n-1,k) + k* P(n-1,k-1)
# P(n,k) = n! / (n-k)!

# base case
# P(n,k) =1 if k=0
# P(n,k) =0 if k>n

def perm_coeff(n,k):
    if k ==0 :
        return 1
    if k>n:
        return 0
    a= perm_coeff(n-1,k)
    b= k * perm_coeff(n-1,k-1)
    print (a,b)
    return a+b


def perm_coeff_tabulated(n,k):
    dp =[[0 for j in range(k+1)] for i in range(n+1)]
    for i in range(n+1):
        for j in range(k+1):
            if j ==0:
                dp[i][j] =1
            elif j>i:
                dp[i][j] = 0
            else:
                dp[i][j] = dp[i-1][j] + j* dp[i-1][j-1]
    return dp[n][k]


def perm_coeff_memoized(n,k,dpmemo):
    if n<0 :
        return 0
    if k == 0:
        dpmemo[n][k] =1
        return 1
    if k>n:
        dpmemo[n][k] =0
        return 0
    if dpmemo[n][k] != -1:
        return dpmemo[n][k]
    print (n,k)
    dpmemo[n][k]=perm_coeff_memoized(n-1,k,dpmemo) + k * perm_coeff_memoized(n-1,k-1,dpmemo)
    return dpmemo[n][k]


if __name__ == "__main__" :
    n=5
    k=2
    dpmemo = [[-1 for j in range(k+1)]for i in range(n+1)]
    dpmemo[0][0] =0
    # print(perm_coeff(n,k))
    # print(perm_coeff_tabulated(n,k))
    print(perm_coeff_memoized(n,k,dpmemo))