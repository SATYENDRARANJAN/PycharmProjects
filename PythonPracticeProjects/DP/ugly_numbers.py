# ugly numbers are nos whose prime factors are 2,3,5

# n= n%2
# n=n%3
# n=n%5 if n !=1
# ugly[0]=1
# ugly[0] * 2
# ugly[0] * 3
# ugly[0] * 5



def maxdivide(a,b):
    while a % b == 0:
        a = a/b
    return a


def getNthUglyNo(n):
    i=1
    count =1
    # Check for all integers until ugly becomes n
    while n > count :
        n = maxdivide(i,2)
        n = maxdivide(n,3)
        n = maxdivide(n,5)
        if n ==1:
            count +=1
        i+=1
    return i


def getNthUglyNo_tabulated(n):
    ugly = [0]*(n+1)
    count =0
    ugly[count]=1
    i2 = i3 = i5 =0
    print (i2 , i3 , i5)
    next_multiple_of_2 = ugly[i2] * 2
    next_multiple_of_3 = ugly[i3] * 3
    next_multiple_of_5 = ugly[i5] * 5
    count += 1
    while count<=n:
        ugly[count] = min(next_multiple_of_2,next_multiple_of_3,next_multiple_of_5)
        print ("{0}..{1}".format(ugly[count] ,count))
        if ugly[count] == next_multiple_of_2:
            i2 = i2+1
            next_multiple_of_2 = ugly[i2]*2
        if ugly[count] == next_multiple_of_3 :
            i3 = i3+1
            next_multiple_of_3 = ugly[i3]*3
        if ugly[count] == next_multiple_of_5 :
            i5 = i5 + 1
            next_multiple_of_5 = ugly[i5]*5
        count += 1
    return ugly[n]


if __name__ == "__main__":
    getNthUglyNo(10)
    print(getNthUglyNo_tabulated(10))