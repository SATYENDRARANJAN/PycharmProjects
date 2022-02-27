

#Divide array in sets of length =gcd(d,n)

def gcd(a,b):
    if a==0:
        return b
    if b==0:
        return a
    if a==b:
        return a
    if a>b:
        return gcd(a-b,b)
    else:
        return gcd(a,b-a)


def juggling_swap_algo(a,d,l):
    g = gcd(d,l)
    i = 0
    for i in range(g):
        temp =a[i]
        j=i
        while(1):
            k=j+d
            if k>=l:
                k=k-l
            if k==i:
                break
            a[j]=a[k]
            j=k
        a[j]=temp



            if j>l:

                arr[i] = arr[i+d]







if __name__=="__main__":
    arr=[1,2,3,4,5,6,7,8,9,10,11,12]
    d=4
    l =len(arr)

    juggling_swap_algo(arr,d,len(arr))