# tiling 2*1 tile into a 2*n space
# if first tiles is  placed horizontally ,then second tiles will also be placed horizontally
# if first tiles is placed vertically , then second tiles will also be placed vertically .

def count_tiling_ways(n):
    if n<0:
        return 0
    if n ==1 or n==2:
        return n
    else:
        return count_tiling_ways(n-1) + count_tiling_ways(n-2)


# count tiling ways tabulated  : bottoms up
def count_tiling_ways_tabulated(n):
    dp = [0 for i in range(n+1)]
    print ("i : ",n)
    if n<2:
        return n
    dp[0] =0
    dp[1] =1
    dp[2] =2
    for i in range(3,n+1):
        dp[i] = dp[i-1]+dp[i-2]
    return dp[n]



def count_tiling_ways_memoized(n,dpmemo):
    if n<2:
        dpmemo[n] =n
        return n
    if dpmemo[n] !=-1:
        return dpmemo[n]
    dpmemo[n] = count_tiling_ways_memoized(n-1,dpmemo) + count_tiling_ways_memoized(n-2  , dpmemo)
    return dpmemo[n]




if __name__ == "__main__":
    for i in range(7):
        dpmemo = [-1 for i in range(i + 1)]

        # print(count_tiling_ways(i))
        # print(count_tiling_ways_tabulated(i))
        print(count_tiling_ways_memoized(i , dpmemo))