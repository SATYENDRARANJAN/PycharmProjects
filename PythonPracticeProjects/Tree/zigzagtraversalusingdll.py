class Node():
    def __init__(self):
        self.next   = None
        self.previous = None
        self.val = None



class BinaryTree():
    def __init__(self):
        self.head = None



if __name__ == "__main__":
    btree = BinaryTree()
    btree.head = Node(1)
    second = Node(2)
    third = Node(3)
    forth = Node(4)
    fifth = Node(5)
    sixth = Node(6)
    seventh = Node(7)
    eight = Node(8)
    ninth = Node(9)
    tenth = Node(10)

    btree.zigzagtraversalusing_dll(btree.head)
