#mergesort
def mergesort(a,l,r):
    print("cls is {0} and {1}".format(l,r))
    if l ==r :
        return a
    mid =l +(r-l)//2
    print (mid ,l,r)

    n1 = mid-l+1
    n2 = r-mid
    k=0
    # seperate first half and second half of the array
    a1=[0] * (mid -l +1)
    a2=[0] * (r -mid )
    for i in range(l,mid+1):
        a1[i] =a[i]
        print(("a1: {0} , {1} ,{2}").format(a1, a, i))
    for i in range(mid+1,r+1):
        a2[k]=a[i]
        print ("a2:{0} ,{1},{2}".format(a2,a[i],i))
        k=k+1

    # merge sort each of them
    a1 = mergesort(a1 ,0,len(a1)-1)
    a2 = mergesort(a2, 0,len(a2)-1)
    print("a1:{0} ,a2:{1}".format(a1,a2))

    i=0
    j=0
    k=0
    c=[0]*len(a)
    while(i<len(a1) and j<len(a2)):
        if (a1[i] <= a2[j]):
            print("i:",i)
            c[k]=a1[i]
            print("Printing 1 .c:{0} ,a1:{1}".format(c[k], a1[i]))
            k=k+1
            i=i+1
        else :
            print("j:",j)
            c[k]=a2[j]
            print("Printing 2. c:{0} ,a2:{1}".format(c[k], a2[j]))
            k=k+1
            j=j+1

    if i<len(a1):
        while(i != len(a1)):
            c[k] = a1[i]

            k=k+1
            i=i+1
    elif j<len(a2):
        while(j != len(a2)):
            c[k] = a2[j]
            k = k + 1
            j = j + 1
    print("c:{0}".format(c))
    return c

# main function
if __name__ =="__main__":
    a = [1,4,2,3,1,5,6,3,4,5]
    l = 0
    r = len(a)-1
    res = mergesort(a,l,r)
    print(res)