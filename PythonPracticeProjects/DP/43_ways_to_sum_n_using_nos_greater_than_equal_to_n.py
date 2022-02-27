# To find the sum n using nos. greater than or equal to m , we need to start from m and add x to get n .( Variation of Unbounded knapsack .)
# We basically have 2 options to do it :-
# 1. Add the first number and sum should be equal to n-m . and recursively call for sum of remaining array .
# 2. Remove the first and sum should be equal to n and recursively call sum of remaining array .

# To realise these kind of problems , we create a matrix where in row tells us the sum and column tells us the range of numbers that we can use .
# Eg . I = SUM = 9 AND J = range = [starting_point , total_sum]

# First row 0 would be populated with 0 , as sum of 0 is possible without using any no. and only 0 .
# First column 0 would be populated with 0 , as sum of 0 is only possible when we dont use any no.
# Last row means sum iLast using numbers in range from start point(j) to iLast

# i = 1 to m // total sum
# j = 1 to n // starting and end limit
# ways(i ,j+1) :  Keeping the starting element NOT ADDED i.e. j and start from j+1  AND sum becomes i :  ways to find sum i using elements starting from j+1 to n
# ways(i-j ,j) :  Keeping the starting element ADDED i.e. j used repeatedly added => i - (j+j+j+j...) till i-summation(j's) <j
#              :  AND sum becomes i-j :  ways to find sum i-j using elements starting from j
# dp[i][j] = ways(i ,j+1) + ways(i-j ,j)
# Now for sum till  first element is in first col and sum till last element  is in last column


# Then each column would have the ways in which sum of i is possible using elements from [m+1,i]    +
# and Ways in which sum of (i-m)  is possible using elements from [m,i-m]

# Suppose m =1 ,n =3 == > follow backwards.
# We will first find  what is the sum on the (i,j)th i.e. (m,n)th position


from builtins import range, max


def find_ways(total_sum,starting_point):
    print(total_sum , starting_point  )
    dp = [[0 for i in range(total_sum+1)] for j in range(total_sum+1)]
    dp[0][total_sum + 1] = 1;

    for i in range(1,total_sum+1):
        for j in range(starting_point,total_sum+1):
            # for i < j and ways(i-j,j) wont be possible as j>i ,hence only including ways(i,j+1)
            dp[i][j] = find_ways(i,j+1)
            if(i > j):
                dp[i][j] += find_ways(i-j,j)
    # print(dp)
    return dp[total_sum][starting_point]



# not working code
def add_m_and_check_print(total_sum, curr_sum, lst,start ):
    # print(lst , curr_sum,total_sum)
    if curr_sum == total_sum:
        print (lst)
        return
    if curr_sum>total_sum:
        return
    for i in range(start ,total_sum):
        # print( lst +[i] , curr_sum+i,total_sum)
        add_m_and_check_print(total_sum, curr_sum+i , lst +[i],start)

#
#
# def find_ways2(total_sum,start):
#     if total_sum == 0 :
#         return 0
#     for  i in range(start,total_sum):
#         ways = 1 +



def find_ways_recursive(sum,n):
    if sum <= 0:
        return 0
    elif sum<=n:
        return 0
    else:
        for i in range(n,sum+1):
            if find_ways_recursive(sum):
                pass

def findways(n,k,list):
    w=0;
    if n==0 or n==k :
        return 1
    elif n<k:
        return 0
    else:
        for i in range(k,n):
            w += findways(n-i,i,list+[i])
    return 1+w

def print_dd_array(a,m,n):
    for i in range(m):
        for j in range(n):
            print(a[i][j], end="    ")
        print("")

def findways_dp1(n,k):
    # find sum of n using nos. greater than k (k to n)
    dp = [[0 for j in range(n+1)] for i in range(n+1)]

    for j in range(n,0,-1):
        for i in range(j,n+1):
            print(i,j)
            if i==j:
                dp[i][j] = 1
            if i<j:
                dp[i][j] = 0
            if i>j:
                dp[i][j] = dp[i-j][j] + dp[i][j+1]
    print_dd_array(dp,n+1,n+1)
    return dp[n][k]

# sum , i
# i =4 sum =4
# i =3 , sum 3 , sum 4


def findways_dp2(n,k):
    dp = [[0 for i in range(n+1)] for j in range(n+1)]
    # as we need dp[4,4] ==> dp[3,3],dp[3,4] ==> dp[2,2][2,3][2,4] ==> dp[1,1][1,2][1,3][1,4] so basically here for each i from 221

    # j is sum
    # i is number's lower limit (find sum of j using nos. greater than i)
    for i in range(n,0,-1): # numbers till i
        for j in range(i,n+1): # sum j using numbers greater than i
            print(i,j)
            if i==j:
                 dp[i][j] = 1
            if i>j:
                dp[i][j] = 0
            if i<j:
                dp[i][j] = dp[i][j-i] + dp[i+1][j]
    print_dd_array(dp,n+1,n+1)

    return dp[k][n]



# Python3 Program to find number of ways to
# which numbers that are greater than
# given number can be added to get sum.
MAX = 100


# Return number of ways to which numbers
# that are greater than given number can
# be added to get sum.

# GEEKS FOR GEEKS COPIED CODE
def numberofways(n, m):
    dp = [[0 for i in range(n+2)] for j in range(n+2)]

    dp[0][n + 1] = 1

    # Filling the table. k is for numbers
    # greater than or equal that are allowed.
    for j in range(n, m - 1, -1):

        # i is for sum
        for i in range(n + 1):

            # initializing dp[i][k] to number
            # ways to get sum using numbers
            # greater than or equal k+1
            dp[i][j] = dp[i][j + 1]

            # if i > k
            if (i - j >= 0):
                dp[i][j] = (dp[i][j] + dp[i - j][j])

    return dp[n][m]





val = [60, 100, 120]
wt = [10, 20, 30]
W = 50
lowrlimit=1
if __name__ == "__main__":
    total_sum = 4
    starting_point = 1

    curr_sum =0
    i=0
    list =[]
    print(findways(4,1,list))
    print(findways_dp1(4,1))
    print(findways_dp2(4,1))
    # print(numberofways(4, 1))

    # print(find_ways_recursive(total_sum,starting_point))
    # print(find_ways_dp_with_2_params(total_sum,starting_point))
    # print(find_ways_dp_with_1_params_1_row_being_used(total_sum,starting_point))


    # Do not become football of other people's opinion)A
    # ACCEPT PEOPLE as they are .
    # Total acceptance is divinity.
    # jO VYAKTI JAISE H UNKO VAISE SWEEKAR KREIN.
    # IS CHhad TO SWEEKAR KREIN. Vartman chaad atal h