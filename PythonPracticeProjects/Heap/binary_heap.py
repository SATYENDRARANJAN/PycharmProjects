# Heap  insert(), delete(), extractsMin() , decreaseKey() operations in O(logn) time .
# Priority queues can be efficiently implemented using binary heap .
# Binary Heap and Fibonacci Heap are variations of binary heap .
# These variations perform union also efficiently.
# getMini() : It returns root of element of minheap . Time complexity of this operation is O (1)
# extractMin() : removes
from builtins import len, float, range, str


class Heap:
    def __init__(self):
        self.array =[]

    def newMinHeapNode(self,v,dist):
        minHeapNode = [v,dist]
        return minHeapNode

    # utility
    def parent(self,i):
        return (i-1)//2

    def left(self,i):
        return 2*i+1;

    def right (self,i):
        return 2*i+2;

    def size(self):
        return len(self.array)

    # Operations
    def insert(self,key):
        #everytime we insert a key we check whether key satisfies min heap property
        i = len(self.array)-1
        self.array.append( key)
        # shift up
        while(i!=0  and self.array[self.parent(i)]>self.array[i]):
            self.array[self.parent(i)] ,self.array[i] = self.array[i],self.array[self.parent(i)]
            i = self.parent(i)

    def delete_key_at_index(self,i):
        self.decreaseKey_at_index(i , float("-inf"))
        return self.extractMin()

    def decreaseKey_at_index(self, i, new_val):
        # assuming new_val < array[i]
        self.array[i]= new_val
        # shift up
        while(i!=0 and self.array[self.parent(i)] > self.array[i]):
            self.array[self.parent(i)] ,self.array[i] = self.array[i] ,self.array[self.parent(i)]
            i = self.parent(i)

    # Method to remove min element from the minheap
    def extractMin(self):
        # swap with the last element
        # heapify till len -1
        heap_size = len(self.array)
        if heap_size<=0:
            return float("inf")
        if heap_size ==1 :
            return self.array.pop(0)
        # if size >2 . swap with last and heapify
        root = self.array[0]
        self.array[0]= self.array.pop(self.size()-1)
        self.heapify(0)
        return root

    def print_heap(self):
        print(self.size())
        for i in range((self.size()-1)//2):
            print (i)
            print("Parent:" + str(self.array[i]) + "  left child: " + str(self.array[self.left(i)]) + "  right child : " + str(self.array[self.right(i)]))


    def heapify(self,i): # its actually minheapify
        l = self.left(i)
        r = self.right(i)
        smallest =i
        if l<self.size()-1 and self.array[i]>self.array[l]:
            smallest = l

        if r<self.size()-1 and self.array[i]>self.array[r]:
            smallest = r

        if smallest!=i:
            self.array[i],self.array[smallest]=self.array[smallest],self.array[i]
            self.heapify(smallest)
        self.print_heap()

if __name__=="__main__":
    minHeap =Heap()
    minHeap.insert(5)
    minHeap.insert(3)
    minHeap.insert(17)
    minHeap.insert(10)
    minHeap.insert(84)
    minHeap.insert(19)
    minHeap.insert(6)
    minHeap.insert(22)
    minHeap.insert(9)
    print(minHeap.array)
    minHeap.print_heap()

    minHeap.delete_key_at_index(6)
    print(minHeap.array)

    minHeap.print_heap()
