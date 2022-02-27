# pseudo
# for i : print all subseq till i
# dp[0] =[1]
# dp[1] = dp[i-1] * a[i]
# a[i-2]
# a[i-3]
from builtins import range


def get_subseq(a,n):
    if n == 0:
        return [[a[0]]]
    list=[]
    list2 =[]
    for i in range(n-1,-1,-1):
        list = get_subseq(a,i)
        for subseq in list:
            list2.append(subseq + [a[n]])
        list2 = list2 + list
        list2.append([a[n]])
    return list2


def get_subseq_dynamic(a, n):
    print("n: ",n)
    dp = [[[] for j in range(n+1)] for i in range(n+1)]


    for i in range(n+1):
        for j in range(i,n+1):
            if i == j:
                dp[i][j] = [[a[i]]]
                print(" === i:{0} ,j:{1} ,dp[{4},{3}]:{2}, : {5}".format(i, j, dp[i][j],j,i,a[i]))
            else:
                print(" *** i:{0} ,j:{1} ,dp[{4},{3}]:{2}, : {5}".format(i, j, dp[i][j-1],j-1,i,a[i]))
                templist= [k + [a[j]] for k in dp[i][j-1]]
                print("templist :",templist)
                list  =[]
                list.append(templist)
                list.append(dp[i][j-1])
                dp[i][j] = list

    print(dp[0][n])
    l=dp[0][n]
    for elem in l:
        print(elem)





            # print(" ***  for i ={0} and j ={1}  *** ".format(i, j))
            # if True:
            #     print("i:{0} ,j:{1} ,dp[{4},{3}]:{2}, : {5}".format(i, j, dp[i][j - 1],j-1,i,a[i]))
            #     list = [([k] + [a[i+1]]) for k in dp[i][j - 1]]
            #     print(list)
            #     dp[i][j] = dp[i][j - 1].append(list)
                # if len(dp[i][j]) == 0:
                #     print(" ** dp[{0},{1}]: {2} ,list = {3}**".format(i,j,dp[i][j], list) )
                #     dp[i][j] = dp[i][j].append(list)
                # print("tt1 : ", dp[i][j], list)
                # dp[i][j] = dp[i][j].append([a[j]])
                # print("i:{0} , j: {1} , dp[{3}][{4}] : {2} ".format(i, j, dp[i][j],i,j))




if __name__ == "__main__":
    a = [1,2,3,4]
    n = len(a)
    for i in range(n):
        l = get_subseq(a,i)
        for elem in l:
            print(elem)
    #     print("****************************")
    # # print subsequences of an array a
    # l = get_subseq(a, n-1)
    # for elem in l:
    #     print(elem)
    # print subsequences of an array a - dynamic
    # l = get_subseq_dynamic(a, n-1)







