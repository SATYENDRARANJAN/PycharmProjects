from queue import Queue


class Node():
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None


# O(h) where h is the height is the complexity of insert operation in BST



class BST():
    def __init__(self):
        self.root = None

    def insert(self,key):
        return self.insert_util(self.root,key)

    def insert2(self , key):
        return self.insert2_util(self.root , key)

    def insert2_util(self,node, key):
        if node is None:
            return Node(key)
        else:
            if node.val > key :
                node.left = self.insert2_util(node.left , key)
            elif node.val < key:
                node.right = self.insert2_util(node.right , key)
        return node

    def print(self):
        self.print_util(self.root)

    def print_util(self,node):
        if node is None :
            return
        print(node.val)
        if node.left is not None:
            self.print_util(node.left)
        if node.right is not None:
            self.print_util(node.right)

    def insert_util(self, node , key ):
        # goto root
        # if root is none , insert in root ,
        # if > root ; insert(root.right)
        # elif <root : insert (root.left)
        if node is None:
            node = Node(key)
        else:
            if node.val <key:
                if node.right is None:
                    node.right = Node(key)
                else :
                    self.insert_util(node.right ,key)
            else:
                if node.left is None:
                    node.left = Node(key)
                else:
                    self.insert_util(node.left,key)

    def min_value_node(self,node):
        curr = node
        while curr.left is not None:
            curr = curr.left
        return curr

    def delete_key(self,key):
        self.delete_key_util(self.root,key )

    def delete_key_util(self, node , key):
        # base case
        if node is None:
            return None

        # to be deleted from left subtree or right subtree
        if key < node.val:
            node.left = self.delete_key_util(node.left,key)
        elif key > node.val :
            node.right = self.delete_key_util(node.right,key)
        # if key is same as root's key then this is the node to be deleted
        # handle 3 cases of 0,1,2, childres
        else:
            # case for 0 or 1 child nodes
            if node.left is None :
                temp = node.right
                node = None
                return temp
            elif node.right is None:
                temp = node.left
                node = None
                return temp
            # case for 2 child nodes -  return the min from the right subtree
            temp = self.minValueNode(node.right)
            node.key = temp.key
            node.right = self.delete_key_util(node.right,temp.key)
        return node

    def calculate_left_space(self,level , i ):
        pass

    def printlevel(self,level , queue):
        item =0
        while item < queue.qsize():
            left_space = self.calculate_left_space(level, item)
            print(left_space*" ",end='')


    def printelement(self,level, i , node):
        left_space = self.calculate_left_space(level, i )

    def print_tree(self):
        # find the height of the tree
        height = self.height(self.root)
        print ("Height is : {0}".format(height))
        root = self.root
        # traverse tree level order
        queue = Queue()
        queue.put(root)
        level = 1
        while queue.qsize() !=0:
            count = queue.qsize()
            left_space_count = self.calculate_left_space()
            # queue has elements of current level
            self.printlevel(level ,queue)

            while count !=0:
                popped_node = queue.get()

                print(popped_node.val ,end =' ')
                if popped_node.left is not None:
                    queue.put(popped_node.left)
                if popped_node.right is not None:
                    queue.put(popped_node.right)
                count -=1
            level +=1


            print('')










    def height(self,node):
        if node is None:
            return 0
        return (max(self.height(node.left),self.height(node.right)))+1


if __name__ == "__main__":
    bst = BST()
    bst.root = Node(5)
    bst.root.left = Node(2)
    bst.root.right = Node(13)
    bst.insert(4)
    bst.insert(9)
    bst.insert(8)
    bst.insert(6)
    bst.insert2(7)
    # bst.delete_key(8)
    # bst.delete_key(9)
    bst.print_tree()



