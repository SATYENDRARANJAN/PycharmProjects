


def binary_search(a,l,h):
    mid= l+(h -l)//2
    i=0
    if mid<=h and a[mid]>a[mid+1]:
        i=mid
    elif a[mid]>a[h]:
        binary_search(a,l,mid-1)
    else:
        binary_search(a,mid,h)




def find_if_sum_exists(a,l):
    #find the pivot  either linear search in (o(n)) OR binary search of  point with a[i+1]<a[i]
    pivot_idx = binary_search(a,l)
    # use the two pointer method (meet in the middle algo)
    # as array is sorted and rotated - use a mod
    # pivot_idx is the idx by which it is rotated
    # incremented and decremented in rotational manner using mod









if __name__ == "__main__":
    a=[6,7,8,1,2,3,4,5]
    find_if_sum_exists(a,len(a))