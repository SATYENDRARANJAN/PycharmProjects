"""
Merge two sorted arrays using hashmap  in 0(n) time and 0(n) extra space .
"""
def next_gap(n):
    if n <=1:
        return 0
    return (n//2 + n%2)

def merge_2_sorted_arrays(a1, a2, l1, l2):
    x = min(l1,l2)
    n = l1+l2
    # FORM BOTH ARRAYS TO BE BITONIC
    # # SORT THEM USING IN-PLACE ALGO
    # for i in range(x):
    #     if a1[l1-i-1] > a2[i]:
    #         a1[l1-i-1],a2[i] =a2[i] ,a1[l1-i-1]

    # SORT THEM USING IN PLACE ALGO .
    gap = next_gap(n)
    while gap>0:
        i=0;
        while i + gap < l1:
            print (i , gap)
            if a1[i] > a1[i+gap]:
                a1[i], a1[i+gap] = a1[i+gap],a1[i]
            i=i+1

        j = i+gap-l1 if i+gap>l1 else 0
        while i<l1 and j<l2 :
            if a1[i] > a2[j]:
                a1[i],a2[j] = a2[j] ,a1[i]
            i+=1
            j+=1

        if (j<l2):
            while(j+gap < l2):
                if a2[j] >a2[j+gap]:
                    a2[j],a2[j+gap] = a2[j+gap],a2[j]
                j +=1
        gap = next_gap(gap)




if __name__== "__main__":
    a1 = [ 1, 5, 9, 10, 15, 20 ]
    l1 =len(a1)
    a2 = [ 2, 3, 8, 13 ]
    l2 = len(a2)
    merge_2_sorted_arrays(a1, a2, l1 , l2 )
    print (a1,a2)
