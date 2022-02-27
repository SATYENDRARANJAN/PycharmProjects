# Note:
# Root is at index 0 in array.
# Left child of i-th node is at (2*i + 1)th index.
# Right child of i-th node is at (2*i + 2)th index.
# Parent of i-th node is at (i-1)/2 index.
def heapify(arr , node , last ):
    largest = node
    left = 2*node+1
    right = 2*node+2
    # find largest in the subtree
    if left<last and a[left]>a[node]:
        largest = left
    if right<last and a[right]>a[node]:
        largest = right
    if largest != node:
        # swap a[node] and a[largest]
        a[node],a[largest] = a[largest] ,a[node]
        heapify(arr , largest ,last)
        print (arr)





def buildHeap(a):
    last_non_leaf_node = (len(a)//2)-1
    for i in range(last_non_leaf_node,-1,-1):
        heapify(a, i,len(a))


if __name__ == "__main__":
    a = [32,45,2,1,68,5,23,6,9,77]
    buildHeap(a)
    print(a)