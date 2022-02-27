# heap is saved in arr form
# heapify the tree
# root has the largest
# swap the root with the last element .
# largest becomes the last element
# heapify root to a[largest -1] elements now .

def heapify(a, node , last):
    largest =node
    left = 2*node +1
    right = 2*node +2
    print("left : {0} last: {1} right : {2}".format(left,last,right))
    if left<last and a[left] > a[largest]:
        largest = left
    if right<last and a[right] > a[largest]:
        largest = right
    if largest != node:
        a[largest],a[node]=a[node],a[largest]
        heapify(a, largest ,last)



def heapifyTree(a, node ,last):
    # heapify the tree
    for i in range((last-1)//2, -1 ,-1):
        print('\n')
        print("***** HEAPIFYING  LENGTH {0} to {1} ****".format(i,last))
        heapify(a , i , last+1)
        #swap node and last



def heapsort(a , start , length):
    for i in range( length-1, -1, -1):
        print("******************* HEAPIFYING TREE LENGTH {0}  **********************".format(i))
        heapifyTree(a,start,i)
        print("after heapify:{0}".format(a))
        a[i],a[0] = a[0],a[i]


if __name__ == '__main__':
    a =[1,2,8,4,2,3,4,5,3,2,22,3]
    heapsort(a,0,len(a))
    print(a)