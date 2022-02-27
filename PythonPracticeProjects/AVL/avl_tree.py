class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1

# AVL Tree which supports the insert operation .
class AVLTree:
    def insert(self,node , key):
        # 1. normal insertion in BST
        # banlancing the tree using BF
        if node is None:
            return TreeNode(key)
        elif key < node.val:
            node.left = self.insert(node.left,key)
        else:
            node.right = self.insert(node.right,key)
        # 2. Update the height of the root node.
        node.height = 1 + max(self.get_height(node.left),self.get_height(node.right))
        # 3. Get balance factor
        balance = self.get_balance(node)
        # 4. If node is unbalanced , then try out the 4 cases .
        # Case 1 : Left Left .
        if balance >1 and key < node.left.val:
            return self.rotate_right(node)
        # Case 2 : Right Right
        if balance < -1 and key > node.right.val:
            return self.rotate_left(node)
        # Case 3 : Right Left
        if balance > 1 and key > node.left.val:
            return self.rotate_left_right(node)
        # Case 4 : Left Right
        if balance < -1 and key < node.right.val:
            return self.rotate_right_left(node)

    def rotate_right(self,node):
        temp = node.left
        temp1 = node
        temp.right = node

    def get_height(self,node):
        if node is None:
            return 0
        return node.height

    def get_balance(self,node):
        if node is None:
            return 0
        # return node.left.height - node.right.height
        return self.get_height(node.left) - self.get_height(node.right)