# This problem is about finding the no. of ways to paint fences where no two adjacent fences can have the same color .
# to paint n = 2 fences
# --> n * n-1 ways
# for n =3 => when first two different colored : n * n-1 * n
# for n =3 => when both same : n * n-1
# total for n =3 is : n* (n-1) *(n+1)
# for n =4 => when same : n * n-1 * n
# for n =4 when different :  n * n-1  * n* n-1
# totat for 4  = n * n-1 * n  +  n * n-1  * n* n-1
# for n = 5 when same : n * n -1 * n * n-1
# for n =5 , when different : n * n-1 * n * n-1*n
# This way we can find the exact answer but to find it by another way so that the problem has a recursive approach .

# Method 2: Breaking the problem into recursive sub problem .
# f(n,k) = fs + fd
# f(1,k) = k + 0
# f(2,k) = f(1,k) * (k-1) + f(1,k) *1
# f(3,k) = f(2,k) * (k-1) +
# f(4,k) =


def paint_fence(n,k):
    if n == 1:
        return k
    if n == 2:
        return k * k
    # n1 =  count when both the last fences are same colored
    # n2 = count when both the last fences are different colored
    n1 = paint_fence(n-2,k) * (k-1) * 1
    n2 =  paint_fence(n-1,k) * (k-1)
    return n1 +n2


def paint_fence_tabulated(n,k):
    dp = [0] *(n+1) # for o to  n  : dp tells the total no of ways to paint n fences with k colors where k is constant
    dp[0] = 0
    dp[1] = k
    dp[2] = k * (k-1) +k *1
    for i in range(3,n+1):
        dp[i] = dp[i-1] * (k-1) + dp[i-2] * (k-1)
    return  dp[n]



def paint_fence_memoized(n,k,dpmemo):
    if n == 0 or k==0 :
        dpmemo[0] = 0
        return 0
    if dpmemo[n] !=-1:
        return dpmemo[n]
    elif n ==1:
        dpmemo[n] = k
    elif n ==2:
        dpmemo[n] = k * k
    else:
        dpmemo[n] = (k-1) * (paint_fence_memoized(n-1,k,dpmemo) + paint_fence_memoized(n-2,k,dpmemo))
    return dpmemo[n]





if __name__ == "__main__":
    n =3 # fence
    k =2 # colors
    dpmemo = [-1 for i in range(n+1)]
    print(paint_fence(n,k))
    print(paint_fence_tabulated(n,k))
    print(paint_fence_memoized(n,k,dpmemo))


