
# gcdvalue= gcd(n,d)
# divide array in gcdvalue sets
# shift all the elements in the array blocks to the left by d elements .
# we divide it in gcd parts
# why did we  divide it in gcd parts ?
# Suppose we take an example of n =9 , d=6
# Now coming to the point Why GCD. The GCD gives an exact figure of rotation to be performed. It actually minimizes no of rotations.
#
# For example,
#
# if you want to perform rotation of 30 numbers
#
# with d = 1 the outer loop will be rotating once and inner would rotate 30 times 1*30=30
#
# with d = 2 the outer loop will be rotating twice and inner would rotate 15 times 2*15=30
#
# with d = 3 the outer loop will be rotating thrice and inner would rotate 10 times 3*10=30
#
# So, the GCD Here would ensure the rotations don't exceed the value 30. And as you are getting a number that is divisor of total elements, It won't let skip any element
#TC=o(N)
#SC= O(1)

def gcd(n,d):
    if d==0:
        return n
    else:
        return gcd(d,n%d)

def rotate_array(a,d):
    n = len(a)
    gcdval = gcd(n,d)
    print("gcdcval: ",gcdval)
    for i in range(gcdval):
        temp = a[i]
        j=i
        while(1):
            k=j+d
            if k>=n:
                k%=d
            if k==i:
                break
            print(j,k,a[j],a[k])
            a[j]= a[k]
            print(a)
            j+=d
        a[j]=temp

    print(a)


if __name__=="__main__":
    a=[1,2,3,4,5,6,7,8,9,10,11,12]
    d=3
    rotate_array(a,d)