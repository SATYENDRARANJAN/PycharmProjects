def fib(n):
    if n==0 or n==1:
        return  n
    return fib(n-1) +fib(n-2)


def fib_tabulated(n):
    a[0] =0
    a[1] =1
    f = [0] * n+1
    # base case assignment
    f[1] =1

    # calculating the fibonacci and storing the values
    i=0
    for i in range(2,n+1):
        a[i] = a[i-1]+a[i-2]
    return a[n]


# memoization includes creating a lookup table in normal recursion and checking into it before finding the value .
# write normal recursion
# add lookup
def fib_memoized(n ,lookup ):
    if n <=1:
        lookup[n]= n
    else:
        if lookup[n] is None:
            lookup[n] =fib_memoized(n-1,lookup) + fib_memoized(n-2,lookup)
    return lookup[n]








if __name__=="__main__":
    n =10
    fib(n)
    fib_tabulated(n)
    lookup =[0] * n+1
    fib_memoized(n , lookup)


