# find no. of expressions containg n no. of parantheses which are correctly matched .
# find no. of possible binary search trees with n keys .
# count no. of full binary trees with n+1 leaves .
# Given a number n, return the number of ways you can draw n chords in a circle with 2 x n points such that no 2 chords intersect.

# c(3) = c(1)*c(2) + c(2) * c(1) = 1 * 1 + 1 * 1 =2
# c(4) = c(1)*c(3) +c(2) * c(2) +c(3) * c(1) = 1*2 + 1+2*1 =5


def catalan(n):
    if n <=1:
        return 1
    # find the catalan no
    res =0
    for i in range(n):
        res = res + catalan(i) * catalan(n-i-1)
    return res

def catalan_tabulated(n,lookup):
    if n <=1:
        return  1
    res =0
    if lookup[n] == 0:
        print(True)
        print("n" , n)
        for i in range(n):
            print ("i",i)
            print( "1...",catalan_tabulated(i,lookup))
            print("2..." ,catalan_tabulated(n-i-1,lookup))
            res  = res + catalan_tabulated(i,lookup) * catalan_tabulated(n-i-1,lookup)
        lookup[n]=res
        print("returning n", n)
        print("returning lookup" , lookup[n])
    return  lookup[n]

def catalan_memoized(n):
    if n<=1:
        return 1
    catalan =[0 for i in range(n+1)]
    catalan[0] =1
    catalan[1] =1
    for i in range(2,n+1):
        catalan[i]=0
        for j in range(i):
            catalan[i] = catalan[i] + catalan[j] * catalan[i-j-1]

    return  catalan[n]

if __name__ == "__main__" :
    lookup = [0] * 10
    lookup[0]=lookup[1]=1
    # catalan(5)
    # print("catalan : ",catalan_tabulated(3,lookup))
    print("catalan memoized : ", catalan_memoized(3))
