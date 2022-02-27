# Find max value of items filled in a knapsack when adding is either completely allowed or not .
# Consider all subset and pick the one with max_value
# In this we have to check whether an item is completely added or not .
# Even if the array is sorted , by choosing them in sorted order ,we cant guarantee that the max value will be found as "addition of 2 or more smaller elements
# of lower cost may fill more space in knapsack and may increase the cost THAN BY including only one large item or higher cost and leaving some space vacacnt which
# which couldnt be occupied by any other snmaller element.

# ITEMS CANNOT BE REPEATED HERE and 0 OR 1 ADDITION (EITHER COMPLETELY OR NOT ADDED)

# Also , to find total ways in which elements can be added are  (Assume for n total elements):
# if the ith element is included  : value is - val[i] + maxval(i-1 , W-wt[i])
# if the ith element is not included : value is  - maval(i-1 ,W)

# Brute force solution : consider total subsets and calculate total weight and values of all subsets .
# Consider only subsets whose total weight is smaller than  W i.e. if wt[i] > W:  dp [i] = dp[i-1]
# else there are 2 cases:
# if ith element is included : val[i] + maxval(W-wt[i] , i-1)
# if ith element is not included : maxval(W ,i-1)

# Base cases:
# using 0 items - 0 weight
# using 1 items - same weight

# dp[i][j] = max value obtained by using sum till 'ith weight' and calculating sum 'i'
# when ith element is included : dp[W-wt[i]][i-1] + dp[W][i-1]

from builtins import staticmethod, range, len, max


class Item:
    def __init__(self,wt,val,ind,cost):
        self.wt = wt
        self.val = val
        self.ind = ind
        self.cost = cost

    def __lt__(self, other):
        return self.cost<other.cost

class FractionalKnapsack:

    @staticmethod
    def init_items(wt_arr, val_arr):
        items =[]
        for i in range(len(wt_arr)):
            item = Item(wt_arr[i],val_arr[i],i , val_arr[i]/wt_arr[i])
        return items

    def knapsack_0_1_repetetion_allowed1(self, W):
        dp = [0 for j in range(W+1)]
        for i in range(len(wt)):
            for j in range(W+1):
                if (wt[i]==j):
                    dp[j] = max(val[i],dp[j])
                if (wt[i]<j):
                    dp[j] = max(dp[j-wt[i]] + val[i],dp[j])
                if (wt[i]>j):
                    dp[j]= dp[j]
        return dp[W]


    def knapsack_0_1_repetetion_allowed2(self, W):
        dp = [0 for j in range(W)]
        for i in range(len(wt)):
            for j in range(W):
                if (wt[i]==j+1):
                    dp[j] = max(val[i],dp[j])
                if (wt[i]<j+1):
                    dp[j] = max(dp[j-wt[i]] + val[i],dp[j])
                if (wt[i]>j+1):
                    dp[j]= dp[j]
        return dp[W-1]


    def knapsack_0_1_repetetion_allowed4(self, W):
        dp = [0 for j in range(W+1)]
        for i in range(len(wt)):
            for j in range(W+1):
                # if (wt[i]==j):
                #     dp[j] = max(val[i],dp[j])
                if (wt[i]<=j):
                    dp[j] = max(dp[j-wt[i]] + val[i],dp[j])
        return dp[W]


    def knapsack_01_recursive_dp3(self,w,n):
        dp= [[0 for j in range(n+1)] for i in range(w+1)]
        print (dp)
        for i in range(1,w+1):
            for j in range(1,n+1):
                # print (dp)
                # if i==0 or j==0:
                #     dp[i][j] = 0
                if wt[j-1]<=i:
                    dp[i][j] = max(dp[i-wt[j-1]][j]+val[j-1],dp[i][j-1])
                else:
                    dp[i][j] = dp[i][j-1]
        return dp[w][n]



# val = [60, 40, 100, 120]
# W = 50
W = 8
val= [10, 40, 50, 70]
wt= [1, 3, 4, 5]
if __name__ == "__main__":
    f =  FractionalKnapsack ()
    print(f.knapsack_0_1_repetetion_allowed2(W))
    print(f.knapsack_0_1_repetetion_allowed1(W))
    print(f.knapsack_0_1_repetetion_allowed4(W))
    print(f.knapsack_01_recursive_dp3(W,len(wt)))


