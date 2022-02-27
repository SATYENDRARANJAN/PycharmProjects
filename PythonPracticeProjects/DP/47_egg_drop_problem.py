# There are n eggs and k floors and we need to  find min no. of trials  needed to find the topmost floor from where eggs wont break .
# For 1 floor , we would need only 1 egg  to find whether it breaks from 1st floor or not.
# For 1 egg , only way is to go upwards from the bottommost floor and check for each floor , hence no. of trials is k for 'k floors'.
# Similarly for 2 floors  ==>
#           From 2nd floor ==> eggdrop(n,2) ==> if egg is dropped ==> it may break ==> eggdrop(n-1,1) = 1
#                                                                 ==> it may not break ==> eggdrop(n,k-2) = ed(n,0) = 0
# for 3 floors  ==>
#           From 2nd floor ==> eggdrop(n,3) ==> if egg is dropped ==> it may break ==> eggdrop(n-1,2)
#                                                                 ==> it may not break ==> eggdrop(n,k-3) = ed(n,1)
# for 4 floors  ==>
#           From 2nd floor ==> eggdrop(n,4) ==> if egg is dropped ==> it may break ==> eggdrop(n-1,3)
#                                                                 ==> it may not break ==> eggdrop(n,k-4) = ed(n,0)
# for 5 floors  ==>
#           From 2nd floor ==> eggdrop(n,5) ==> if egg is dropped ==> it may break ==> eggdrop(n-1,4)
#                                                                 ==> it may not break ==> eggdrop(n,k-5) = ed(n,0)

# We create out first solution by recursive
import sys
from builtins import max, min, range

# As there is overlapping subsproblem's  being solved through recursion , complexity is exponential
# Space Complexity : O(1)
def eggdrop_rec(n,k):
    if n ==0 or k ==0:
        return 0
    elif n ==1:
        return k
    elif k ==1:
        return 1
    min_of_max_trials = sys.maxsize
    # calculate if started from each floor and choosing (floor+1) to (floor+k) as the limits of the floors
    for x in range(1,k+1):
        # trials_if_egg_breaks = eggdrop_rec(n-1,x-1)
        # trials_if_egg_doesnt_break = eggdrop_rec(n,k-x)
        max_trials_for_worst_case = max(eggdrop_rec(n-1,x-1),eggdrop_rec(n,k-x))
        if min_of_max_trials > max_trials_for_worst_case:
            min_of_max_trials = max_trials_for_worst_case
    return 1+min_of_max_trials


# Time Complexity : O(n*k^2)
# Space Complexity : O(n*k)
def eggdrop_dp(n,k):
    dp = [[0 for j in range(k+1)] for i in range(n+1)]
    # fill edge conditions first
    # if i =0 i.e. eggs =0  and j == 1 to k : return 0
    # if i =1 i.e. eggs =1  and j == 1 to k: return j
    # if j =0 i.e. floor =0 , eggs = anything  : return 0
    # if j =1 i.e. floor =1 , eggs = anything : return 1

    for i in range(n+1):
        dp[i][0]=0
        dp[i][1]=1
    for j in range(k+1):
        dp[0][j]=0
        dp[1][j]=j
    for i in range(2,n+1):
        for j in range(2,k+1):
            minimum_of_max_trials=sys.maxsize
            for x in range(1,j+1):
                max_trials_worst_case = max (dp[i-1][x-1] , dp[i][j-x])
                if minimum_of_max_trials > max_trials_worst_case:
                    minimum_of_max_trials = max_trials_worst_case
            dp[i][j] = 1+ minimum_of_max_trials
    return dp[n][k]


if __name__=="__main__":
    print(eggdrop_rec(2,10))
    print(eggdrop_dp(2,10))