"""merge 2 sorted arrays in TC : O(m+n) using space 0(m+n)
Performing merge sort's function to merge 2 arrays by copying them into a new array .

Take 2 pointers pointing each array .
and compare the current nos. and add largest to third .
In the end add the remaining uncompared elements of the larger array to the new array .
TC : 0(M+N)
SP = O(M+N)

"""
def merge_2_sorted_arrays(arr1 , arr2):
    l1 = len(arr1)
    l2 = len(arr2)
    print (l1, l2)

    min_l = l1 if l1<l2 else l2

    i = 0
    j = 0
    k = 0
    arr3 = []
    while i < l1 and j< l2:
        if arr1[i] < arr2[j]:
            arr3.append(arr1[i])
            i += 1
        else:
            arr3.append(arr2[j])
            j += 1
    print(arr3)

    # merging the remaining elements
    if i<l1:
        print("l1>l2")
        while i!=l1:
            arr3.append(arr1[i])
            i += 1
    if j<l2:
        print("l2>l1")
        while j!=l2:
            arr3.append(arr2[j])
            j += 1
    print (arr3)

if __name__ == "__main__":
    arr1 = [1,2,3,4,5,6,7,9]
    arr2 = [3,4,5,67,88]
    merge_2_sorted_arrays(arr1 , arr2)

