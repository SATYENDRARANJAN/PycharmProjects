# this problem  is about findign the pair or single instance of a member in an array of members .
# suppose the array is  [1,2,3]
# then solution is :-
# [{1},{2},{3}] , [{1,2} ,3] ,[1,{2,3}] ,[2,{3,1}] , so n = 4

# if a friend is present singly or if a friend is present in pair
# when singly present then f1(n) =f(n-1)
# when in pair f2(n) = (n-1) *f(n-2)
# count  = f1(n) + f2(n)

def find_friends_pairing_count_util(n):
    print("N:",n)
    if n<=2:
        count = n
    if n>2:
        count = find_friends_pairing_count_util(n-1) + (n-1) * find_friends_pairing_count_util(n-2)
    return count


def find_friends_pairing_count(arr):
    n=len(arr)
    return find_friends_pairing_count_util(n)



# tabulated
def find_friends_pairing_count_util_tabulated(n):
    dp =[0 for i in range(n+1)]
    if n<=2:
        return n
    dp[0]=0
    dp[1]  =1
    dp[2] =2
    for i in range(3,n+1):
        dp[i] = dp[i-1] + (i-1) * dp[i-2]
    return dp[n]



#memoixed
def find_friends_pairing_count_util_memoized(n,dp):
    # print(n)
    if n<=2:
        dp[n]=n
        return dp[n]
    elif dp[n] ==-1:
        # print("dp[{0}] =  {1} + {2}".format(n, find_friends_pairing_count_util_memoized(n-1,dp),(n-1) * find_friends_pairing_count_util_memoized(n-2 , dp)))
        dp[n]= find_friends_pairing_count_util_memoized(n-1,dp)  + (n-1) * find_friends_pairing_count_util_memoized(n-2 , dp)
    return dp[n]



if __name__ == "__main__":
    arr =[1,2,3,4]
    print(find_friends_pairing_count(arr))
    print(find_friends_pairing_count_util_tabulated(len(arr)))
    dpmemo = [-1 for i in range(len(arr)+1)]
    print(find_friends_pairing_count_util_memoized(len(arr), dpmemo))


