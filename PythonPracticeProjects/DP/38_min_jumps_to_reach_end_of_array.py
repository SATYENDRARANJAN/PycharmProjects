from builtins import len, range

# time complexity on(n^n)
# space complexity on(1)
def minjumps(a,h):
    minima = 999999
    if h==0:
        return 0
    print(a,h)
    for i in range(h):
        print("going for {0}---{1}".format(i,a[i]))
        m = minjumps(a,i)
        print("         minjump  to reach {0} = {1}    :  {2} ".format(i,minjumps(a,i), a[i]))
        # jump is always going to be of one count , it might span for more more than one houses or length. so m+1 is used and not m+i
        for k in range(1,a[i]+1):
            if  a[i]!=0 and m!=999999 and i+k >=h and m+1<minima:
                minima = m+1
                print("               minima :",minima)
    return minima



if __name__ == "__main__":
    a = [1, 1, 1, 1,2]
    # a = [1, 3, 5, 8, 9]
    a = [1,1,1  ,1,1,1  ,1,1,1  ,1,1,1  ,1]
    # a = [1, 3, 5, 3, 2, 2, 1, 1, 9, 5]
    print("minima",minjumps(a,len(a)-1))
