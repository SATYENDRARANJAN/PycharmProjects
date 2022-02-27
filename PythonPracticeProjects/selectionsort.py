
# find min from [i+1] to n
# replace it with a[i]
def selection_sort(arr):
    for i in range(len(arr)):
        min_idx =i
        for j in range(i+1,len(arr)):
            if arr[min_idx] >arr[j]:
                min_idx =j
        arr[min_idx] ,arr[i] =arr[i],arr[min_idx]
        print (arr)
    return arr



if __name__ =="__main__":
    arr = [23,24,95,23,45,45,34,55]
    print("final answer is {0}".format(selection_sort(arr)))



# # find the min element from i = 0 to n-1 .
# # replace it with
#
# def insertion_sort(a):
#     # select one element and compare it with all others .
#     print (a)
#     n = len (a)
#     for i in range(1,n):
#         ptr = a[i]
#         ptr_idx = i
#         j=0
#         for j in reversed(range(0 , i)):
#             print ("fsdfs  "+ str(j) +" "+str(ptr_idx) +"" )
#             if a[j] >= ptr:
#                 a[j+1] =a[j]
#             else:
#                 break
#         a[j+1]=ptr
#         print(a)
#     print("ww ~~ ")
#
#
#
#
#
# if __name__ == "__main__":
#     arr = [19, 29, 49, 34, 22, 34, 54]
#     print(insertion_sort(arr))
