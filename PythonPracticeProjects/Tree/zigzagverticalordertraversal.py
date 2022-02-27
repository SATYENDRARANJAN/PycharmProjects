from queue import  Queue

class Node():
    def __init__(self, val):
        self.left  = None
        self.right = None
        self.val = val

class BinaryTree():
    def __init__(self):
        self.head = None
        global queue
        queue = Queue()


    def printzigzag(self):
        # save on row
        # save other row reverted .
        # save each row reverted in the queue and print  left and right of the popped element .
        root = self.head
        ltr = True
        self.printzigzagutil(self.head , ltr)

    def printzigzagutil(self,node , ltr):
        if node is None :
            return

        current_level =[]
        next_level = []

        global  queue
        queue.put(node)
        while queue.qsize() !=0:
            popped_element = queue.get()
            print(popped_element.val)
            if ltr == True:
                if popped_element.left is not None:
                    queue.put(popped_element.left)
                if popped_element.right is not None:
                    queue.put(popped_element.right)
            else:
                if popped_element.right is not None:
                    queue.put(popped_element.right)
                if popped_element.left is not None:
                    queue.put(popped_element.left)

            ltr =not ltr




    def print_zig_zag_utit(self,node):
        ltr = False
        current__level_stack = []
        next_level_stack =[]
        current__level_stack.append(node)

        while len(current__level_stack)!= 0:
            popped_element = current__level_stack.pop()
            print(popped_element.val)
            if ltr == True :
                if popped_element.left is not None:
                    next_level_stack.append(popped_element.left)
                if popped_element.right is not None:
                    next_level_stack.append(popped_element.right)
            else:
                if popped_element.right is not None:
                    next_level_stack.append(popped_element.right)
                if popped_element.left is not None:
                    next_level_stack.append(popped_element.left)
            if len(current__level_stack) ==0:
                current__level_stack,next_level_stack = next_level_stack,current__level_stack
                ltr = not ltr


if __name__ == "__main__":
    root  = Node(0)
    btree = BinaryTree()
    btree.head = root
    l1 = Node(1)
    r1 = Node(2)
    l2 = Node(3)
    r2 = Node(4)
    l3 = Node(5)
    r3 = Node(6)
    l4 = Node(7)
    r4 = Node(8)

    btree.head.left = l1
    btree.head.right = r1
    l1.left =l2
    l1.right = r2
    r1.left = l3
    r1.right = r3
    l2.left = l4
    l2.right = r4

    btree.print_zig_zag_utit(btree.head)
