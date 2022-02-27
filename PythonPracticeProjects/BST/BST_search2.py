class Node():
    def __init__(self,val):
        self.val = val
        self.right = None
        self.left = None


class BST():
    def __init__(self):
        self.root = None

    def search(self,key):
        if self.search_util(self.root , key):
            return True
        return False

    def search_util(self, node , key):
        if node.val == key:
            return True
        if node.val> key:
            if node.left is not None:
                return self.search_util(node.left ,key)
            else :
                return False
        elif node.val < key:
            if node.right is not None :
                return self.search_util(node.right , key)
            else:
                return False


    def insert_util(self, node ):
        if root is None:
            root = node





if __name__ == "__main__":
    bst = BST()
    bst.root = Node(1)
    bst.root.left = Node(2)
    bst.root.right = Node(3)
    bst.root.left.left = Node(4)
    print(bst.search(13))


