class Node():
    def __init__(self,val):
        self.val = val
        self.next = None


class LinkedList():
    def __init__(self):
        self.head = None

    def printList(self):
        temp = self.head
        list =[]
        while temp != None:
            list.append(temp.val)
            temp = temp.next
        print(list)

    def revert_in_group_of_3_alternate(self, node,k ,turn):
        head = node
        next = None
        prev = None
        curr = head
        count = 0

        while curr!=None and count<k:
            if turn %2==1:
                next = curr.next
                curr.next = prev
                prev = curr
                curr = next
                count = count+1
            else:
                prev = curr
                curr = curr.next
                count = count +1

        if curr is not None:
            if turn % 2 == 1:
                head.next = self.revert_in_group_of_3_alternate(curr ,k,turn+1)
            else:
                prev.next = self.revert_in_group_of_3_alternate(curr, k, turn + 1)
        if turn % 2 == 1:
            return prev
        else : return  head



if __name__ == "__main__":

    ll = LinkedList()
    ll.head = Node(1)
    second = Node(2)
    third = Node(3)
    fourth = Node(4)
    fifth = Node(5)
    sixth = Node(6)
    seventh = Node(7)
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
    ll.head= ll.revert_in_group_of_3_alternate(ll.head,3,0)
    print("reversed list :{0}".format(ll.printList()))