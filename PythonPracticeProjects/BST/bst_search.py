class  Node():
    def __init__(self,val):
        self.val = val
        self.right = None
        self.left = None


class BST():
    def __init__(self ):
        self.root  = None

    def search(self,node,key):
        if node is not None and node.val == key:
            return True
        if node.left is not None and node.val > key:
            return self.search(node.left,key)
        if node.right is not None and node.val < key:
            return self.search(node.right,key)
        return False


    def print(self,node):
        if node is  None :
            return
        print (node.val)
        self.print (node.left)
        self.print (node.right)


if __name__ == "__main__":

    bst = BST()
    bst.root = Node(10)
    bst.root.left = Node(5)
    bst.root.right = Node(15)
    bst.root.left.left = Node(2)
    bst.root.left.right = Node(7)
    bst.root.right.left = Node(13)
    bst.root.right.right = Node(17)
    bst.print(bst.root)
    print(bst.search(bst.root , 5))



