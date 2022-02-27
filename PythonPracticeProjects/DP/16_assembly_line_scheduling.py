# This problem is to find what is the min time to complete the assembly line passage .
# at each step , when we move forward , we add the min of previous ones then move ahead .
# we chose 2 starting points 0,1 and 1,1
# dp[0,0] = v[0,0] + 0
# dp[1,0] = v[1,0] + dp[0,0]
# dp[2,0] = v[2,0] + min(dp[1,0] , tr[2,0] + dp[1,1])
# dp[3,0] = v[3,0] + min(dp[2,0] , tr[3,0] + dp[2,1])

#.. henceforth we do this for each cell in assembly line : therefore


def f1(n):
    if n ==0 :
        return e[0] + a[0][0]
    else :
        return a[0][n] +  min(f1(n-1) , f2(n-1) + tr[0][n-1] )


def f2(n):
    if n ==0:
        return e[1] + a[0][1]
    else:
        return a[1][n] +  min(f2(n-1) , f1(n-1) + tr[1][n-1])






if __name__ == "__main__":
    global a,tr,e,x
    a = [[4,5,3,2], [2,10,1,4]]
    tr = [[0, 7, 4, 5] ,[0, 9, 2, 8]]
    e = [10, 12]
    x = [18, 7]
    print(f1(3) +x[0])
    print(f2(3) +x[1])