# This problem is about finding whether the value k exists in the arr and its subset sum
# to find whether a subset with sum k exists or not arr = [1,2,3,5,8,9]  , k =16
# when the last element in the list not included ; then ispresent = does_subset_sum_exists(arr,n-1,k)
# when the last element in the list is not excluded : then ispresent = does_subset_sum_exists(arr,n-1,k-arr[n-1])


def subset_util(arr , l , k):

    if l==0:
        if k ==0 :
            return True
        if k !=0:
            return False
    if l!=0:
        if k ==0:
            return True
        if k !=0 :
            return subset_util(arr , l-1 , k) or  subset_util(arr, l-1,k-arr[l-1])



def find_subset_exists(arr, k):
    l = len(arr)
    if l ==0  and k ==0 :
        return True
    if k ==0 :
        return True
    return subset_util(arr,l-1,k) or subset_util(arr,l-1,k-arr[l-1])


def does_subset_exists_tabulated(arr , k ):
    l = len(arr)
    dp =[[False for j in range(k+1)]for i in range(l+1)]

    for i in range(l+1):
        for j in range(k+1):
            print(i,j)
            if i ==0 and j ==0 :
                dp[i][j]=True
            if i==0 and j !=0 : # sum is 0
                dp[i][j] = False
            if i!=0 and j ==0 :
                dp[i][j] = True
            if i!=0 and j !=0:
                print("{0} or {1}".format( dp[i-1][j] ,dp[i-1][j-arr[i-1]]))
                dp[i][j] = dp[i-1][j] or dp[i-1][j-arr[i-1]]

    return dp[l][k]


def does_subset_exists_memoized(arr, n, k,dpmemo ):
    print (n ,k)
    if n==0:
        if k ==0 :
            return True
        elif k !=0:
            return False
    if n!=0:
        if k ==0:
            return True
        if k !=0:
            if dpmemo[n][k] != False:
                return dpmemo[n][k]
            dpmemo[n][k] =  does_subset_exists_memoized(arr,n-1,k,dpmemo) or does_subset_exists_memoized(arr, n-1,k-arr[n-1],dpmemo)
    return dpmemo[n][k]


def print_dd(arr, n, k):
    print("dd is ******************")
    for i in range(n):
        for j in range(k):
            print (arr[i][j] ,end = "     ")
        print ()



def subset_sum(arr, n, k ):
    dp = [[0 for i in range(k+1)] for j in range(2)]
    print_dd(dp,2,k+1)
    print("n,k is :")
    print(n,k)
    for i in range(n+1):
        for j in range(k+1):
            print(i,j)
            if i==0 :
                if j==0:
                    dp[i%2][j] = True
                    # return True
                else :
                    dp[i%2][j] = False
                    # return False
            if i!=0:
                if j==0:
                    dp[i%2][j] =True
                    # return True
                if j!=0:
                    if i%2 ==0:
                        print("i%2:{0}".format(i%2))
                        print("arr[i%2+1]:{0}".format(arr[i%2+1]))
                        if j<arr[i%2+1]:
                            dp[i % 2][j] = dp[i % 2 + 1][j]
                        else:
                            dp[i%2][j] = dp[i%2+1][j] or dp[i%2+1][j-arr[i-1]]
                    else:
                        print("i%2:{0}".format(i%2))
                        print("arr[i%2-1]:{0}".format(arr[i-1]))
                        if j < arr[i-1]:
                            print("dp[i%2+1][j] :{0}".format(dp[i % 2 - 1][j]))
                            dp[i % 2][j] = dp[i % 2 - 1][j]
                        else:
                            print("dp[i%2-1][j] :{0}".format(dp[i%2-1][j]))
                            print("dp[i%2-1][j-arr[i%2-1]]:{0}".format(dp[i%2-1][j-arr[i-1]]))
                            dp[i%2][j] = dp[i%2-1][j] or dp[i%2-1][j-arr[i-1]]
            print_dd(dp,2,k+1)

    # if n%2==0:
    #     return dp[n%2][k]
    # else:
    return dp[n%2][k]




if __name__ == "__main__":
    arr =[1,3,8,6,4]
    k=89
    # print(find_subset_exists(arr, k))
    # print(does_subset_exists_tabulated(arr, k))
    l = len(arr)
    dpmemo =[[False for j in range(k+1)] for i in range(l+1)]
# 1    print(does_subset_exists_memoized(arr,l,k,dpmemo))
    print(subset_sum(arr , l , k ))
