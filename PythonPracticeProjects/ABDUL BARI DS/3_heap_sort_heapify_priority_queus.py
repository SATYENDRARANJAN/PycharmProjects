# Heap - Complete binary tree
# minHeap- smaller no. - higher prioirity
# maxheap- larger no. higher priority

#  node at i
# left child  - 2i
# right child - 2i +1
# parent -  floor(i//2)

# insert and delete in max_heap
class Heap :
    def __init__(self):
        self.__arr =[]

    def parent(self,i):
        return i//2

    def decrease_key_at_index_to_maxinf_and_shift_up(self,i,new_val):
        # assuming new_val<arr[i]
        self.arr[i]=new_val
        # shift up
        while(i!=0 and self.array[self.parent(i)] > self.array[i]):
            self.array[i] , self.array[self.parent(i)] = self.array(self.parent(i)),self.array[i]
            i = self.parent(i)


    def extractMin(self):
        # Method to remove max element from the min heap
        # swap with the last element
        # heapify till n-1
        heap_size = len(self.arr)
        if heap_size <=0:
            return float("inf")
        if heap_size ==1:
            return self.array.pop(0)
        lastelement = self.array[-1]
        self.arr[0] = lastelement
        self.heapify(0)


    def heapify(self,i):
        #  compare to left and right child and swap down till it finds its position ,
        l = self.leftchild(i)
        r = self.rightchild(i)
        if l<self.size()-1 and self.arr[i]<self.arr[l]:
            largest = l
        if r<self.size()-1 and self.arr[i]<self.arr[r]:
            largest

    #operations
    def insert(self,val,index=None):
        # add it at last
        # find its parent and compare and shift
        # self.arr[i+1] = val
        self.arr.append(val)
        i = len(self.arr)-1
        while i>0 and self.arr[i]>self.arr[self.parent(i)]:
            self.arr[self.parent(i)],self.arr[i] = self.arr[i],self.arr[self.parent(i)]
            i = self.parent(i)

    def delete_key_at_index(self,index):
        # copy last  element from array at this index
        # heapify that index
        self.decrease_key_at_index_to_maxinf_and_shift_up(index,float("inf"))
        self.extractMin()














if __name__ =="__main__":
    maxheap = Heap()
    maxheap.insert(5)
    maxheap.insert(10)
    maxheap.insert(11)
    maxheap.insert(4)
    maxheap.insert(7)
    maxheap.insert(3)

    maxheap.delete(4)

    maxheap.delete_key_at_index(4)
    maxheap.printHeap()