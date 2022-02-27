class Node():
    def __init__(self,val):
        self.val= val
        self.next = None


class Linkedlist():
    def __init__(self):
        self.head = None

    def reverse(ll):
        prev = None
        curr = ll.head
        ll.printLL()
        while curr!= None:
            n = curr.next
            curr.next = prev
            prev = curr
            curr = n
        curr =prev
        ll.head= curr

    def printLL(self):
        curr = self.head
        list =[]
        while(curr!=None):
            list.append(curr.val)
            curr = curr.next
        print("list is {0}".format(list))


if __name__ == "__main__":
    ll = Linkedlist()
    ll.head = Node(1)
    second = Node(2)
    third = Node(3)
    fourth = Node(4)
    fifth = Node(5)
    sixth = Node(6)
    seventh =Node(7)
    eight = Node(8)
    ninth = Node(9)
    tenth = Node(10)
    ll.head.next = second
    second.next = third
    third.next = fourth
    fourth.next = fifth
    fifth.next = sixth
    sixth.next = seventh
    seventh.next = eight
    eight.next = ninth
    ninth.next = tenth
    # ll.printLL()
    ll.reverse()
    ll.printLL()