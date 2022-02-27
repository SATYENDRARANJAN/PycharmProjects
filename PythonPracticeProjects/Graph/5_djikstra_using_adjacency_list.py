# For djikstra using adjacency matrix time complexity is O(V^2)
# For djikstra using adjacency list , time complexity is O(V+E)
import sys
from builtins import list, len, str, range, float
from collections import defaultdict

# Heap  insert(), delete(), extractsMin() , decreaseKey() operations in O(logn) time .
# Priority queues can be efficiently implemented using binary heap .
# Binary Heap and Fibonacci Heap are variations of binary heap .
# These variations perform union also efficiently.
# getMini() : It returns root of element of minheap . Time complexity of this operation is O (1)
# extractMin() : removes

class Heap1:
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

    def heapify(self, k):
        smallest = k
        left_child = 2*k+1
        right_child = 2*k+2
        if left_child < self.heapsize() and self.array[k].dist > self.array[left_child].dist:
            smallest = left_child
        if right_child < self.heapsize() and self.array[k].dist > self.array[right_child].dist:
            smallest = right_child

        if smallest!= k:
            smallest_node = self.array[smallest]
            # swap positions
            self.pos[smallest],self.pos[k] = self.pos[k],self.pos[smallest]
            # swap nodes
            self.array[smallest] ,self.array[k] = self.array[k] , self.array[smallest]
            self.heapify(smallest)


    def print_heap(self):
        print(self.size())
        for i in range((self.size()-1)//2):
            print (i)
            print("Parent:" + str(self.array[i]) + "  left child: " + str(self.array[self.left(i)]) + "  right child : " + str(self.array[self.right(i)]))

class HeapNode:
    def __init__(self,id,dist):
        self.id=id
        self.dist=dist

    def __str__(self):
        return str(self.id) +" "+ str(self.dist)

class Heap:
    def __init__(self):
        self.array =[]
        self.pos=[]

    # utility
    def parent(self, i):
        return (i - 1) // 2

    def left(self, i):
        return 2 * i + 1;

    def right(self, i):
        return 2 * i + 2;

    def size(self):
        return len(self.array)

    # heap operations
    # Node are in format [u,dist]
    def insert_node(self,node):
        self.array.append(node)
        idx =len(self.array)-1
        # shift up
        self.shiftUp(idx)
        # i =0
        # while(i!=0 and self.array[self.parent(node[0])][1] >  self.array[node[0]][1]):
        #     self.array[self.parent(node[0])] ,self.array[node[0]] = self.array[node[0]] ,self.array[self.parent(node[0])]

    def shiftUp(self,idx):
        parentIdx = 0 if idx==0 else (idx-1)//2
        currentIdx = idx
        while (currentIdx > 0 and self.array[parentIdx].dist>self.array[currentIdx].dist):
            # swap parent and current nodes
            parent_node = self.array[parentIdx]
            current_node = self.array[currentIdx]
            parent_node,current_node = current_node,parent_node

            # swap their indexes or positions
            self.pos[parentIdx],self.pos[currentIdx] = self.pos[currentIdx],self.pos[parentIdx]

            currentIdx = parentIdx
            parentIdx=(parentIdx-1)//2

    def extractMin(self):
        heap_size =  len(self.array)
        if heap_size ==0 :
            return None
        if heap_size ==1:
            return self.array[0]

        minNode = self.array[0]
        lastNode =  self.array.pop(-1)
        self.array[0] = lastNode
        self.heapify(0)

        # change indexes of the min node and last node
        # setting pos of last node doesnt matter as it is already set to 0
        self.pos[lastNode.id] = 0

        return minNode

    def decreaseKey(self , val , vertex_id):
        # get the index which distance's need a decrease
        vertex_pos = self.pos[vertex_id]
        # update value in minheap ; its updated in heapnodes in previous function
        self.array[vertex_pos].dist = val
        self.shiftUp(vertex_pos)

    def heapify(self,i): # its actually minheapify
        l = self.left(i)
        r = self.right(i)
        smallest =i
        if l<self.size()-1 and self.array[i].dist>self.array[l].dist:
            smallest = l

        if r<self.size()-1 and self.array[i].dist>self.array[r].dist:
            smallest = r

        if smallest!=i:
            self.array[i],self.array[smallest]=self.array[smallest],self.array[i]
            self.heapify(smallest)
        self.print_heap()

    def isInMinHeap(self,id):
        if self.pos[id] < self.size():
            return True
        return False

    def print_heap(self):
        print(self.size())
        for i in range((self.size()-1)//2):
            print (i)
            print("Parent:" + str(self.array[i]) + "  left child: " + str(self.array[self.left(i)]) + "  right child : " + str(self.array[self.right(i)]))

class Graph:
    def __init__(self,v):
        self.V = v
        self.graph  = defaultdict(list)

    def addEdge(self,u,v,w):
        # As the graph is undirected , the edge will be bidirectionally added
        # edges are between nodes where Node has ("distance from parent" and id). Node here is taken as a list
        self.graph[u].append([v,w])
        self.graph[v].append([u,w])

    # The main function that calculates distance from source to all vertices
    def djikstra(self,src):
        # dist , spt ,
        # create minheap of all the vertices
        # pick the smallest element from the minheap
        # remove it from the minheap or mark it as visited
        # traverse all its neighbours and record the traversal time for unvisited
        # find  the SPT (dist[u] + spt[u] > dist[v] ? dist[v] = dist[u]+spt[u]:none)
        # record the parent of the neighbour

        # Get the number of vertices in graph dist values used to pick min weight edge in cut
        heapnodes =[]
        # minHeap represents set E
        minheap = Heap()
        print("minheap is : ")
        print (minheap)
        # create an array of nodes corresponding to each vertex to be inserted in minheap
        for i in range(self.V):
            heapnodes.append(HeapNode(i ,float("inf")))
        heapnodes[src].dist=0

        # Initialize "minHeap" with all vertices , "dist" values of all vertices
        for i in range(self.V):
            minheap.insert_node(heapnodes[i])
            minheap.pos.append(i)

        # initialize min src dist =0

        # extract min dist node.
        # find its neighbours
        # update the value of dist
        while(len(minheap.array)!=0):
            # extract the top
            minNode = minheap.extractMin()
            # extract the vertex id
            print("minNode:{}".format(minNode))
            extractedVertex_id = minNode.id
            extractedVertex_dist = minNode.dist

            for neighbour_node in self.graph[extractedVertex_id]:
                    print(neighbour_node)

            print("*****")
            for neighbour_node in self.graph[extractedVertex_id]:
                # its a graph saved in defaultdict {0: [0,1],1:[1,2]}
                print("fsdfsd : " )
                print(heapnodes[neighbour_node[0]])
                print(heapnodes)
                print(neighbour_node[0])
                curr_key = heapnodes[neighbour_node[0]].dist
                new_key = heapnodes[extractedVertex_id].dist +neighbour_node[1]
                if minheap.isInMinHeap(neighbour_node[0]) and \
                    curr_key > new_key:
                    minheap.decreaseKey(new_key,neighbour_node[0])
                    heapnodes[neighbour_node[0]].dist = new_key




if __name__=="__main__":
    graph = Graph(9)
    graph.addEdge(0, 1, 4)
    graph.addEdge(0, 7, 8)
    graph.addEdge(1, 2, 8)
    graph.addEdge(1, 7, 11)
    graph.addEdge(2, 3, 7)
    graph.addEdge(2, 8, 2)
    graph.addEdge(2, 5, 4)
    graph.addEdge(3, 4, 9)
    graph.addEdge(3, 5, 14)
    graph.addEdge(4, 5, 10)
    graph.addEdge(5, 6, 2)
    graph.addEdge(6, 7, 1)
    graph.addEdge(6, 8, 6)
    graph.addEdge(7, 8, 7)
    graph.djikstra(0)


