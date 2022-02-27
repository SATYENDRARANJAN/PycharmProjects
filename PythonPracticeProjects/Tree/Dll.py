class Node():
    def __init__(self,val):
        self.next   = None
        self.prev = None
        self.val = val

class Dll():
    def __init__(self):
        self.head = None
        self.tail= None

    def add_at_head(self,val):
        new_node = Node(val)
        new_node.next = None
        if self.head != None:
            print("adding second time")
            new_node.prev = self.head
            self.head.next = new_node
            self.head = self.head.next
        else:
            print("adding_for_first_time")
            self.head = new_node
            self.tail = self.head

    def add_at_tail(self,val):
        new_node = Node(val)
        new_node.prev = None
        if self.tail != None:
            self.tail.prev = new_node
            new_node.next = self.tail
            self.tail = self.tail.prev
        else:
            self.tail = new_node
            self.head = self.tail

    def remove_from_head(self):
        if self.head is None:
            return self.head
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            curr = self.head
            self.head = self.head.prev
            self.head.next = None
            curr.prev = None

    def remove_from_tail(self):
        if self.tail is None :
            return self.tail
        if self.tail == self.head:
            self.tail = None
            self.head = None
        else:
            curr = self.tail
            self.tail = self.tail.next
            self.tail.prev = None
            curr.next = None

    def printdll(self):
        curr = self.tail
        list =[]
        while curr :
            list.append(curr.val)
            curr = curr.next
        print (list)


if __name__ == "__main__":
    dll = Dll()
    first = Node(1)
    second = Node(2)
    third = Node(3)
    forth = Node(4)
    fifth = Node(5)

    dll.add_at_head(1)
    dll.printdll()
    dll.add_at_head(2)
    dll.printdll()
    dll.add_at_tail(3)
    dll.printdll()
    dll.add_at_tail(4)
    dll.printdll()
    dll.remove_from_head()
    dll.printdll()
    dll.remove_from_tail()
    dll.printdll()


