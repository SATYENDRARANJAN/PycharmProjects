# count ways of fitting 1*m tile into n*m board
# if tile is fit horizontally : then count(n-2) to be calculated as one more will have to be placed horizontally .
# if tile is placed vertically : then count(n-1) to be calculated as one will have to be placed vertically


def count_tiling_m_n(r,c):

    print(r,c)
    if r<c:
        return 1
    if r==c:
        return 2
    if r>c:
        return count_tiling_m_n(r-1,c) + count_tiling_m_n(r-c,c)


def count_tiling_m_n_tabulated(r,c):
    dp = [0 for i in range(r+1)]
    for i in range(r+1):
        if i<c or i==1:
            dp[i] =1
        if i==c:
            dp[i] =2
        if i>c:
            dp[i] = dp[i-c] + dp[i-1]
    return dp[r]


def count_tiling_m_n_memoized(r,c,dpmemo):
    if dpmemo[r]!=0:
        return dpmemo[r]
    if r<c or r==1:
        dpmemo[r]=1
        return 1
    if r==c:
        dpmemo[r]=2
        return 2
    if r>c:
        dpmemo[r]= count_tiling_m_n_memoized(r-1,c,dpmemo) + count_tiling_m_n_memoized(r-c,c,dpmemo)

    return dpmemo[r]




if __name__ == "__main__":
    r =5
    c =2
    dpmemo = [0 for i in range(r+1)]
    # to find tiles of 1*c
    # print(count_tiling_m_n(r,c))
    # print(count_tiling_m_n_tabulated(r,c))
    print(count_tiling_m_n_memoized(r,c,dpmemo))