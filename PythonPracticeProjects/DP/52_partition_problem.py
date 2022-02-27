# To find the partition with equal sums
# We calculate sum of totl array and find the half sum.
# Now , find if any subssequnce sum is equal to half the sum

# To find each subsequence sum , either pair each element with combinations of each element .
# This basically is equivalent to each element being combined with the all subsequences for child elements

# And all subsequences of each element (or child element) can be found by either counting them in the solution or not counting them in the solution.
from builtins import len, range


def is_half_sum(start,end,sum):
    # print(start,end)
    if start==end :
        return False

    if sum ==0:
        return True


    return is_half_sum(start+1,end,sum-arr[start]) or is_half_sum(start+1,end,sum)




def find_partition(arr,l):
    sum =0

    # find sum
    for i in range(l):
        sum = sum+arr[i]
    print (sum)

    # return if sum is not even.
    if sum %2!=0:return False

    # find the half sum
    halfsum = sum//2

    # find if any subsequence is equal to halfsum
    return is_half_sum(0,l,halfsum)



def find_half_sum_dp(arr,l):
    sum =0
    # find sum
    for i in range(l):
        sum = sum+arr[i]
    # print(sum)

    # return if sum is not even
    if sum%2 !=0:
        return False

    # find the half sum
    halfsum = sum//2

    dp = [[0 for j in range(l+1)]for i in range(sum//2 +1)]

    for j in range(l+1):
        for i in range(sum//2+1):
            print(i,j)
            if i ==0 and j==0:
                dp[i][j]=True
            elif i==0:
                dp[i][j]=True
            elif j==0 and i!=0:
                dp[i][j]=False
            else:
                dp[i][j] = dp[i-arr[j-1]][j-1] or dp[i][j-1]
    print_elemtents_dp(dp, sum//2, l)
    return (dp[sum//2][l])



def find_half_sum_dp_optimized_space(arr,l):
    sum =0
    # find sum
    for i in range(l):
        sum = sum+arr[i]
    print(sum)

    # return if sum is not even
    if sum%2 !=0:
        return False

    # find the half sum
    halfsum = sum//2

    dp = [[0 for j in range(2)]for i in range(sum//2 +1)]

    for i in range(sum//2+1):
        dp[i][0] = True if i ==0 else False

    for j in range(1,2):
        dp[0][j] = False


    for j in range(1,l+1):
        for i in range(1,sum//2+1):
            if j%2 ==1:
                dp[i][j%2] = dp[i-arr[j-1]][j%2-1] or dp[i][j%2-1]
            elif j%2==0:
                dp[i][j%2]= dp[i-arr[j-1]][j%2+1] or dp[i][j%2+1]
    return (dp[sum//2][(l+1)%2])



def print_dd_arr(arr,m,n):
    for i in range(m+1):
        for j in range(n+1):
            print(arr[i][j],end=" ")
        print(" ")



def print_elemtents_dp(dp,m,n):
    print("**start**")
    i=m
    sol1 =[]
    sol2=[]
    for j in range(n,-1,-1):
            # current element included or not in solution set
            print("dp[{0}[{1}]={2}".format(i,j-1,dp[i][j-1]))
            if dp[i][j-1] == True :
                i = i
                print("adding:",arr[j-1])
                sol2.append(arr[j-1])
            elif dp[i-arr[j-1]][j-1] == True:
                i = i-arr[j-1]
                sol1.append(arr[j - 1])
            else:
                print(sol1)
                print(sol2)
    print("**end**")

    print(sol1,sol2)




arr= [1, 5, 11, 5,1,1]

if __name__ == "__main__":
    # print(find_partition(arr,len(arr)))
    print(find_half_sum_dp(arr,len(arr)))
    # print(find_half_sum_dp_optimized_space(arr,len(arr)))


