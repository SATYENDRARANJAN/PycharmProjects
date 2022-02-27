# C(n,k) = C(n-1,k-1) + C(n-1,k)
# O(N*K) for binomial_coeff
# O N^2 for recursive



def binomialcoeff(n,k):
    if k==0 or k==n :
        return 1
    return binomialcoeff(n-1,k-1) + binomialcoeff(n-1,k)


def binomialcoeff_tabulated(n,k):
    dp =[[-1 for j in range(k+1)]for i in range(n+1)]
    for i in range(n+1):
        for j in range(min(i,k) + 1):
            if j==0 or i==j:
                dp[i][j] =1
            else:
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
    return dp [n][k]


def binomial_coeff_memoization(n,k,dpmemo):
    if dpmemo[n][k]!= -1:
        return dpmemo[n][k]
    if k == 0 or k ==n :
        dpmemo[n][k]= 1
        return 1
    dpmemo[n][k] = binomial_coeff_memoization(n-1,k-1,dpmemo) + binomial_coeff_memoization(n-1,k,dpmemo)
    return dpmemo[n][k]


if __name__ == "__main__":
    n=5
    k=2
    dpmemo = [[ -1 for j in range(k+1)]for i in range(n+1)]
    print(binomialcoeff(5,2))
    print(binomialcoeff_tabulated(5,2))
    print(binomial_coeff_memoization(n,k,dpmemo))