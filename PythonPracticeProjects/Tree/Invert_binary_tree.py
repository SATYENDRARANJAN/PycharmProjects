# Inverting a binary tree using preoder traversal .

class Node:
    def __init__(self,val,left = None , right = None):
        self.left  = left
        self.right = right
        self.val = val
    def swap(self):
        # print (self.right)
        self.left,self.right = self.right, self.left

class BinaryTree:
    def __init__(self):
        self.root = None

    #inverting using preorder traversal
    def invert_tree(self):
        root = self.root
        self.invert_using_preorder(root)

    def invert_using_preorder(self,node):
        if node is not None:
            # self.swap(node)
            node.swap()
            self.invert_using_preorder(node.left)
            self.invert_using_preorder(node.right)
        return

    def swap(self,node):
        temp = node.left
        node.left = node.right
        node.right = temp

    def print_tree(self):
        if self.root is not None:
            self.print_tree_util(self.root)


    def print_tree_util(self,node):
        if node is not None:
            print(node.val)
            self.print_tree_util(node.left)
            self.print_tree_util(node.right)
        return




if __name__ == "__main__":
    btree = BinaryTree()
    btree.root = Node(1)
    l1 = Node(2)
    r1 = Node(3)
    l2 = Node(4)
    r2 = Node(5)
    l3 = Node(6)
    r3 = Node(7)
    l4 = Node(8)
    r4 = Node(9)
    btree.root.left = l1
    btree.root.right = r1
    l1.left = l2
    l1.right = r2
    r1.left = l3
    r1.right = r3
    l2.left = l4
    l2.right = r4

    btree.invert_tree()
    btree.print_tree()