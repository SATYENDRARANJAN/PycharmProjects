# find max sum in grid for no two elements adjacent

def find_max_sum(a):
    # incl_prev = max sum till nth column when nth column is included
    # excl_prev = max_sum_till_nth_column_when nth column is  excluded .
    n = len(a[1])
    incl_prev_column = max(a[0][0],a[1][0])
    excl_prev_column = 0
    for i in range(1,n):
        incl_curr_column = excl_prev_column + max(a[0][i],a[1][i])
        excl_curr_column = incl_prev_column
        incl_prev_column = incl_curr_column
        excl_prev_column = excl_curr_column
    return max(incl_curr_column ,excl_curr_column)

if __name__ == "__main__":
    a = [ [ 1, 2, 3, 4, 5],
        [ 6, 7, 8, 9, 10] ]
    a1 = [[1,4,5],[2,0,0]]

    print(find_max_sum(a))
    print(find_max_sum(a1))