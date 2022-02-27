# For a case when an item can be included or not , we have to find all possible combinations:
# To find all possible combinations:
# Lets take nth item . This item can either be included or excluded : maxval (W,n)
# For ith : val_included = val[n-1] + maxval(W-wt[i] ,n-1 )
# For ith : val_not_included = maxval(W , n-1)

# Base Cases:
# For i == 0 or W ==0 :return 0
# if wt[n-1] > W : return val_not_included

val = [60, 100, 120]
wt = [10, 20, 30]
W = 50
# i = W= 0 to 50
# J = len(wt) = 0 to 3
# 0 0 0 0 0 0 0 0 0 ....
# 0 0 0 0 0 0 0 0

# dp[i][j] = 0                                                 : if i==0 or j==0
#          = max (dp[i-wt[j-1]][j-1] + val[j-1], dp[i][j-1])   : if  (wt[j-1] < i) # find  "sum =i"  using  elements till jth index
#          = dp[i][j-1]                                        : otherwise


# IF REPETETION IS ALLOWED
# Now if the repetetion is allowed in Knapsack .We still traverse the matrix  in the same order .
# when an item is included : When repetition is allowed then , the no. of elements do not change  .
# And case of excluding an item does not exists here as no. of items always remain same.
# Thus no. of items in this case is constant .
# Thus we create a one dimensional array .dp[w]
# dp[i]  = max of = when including an item  : dp[i-wt[j]] + val[j]
#                 = when excluding an item  : dp[i]



from builtins import range, len, max


class Item:
    def __init__(self,wt,val,ind,cost):
        self.wt = wt
        self.val = val
        self.ind = ind
        self.cost = cost

    def __lt__(self, other):
        return self.cost<other.cost


class Knapsack_0_1:
    def init_items(wt_arr,val_arr):
        items =[]
        for i in range(len(wt_arr)):
            item = Item(wt_arr[i],val_arr[i],i,wt_arr[i]/val_arr[i])
        items.append(item)
        return items


    def knapsack_01_rec(self,w,n,list):
        print(list)
        if w== 0 or n ==0 :
            return 0
        if w - wt[n-1] <0:
            return self.knapsack_0_1(w,n-1,list)
        else:
            return max(val[n-1]+ self.knapsack_01_rec(w-wt[n-1],n-1,list+[val[n-1]]) , self.knapsack_01_rec(w,n-1,list))


    def knapsack_01_dp(self,w,n):
        dp= [[0 for j in range(n+1)] for i in range(w+1)]
        print (dp)
        for i in range(1,w+1):
            for j in range(1,n+1):
                # print (dp)
                # if i==0 or j==0:
                #     dp[i][j] = 0
                if wt[j-1]<=i:
                    dp[i][j] = max(dp[i-wt[j-1]][j-1]+val[j-1],dp[i][j-1])
                else:
                    dp[i][j] = dp[i][j-1]

        self.printKnapsack(dp,w,n)
        return dp[w][n]


    #  WRONG CODE LINE 90,91  IS WRONG
    # def knapsack_01_dp_nm_matrix(self,w,n):
    #     dp=[ [0 for i in range(n+1)]  for j in range(w+1)]
    #
    #     for i in range(w+1):
    #         for j in range(n+1):
    #             if j==0 :
    #                 dp[i][j] = val[j]
    #             elif wt[j-1]>=i :
    #                 dp[i][j] = dp[i][j-1]
    #             else :
    #                 dp[i][j] = max(dp[i][j-1] ,val[j-1] + dp[i-wt[j-1]][j-1])
    #     return dp[w][n]
    #


    def knapsack_01_dp_nw_matrix(self,w,n):
        dp=[ [0 for i in range(n+1)]  for j in range(w+1)]

        for i in range(w+1): #
            for j in range(n+1):
                if j==0 :
                    dp[i][j] = 0
                elif wt[j-1]>i :
                    dp[i][j] = dp[i][j-1]
                else :
                    dp[i][j] = max(dp[i][j-1] ,val[j-1] + dp[i-wt[j-1]][j-1])
                print (dp)
                self.printKnapsack(dp,W,n)
        return dp[w][n]


    def knapsack_01_dp_nwplus1_matrix(self,w,n):
        dp=[ [0 for i in range(n+1)]  for j in range(w+1)]

        for i in range(w+1):
            for j in range(n):

                if j ==0 :
                    dp[i][j] = val[j]
                elif wt[j-1] > i :
                    dp[i][j] = dp[i][j-1]
                else :
                    dp[i][j] = max(dp[i][j-1] ,val[j] + dp[i-wt[j]][j-1])
                print (dp)
        return dp[w][n-1]


    # the result either comes from   max( dp[w][i-1] , dp[w-wt[j-1]][i-1] )
    # when jth item included ->( val[j] + dp[i-wt[j]] [j-1])
    # when jth item excluded ->( dp[i][j-1] )
    def printKnapsack(self,dp,W,n):
        print("PRINTING KNAPSACK")
        print(dp)
        wt_list =[]
        i=W
        for j in range(n,0,-1):
            print(i,j)
            if i<wt[j-1]:
                continue
            if dp[i][j - 1] == dp[i][j]:
                # means the item is not included
                continue
            elif dp[i][j] == (val[j-1] + dp[i - wt[j-1]][j - 1]):
                # means item is included
                # set wt to w-wt[j]
                print(dp[i][j])
                wt_list.append(wt[j-1])
                i=i-wt[j-1]
        print("THE LIST IS ",wt_list)



#
#print
# val = [60, 100, 120]
# wt = [10, 20, 30]
# W = 50

val = [10, 15, 40]
wt = [1, 2, 3]
W = 5
if __name__ == "__main__":
    f =  Knapsack_0_1()
    list=[]
    print(f.knapsack_01_rec(W,len(wt),list))
    # print(f.knapsack_01_dp_nw_matrix(W,len(wt)))
    print(f.knapsack_01_dp(W,len(wt)))
    # print(f.knapsack_01_dp_nm_matrix(W,len(wt)))
