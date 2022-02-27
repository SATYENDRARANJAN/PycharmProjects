
# 2,3,4,5,6
#RECURSIVE
def find_largest_subset_divisible_pair_util(arr,n):
    if n ==0 :
        return 0,[]
    list =[]
    maxm =0
    max_ind =0
    list.append(arr[n - 1])
    maxlist =[]
    for i in range(n-2,-1,-1):
        if arr[n-1]%arr[i] == 0:
            l = find_largest_subset_divisible_pair_util(arr, i+1)
            if maxm <= l[0]:
                maxm = l[0]
                maxlist = l[1]
                max_ind = i
    maxm = 1+maxm
    return maxm,list+maxlist

def find_largest_subset_divisible_pair(arr , n ):
    dp =[0 for i in range(n)]
    for i in range(n,0,-1):
        print("STARTING FOR :",i-1,arr[i-1])
        dp[i-1] = find_largest_subset_divisible_pair_util(arr,i)
    print("dp:",dp)


#DP
def find_largest_subset_divisible_pair_dp(arr,n):
    dp = [0 for i in range(n+1)]
    dp[n-1] =1
    mxm =0
    # for i in range(n-2,-1,-1):
    #     if arr[n-1] % arr[i] ==0:
    #         dp[i] = max(mxm,dp[i])

    dp[0]=0
    for i in range(0,n):
        mxm=0
        for j in range(i-1,-1,-1):
            if arr[i] % arr[j] ==0:
                mxm =max(mxm,dp[j])
        dp[i] = 1+mxm
    print("dp:",dp)


#MEMOIZATION
def find_largest_subset_divisible_pair_memo(arr,n):
    dpmemo = [0 for i in range(n)]
    for i in range(n-1,-1,-1):
        dpmemo[i] = find_largest_pair_memo_util(arr,i,dpmemo)
    print("dpmemo : ",dpmemo)


def find_largest_pair_memo_util(arr, n,dpmemo): # here n is subscript
    # print(n, dpmemo)
    if n ==0:
        dpmemo[0]=1
        return 1
    if dpmemo[n]==0:
        mxm =0
        for i in range(n-1,-1,-1):
            # print("
            # i:",i,arr[n],arr[i])
            if arr[n] % arr[i] == 0:
                # print("find_largest_pair_memo_util(arr,n-1,dpmemo) :",find_largest_pair_memo_util(arr,i,dpmemo))
                mxm = max(mxm,find_largest_pair_memo_util(arr,i,dpmemo))
                # print("mxm:",mxm)
        dpmemo[n] = 1 + mxm
    return dpmemo[n]






if __name__ == "__main__":
    arr = [1,3,4,5,6,12,9,18,15]
    arr.sort()
    print(arr)
    # print(find_largest_subset_divisible_pair(arr , len(arr)))
    print(find_largest_subset_divisible_pair_dp(arr , len(arr)))
    print(find_largest_subset_divisible_pair_memo(arr , len(arr)))
    print(arr)