"""
Merge using O(m*n) using O(1) extra space .
Create an array a3 of m+n size  OR  use only 2 arrays
Copy a1 into a3 .
Perform insertion sort by copying elements of a2 into a1 .
each element of a2 is inserted into right place in a3
"""


def merge_array(arr1 , arr2):
    arr3= []
    l1 = len(arr1)
    l2 = len(arr2)

    for i in range(l2-1,-1,-1):
        last = arr1[l1-1]
        for j in range(l1-1,-1,-1):
            print("comparing {0} and {1}".format(arr2[i],arr1[j]))
            if arr1[j] >= arr2[i]  :
                if j != l1-1:
                    arr1[j+1]=arr1[j]
                else :
                    last = arr1[j]
            else :
                break
        print(arr1)
        print(arr2)
        print("\n")
        print("out of inner loop")
        arr1[j+1] = arr2[i]
        arr2[i] = last

        print(arr1)
        print(arr2)
    print("out of outer loop")
    print (arr1 + arr2)


if __name__ == "__main__":
    arr1 = [1,2,3,15,16,19]
    arr2 = [1,4 ,8,9,9]
    merge_array(arr1,arr2)