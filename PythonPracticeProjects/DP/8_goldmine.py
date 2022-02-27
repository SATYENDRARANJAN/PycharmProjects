# start from any position in the first column r==5 c==4
# if row == 0 , find min((row, col+1) ,(row+1,col+1) and add to sum
# if row == r-1 , find min ((row -1 ,col+1),(row,col+1)) and add to sum
# if col == c-1 , return sum


import random

# each cell would contain the max sun from previous 3 rows in last column to be added .
def find_sum_goldmine_tabulated(mine, maxrow , maxcol):
    dp = [[0 for j in range(maxcol)] for i in range(maxrow)]

    for j in range(maxcol):
        for i in range(maxrow):
            if j == 0  :
                dp[i][j] = mine[i][j]
            elif i == 0 :
                dp[i][j] = mine[i][j] +  max(dp[i][j-1] ,dp[i+1][j-1])
            elif i == maxrow-1:
                dp[i][j] = mine[i][j] + max(dp[i][j-1],dp[i-1][j-1])
            else:
                dp[i][j] = mine[i][j] + max(dp[i+1][j - 1],max(dp[i][j - 1], dp[i - 1][j - 1]))

    print_dd_arr(dp,maxrow  , maxcol)



def find_sum_goldmine_memoized(mine , r , c , dpmemo):
    if c==0:
        dpmemo[r][c]= mine[r][c]
        return  dpmemo[r][c]
    if dpmemo[r][c] ==0:
        dpmemo[r][c] = max()
    return dpmemo[r][c]


def add_next_max_cell(mine, row, col, sum ):
    r = c = 0
    if col == maxcol:
        return  0
    elif row ==0 :
        next_min = max(mine[row][col+1] , mine[row+1][col+1])
        if next_min == mine[row][col+1]:
            r = row
            c = col+1
        else :
            r = row+1
            c = col+1
    elif row == maxrow-1:
        next_min = max(mine[row-1][col+1] , mine[row][col+1])
        if next_min == mine[row-1][col+1]:
            r = row-1
            c = col+1
        else:
            r = row
            c = col+1
    else:
        next_min = max(mine[row-1][col+1],max(mine[row][col+1],mine[row+1][col+1]))
        if next_min == mine[row - 1][col+1]:
            r = row - 1
            c = col + 1
        elif next_min == mine[row][col+1]:
            r = row
            c = col + 1
        else:
            r = row+1
            c = col+1

    print("Adding : " ,next_min)
    return next_min + add_next_max_cell(mine , r , c, maxrow , maxcol)


def find_sum_gold_mine_recursive(mine , row , col , maxrow , maxcol):
    # sum = sum + add_next_max_cell(mine , row , col , maxrow , maxcol)
    sum = sum + find_sum_gold_mine_recursive(mine, row, col)


def find_sum_gold_mine_recursive(mine,r,c,sum):
    # sum = sum + max(last 3 elements of a column )
    if c == 0:
        sum  = sum + mine[r][c]
    elif r ==0 :
        goldtable[r][c] = mine[r][c] + gold

def print_dd_arr(mine, r ,c):
    for i in range(r):
        for j in range(c):
            print (mine[i][j] , end = "   ")
        print("")


if __name__ == "__main__":
    n = 7
    k = 4
    mine = [[random.randint(0,20)for j in range(k)]for i in range(n)]
    start_row =0
    start_col = 0
    print_dd_arr(mine, n , k )
    # print(find_sum_gold_mine(mine,start_row,start_col, n , k))
    print("\n THE TABULATED VERSION IS :")
    print(find_sum_goldmine_tabulated(mine, n , k))
    #
    # dpmemo = [[0 for j in range(maxcol)] for i in range(maxrow)]
    # print(find_sum_goldmine_memoized(mine, n , k))

    ndp = [[0 for j in range(maxcol)] for i in range(maxrow) ]
    print (find_sum_goldmine_recursive(mine, n, k , gold))