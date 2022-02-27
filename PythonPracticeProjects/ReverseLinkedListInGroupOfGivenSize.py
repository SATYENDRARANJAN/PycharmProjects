
class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        li = []
        while(temp):
            li.append(temp.val)
            temp= temp.next
        return li



    def revert_in_group_of_3(self,node,k):
        #  3-2-1  6-5-4  9-8-7
        prev = None
        head = node
        curr = head
        count =0
        next = None
        while(curr != None and count < k):
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
            count = count +1

        if next is not None:
            head.next = self.revert_in_group_of_3(next, k)
        return prev




if __name__ =="__main__":
    ll = LinkedList()
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

    ll.printList()
    ll.head= ll.revert_in_group_of_3(ll.head,4)
    print("reversed list :{0}".format(ll.printList()))

