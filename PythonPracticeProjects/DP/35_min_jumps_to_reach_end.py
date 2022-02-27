# In this program , we basically need to calculate minimum no. of junmps to reach the end.
# The jumps are such that at the ith position , mext move can be to the a[i]th subscripts ahead .

#
# def min_jumps_from(a, m, n, sum_till_now, length_till_now):
#     # print( " LOOP : ", m, n, sum_till_now, length_till_now)
#     if sum_till_now >= 11:
#         return length_till_now
#     if m > n :
#         return length_till_now
#     min_length_till_now = 99999
#     print( " m= " ,m)
#     print(" " * m*10,"Indexes:" , m, m+a[m])
#     print(" " * m*10,"Values :" , a[m], a[m+a[m]])
#     for j in range(m+1 , m + 1 + a[m]):
#             # print(" " * j*10 ,"min_jumps_from({0}, j:{1} , n:{2}, {3} , {4})".format(a[j], j , n, sum_till_now + a[j] , length_till_now + 1) )
#             print("*** length for {0}th  is {1}".format(j , min_jumps_from(a, j, n, sum_till_now + a[j], length_till_now + 1)))
#             length_j = min_jumps_from(a, j, n, sum_till_now + a[j], length_till_now + 1)
#             if length_j < min_length_till_now :
#                 min_length_till_now = length_j
#             print(" " * j * 10,"Returning : ", min_length_till_now)
#     return min_length_till_now
#
#
#
# Time coplexity O(n^2) .  Space complexity : O(n)
def min_jumps_from(a, m, n, sum_till_now, length_till_now):
    if n==0:
        return 1

    if m > n :
        return length_till_now

    if a[m] == 0:
        if sum_till_now > n:
            return length_till_now
        return 999

    sum_till_now += a[m]
    length_till_now += 1
    min_jumps = 99999

    for j in range(m+1, m+1+a[m]):
        print(" " * m * 5  , m, j, sum_till_now, length_till_now)
        jumps_from_j =  min_jumps_from(a, j, n, sum_till_now, length_till_now)
        # print (" " * m * 5 ,jumps_from_j , m, j)
        if jumps_from_j < min_jumps :
            min_jumps = jumps_from_j
    if min_jumps == 999 or min_jumps == 99999:
        return 999
    print(" " *m*5 , min_jumps)
    return min_jumps

# DP SOL
# At each step we find out the min_jumps_from_(i) . and  it's value is repeatedly resolved as same elements is overlapped in
# for k --> 1 to a[k] , then for k+1 --> 1 to a[k+1]
# So the problem involves , optimal substructure and a overlapping subproblem
# We need to find max sum in min jumps .
# max_sum_from_(i)=  max( max_sum_from_(j) from (i to i + a[i] , i < n)) + a[i]
# dp[i] =  if j+arr[j] < i : dp[i] = min(dp[j]+1 , dp[i])
def min_jumps_dp(arr , m , n):
    dp = [99999 for i in range(n)]

    if n == 0:
        return 99999

    if  arr[0] == 0:
        return 99999
    dp[0]=0
    for i in range(1,n):
        for j in range(0,i):
            print(" " *i*j , j+a[j], i)
            if (j+a[j]) >= i :
                print("dp[{0}] =  min({1},{2})".format(i,dp[j]+1,dp[i]))
                dp[i] = min(dp[j]+1,dp[i])
    print (dp)
    return dp[n-1]

if __name__ == "__main__":
    a  = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
    # a = [2,0]
    # a= [1, 3, 0, 0, 0, 3, 6, 8, 9, 5]
    n = len(a)
    jumps_from_0 = min_jumps_from(a, 0, n-1, 0, 0)
    print("val : ",jumps_from_0)
    jumps_from_0 = min_jumps_dp(a , 0 , n)
    print("val : ", jumps_from_0)