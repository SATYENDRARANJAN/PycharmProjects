# choose a pivot .
# find from where to partition
# quicksort with partitions


def quicksort(a, l , h):
    if l<h:
        # pi_index is partitioning index
        pi_index = partition(a, l , h)
        quicksort(a, l , pi_index-1)
        quicksort(a, pi_index+1 , h)
        print( "Sorted array is {0} ".format(a))
    return a


def partition(a , l , h):
    # choose a pivot position
    # define a swp index and at l-1
    # increment swap and swap with l if a[l] >pivot
    pivot= a[h]
    swp_idx = l-1
    i=0
    for i in range(l, h):
        if a[i]<pivot:
            swp_idx =swp_idx+1
            a[swp_idx],a[i]=a[i],a[swp_idx]

    a[swp_idx+1],a[h]=a[h],a[swp_idx+1]
    return swp_idx+1

def partition2(a, l ,h):
    pivot = a[h]
    i = l-1
    for j in range(l, h):
        if a[j]>pivot:
            i=i+1
            a[i],a[j] = a[j],a[i]
    a[i+1] , a[h]= a[h],a[i+1]
    return i+1 # THE ONLY SORTED NO. IN WHOLE ARRAY AFTER 1 FUNCTION EXECUTINO.





# # choose a pivot
# # find from where to partition
# # quicksort both partitions
# def quicksort(a,l,h):
#     if(l<h):
#         # pi_idx is partitioning index
#         pi_idx = partition(a, l , h)
#         quicksort(a , l , pi_idx-1)
#         quicksort(a , pi_idx +1, h)
#         print(a)
#
#         return a
#
#
# def partition(a , l , h ):
#     pivot = a[h]
#     swp_idx =l -1
#
#     i=0
#     for i in range(l , h):
#         if a[i]< pivot:
#             swp_idx = swp_idx +1
#             a[swp_idx],a[i] =a[i],a[swp_idx]
#     a[h] , a[swp_idx+1] = a[swp_idx+1],a[h]
#     return swp_idx+1
#
#
#
if __name__ =="__main__":
    arr = [2,12,3,5,63,3,5,6,3,33,3,5,66,3]
    res =quicksort(arr,0,len(arr)-1)
    print("ans:",res)