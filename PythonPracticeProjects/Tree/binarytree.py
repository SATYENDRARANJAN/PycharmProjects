from queue import Queue

class Node():
    def __init__(self,val):
        self.right =None
        self.left = None
        self.val = val


class BinaryTree():
    def __init__(self):
        self.head = None
        global queuelist
        queue_list =Queue()

    def printbt(self):
        print("BINARY TREE is :")
        printNode(self.head)

    def printNode(self, node):
        print(node.val)
        if node.left is not None:
            self.printNode(node.left)

        if node.right is not None:
            self.printNode(node.right)

        print("\n")

    def print_level_order_traversal(self,node):
        # user a queue
        # save the root
        # pop the node
        # push its children in queue ,pop again
        global  queue_list

        queue_list = Queue()
        queue_list.put(node)

        while queue_list.qsize() !=0 :
            popped_node =queue_list.get()
            print(popped_node.val)

            if popped_node.left is not None:
                queue_list.put(popped_node.left)
            if popped_node.right is not None :
                queue_list.put(popped_node.right)


    def print_level_order_traversal_iterative_on2(self):
        # find height of the tree
        # traverse from root till each node on that height
        # print that node
        h = self.find_height(self.head)
        for i in range(1,h+1):
            self.printLevel(self.head, i)

    def find_height(self,root):
        if root is None:
            return 0
        else:
            lheight = self.find_height(root.left)
            rheight = self.find_height(root.right)
            return 1 + max(lheight,rheight)

    def printLevel(self,node, level):
        if node is None:
            return
        if level == 1:
            print(node.val)
        else:
            self.printLevel(node.left,level-1)
            self.printLevel(node.right , level-1)





    def print_vertical_order_traversal(self,root):
        # Find min max of a tree
        # for i in range min ot max
        # got from root to i and print  when current node level =i
        min = 0
        max = 0
        min , max = self.find_min_max(root , min , max ,0)
        print("min : {0} max :{1}".format(min,max))
        for i in range(min , max+1):
            print("min .. : {0} max .. :{1} i : {2}".format(min, max,i))
            self.print_vertical_node(root , 0 , i )

    def find_min_max(self, node,min,max,hd):
        if node is None:
            return min,max

        min = hd if hd < min else min
        max = hd if hd > max else max

        min ,max = self.find_min_max(node.left , min , max , hd-1)
        min ,max = self.find_min_max(node.right, min , max , hd+1)

        return min, max

    def print_vertical_node(self,node,curr_level ,i):
        if node is None:
            return
        if curr_level == i:
            print(node.val)
        self.print_vertical_node(node.left ,curr_level-1,i)
        self.print_vertical_node(node.right,curr_level+1,i)

if __name__ == "__main__":
    binary_tree=BinaryTree()
    binary_tree.head = Node(0)
    l1 = Node(1)
    r1 = Node(2)
    l2 = Node(3)
    r2 = Node(4)
    l3 = Node(5)
    r3 = Node(6)
    l4 = Node(7)
    r4 = Node(8)

    binary_tree.head.left = l1
    binary_tree.head.right = r1
    l1.left =l2
    l1.right = r2
    r1.left = l3
    r1.right = r3
    l2.left = l4
    l2.right = r4

    # binary_tree.print_level_order_traversal(binary_tree.head)
    print("height:", binary_tree.find_height(binary_tree.head))

    # binary_tree.print_vertical_order_traversal(binary_tree.head)
    binary_tree.print_level_order_traversal_iterative_on2()
