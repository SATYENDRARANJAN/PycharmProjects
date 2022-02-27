# In the following program , max sum increasing subsequence till a no. then adding any later coming prefix to that sum ,
# which also follows the max sum increasing subsequence property .

    # dp[i][j] basically tells the max sum subseq till ith element and including the jth element also so we should implement the formula here
    # dp[0][1] tells us the max sum subseq till 0 using 0 elements and adding 1st element
    # dp[0][2] tells us the max sum subseq till 0 using 0 elements and adding 2nd element
    # dp[0][3] tells us the max sum subseq till 0 using 0 elements and adding 3rd element
    # dp[0][4] tells us the max sum subseq till 0 using 0 elements and adding 4th element

    # dp[1][2] tells us the max sum subseq till 1 using 1 element and adding 2nd element
    # dp[1][3] tells us the max sum subseq till 1 using 1 element and adding 3rd element
    # dp[1][4] tells us the max sum subseq till 1 using 1 element and adding 4th element
    # and so on ...
    # dp[1][2] = max_subseq_till_1_adding_2() = maxsub_till_0_addin_1() + adding 2

def print_dd(dp,m, n):
    for i in range(m):
        print(dp[i],end='')
        print()



def find_max_sum_subsequence_including_k(a, index, k, l):
    dp1 = [[0 for t in range(k)] for l in range(index)]

    for i in range(0,index):
        for j in range(k):
            print(i,j)
            if i == 0 :
                if a[j]>a[i] and j>i: # j>i is unnecessary here
                    dp1[i][j] = a[i] + a[j]
                else:
                    dp1[i][j] = a[i]
            elif a[j]>a[i] and j>i:
                if dp1[i-1][i] + a[j] > dp1[i-1][j]:
                    dp1[i][j] = dp1[i-1][i] + a[j]
                else:
                    dp1[i][j] = dp1[i-1][j]
            else:
                 dp1[i][j] = dp1[i-1][j]
    print_dd(dp1,index,k)
    k= dp1[index-1][k-1] # which gives the max sum subsequence till index including kth element
    return k



if __name__ == "__main__":
    a = [1, 101, 2, 3, 100, 4, 5]
    l = len(a)
    i = 4
    k = 6
    print (find_max_sum_subsequence_including_k(a,i,k,l))