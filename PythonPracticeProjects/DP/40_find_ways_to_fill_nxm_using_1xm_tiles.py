# find ways to fill (n x m) space using 1xm tiles .

# count of ways = 1 for   : 1<=n<m
#               = 2 for  `: n = m
#               = count(n-1) + count(n-m) for   : m<n

# TC: 0(N)
# SC: O(N)

from builtins import range

def countways(n,m):
    # tables to store values of subproblems
    count = []
    for i in range(n+1):
        count.append(0)
    count[0] = 0

    # fill the table upto value n
    for i in range(1,n+1):
        if  i >=1 and i < m :
            count[i] = 1
        elif i == m:
            count[i] = 2
        elif i > m:
            count[i] = count[i-1] +  count[i-m]
    return count[n]



if __name__ == "__main__":
    m=7
    n=4
    print(countways(m,n))