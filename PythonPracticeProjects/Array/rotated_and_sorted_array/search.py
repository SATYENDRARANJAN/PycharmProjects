# find the pivot
# if element > last element, search in left else in right .
# TIME COMPLEXITY : O(logN)
# SPACE COMPLEXITY :(O(1))
def pivotsearch(a,l,h):
    # base cases
    if h<l:
        return -1
    elif (h==l):
        return l
    mid =( (l+h)//2);
    if (mid<h and a[mid]>a[mid+1]):
        return mid
    if (mid>l and a[mid]<a[mid-1]):
        return mid-1
    if (a[mid]>a[h]):
        return pivotsearch(a, mid + 1, h)
    return pivotsearch(a,l,mid-1)




def pivoted_binary_search(a,n,key):
    pivot = pivotsearch(a,0,n)
    #if no privot , means array not rotated
    if pivot==-1:
        return search(a,0,n,key)
    if key==a[pivot]:
        return pivot
    elif key<a[pivot]:
        return search(a,pivot+1,n,key)
    return search(a,0,pivot-1,key)



def search(a,l,h,key):
    if l>h:
        return -1

    mid =(l+(h-l))//2
    if key == a[mid]:
        return mid
    elif key>a[mid]:
        return search(a,mid+1,h,key)
    return search(a,l,mid-1,key)



if __name__ == "__main__":
    a=[7,8,9,1,2,3,4,5,6]
    k=3
    index=pivoted_binary_search(a,len(a)-1,k)
    # index=search(a,0,len(a)-1,k )
    print(index)