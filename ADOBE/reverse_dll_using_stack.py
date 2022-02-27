# Keep pushing nodes's data in the stack
# Keep popping the element's out and updating the DLL

class Node:
    def __init__(self,data):
        self.data = data
        self.next=None
        self.prev=None

class DLL:
    def __init__(self,data):
        self.head=None

    """Method to reverse using stack"""
    def reverse_using_stacks(self):
        stack=[]
        curr =self.head
        while curr is not None:
            stack.push(curr.data)
            curr=curr.next

        temp=self.head
        while len(stack)!=0:
            temp.data=stack.pop()
            temp= temp.next



    def reverse_using_recursion(self,node):
        if not node:
            return None

        temp=node.next
        node.next=node.prev
        node.prev=temp

        if not node.prev:
            return node

        return self.reverse_using_recursion(self,node.prev)