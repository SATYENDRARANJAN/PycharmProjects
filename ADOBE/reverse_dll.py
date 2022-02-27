
#TC: o(n) , SC:O(1)

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None


class DoublyLinkList:
    def __init__(self):
        self.head=None


    def reverse(self):
        temp=None
        current=self.head

        while current is not None:
            temp=current.prev
            current.next=current.prev
            current.prev=temp
            current=current.prev

        #finally , temp contains last node and current contains null .
        #check for cases like empty list and list with one node,before swapping heads (Need not swap if if <1 nodes present)
        if temp is not None:
            self.head=temp.prev


        current  = self.head
        while current is not None:
            temp = current.prev
            current.prev=current.next
            current.next = temp
            current= current.prev

        if temp is not None:
            self.head=temp.prev


    def push(self,data):
        temp = Node(5)
        temp.prev= None
        if self.head is not None:
            self.head.prev=temp
        temp.next=self.head
        self.head=temp


    def printlist(self):
        current=self.head
        while current is not None:
            print(current.data)
            current=current.next


if __name__=="__main__":
    dll = DoublyLinkList()
    dll.push(5)
    dll.push(3)
    dll.push(5)

    dll.reverse()

    dll.printlist()



