# According to the official Python documentation,
# __repr__ is a built-in function used to compute the "official" string reputation of an object,
# while
# __str__ is a built-in function that computes the "informal" string representations of an object

class Stack():
    def __init__(self):
        self.head = None


class Node():
    def __init__(self,val):
        self.val = val
        self.next  = None

    def __repr__(self):
        return  repr(self.val)


class LinkedList ():
    def __init__(self):
        self.head = None

    # Utility function to print nodes of Linked List
    def __repr__(self):
        nodes  =[]
        curr = self.head
        count =0
        while curr is not None :
            nodes.append(repr(curr))
            print("appending {0}".format(curr.val))
            curr = curr.next
            count = count +1

        return 'the list starts   ' + ', '.join(nodes) + '   ends'

    def printList(ll):
        temp = ll.head
        list =[]
        while temp != None:
            list.append(temp.val)
            temp = temp.next
        print (list)

    def reverse_using_stack(ll):
        # add 3 elements to  a stack
        # pop them and add to a list
        temp = ll.head
        newll = LinkedList()
        stack =[]
        curr = None
        listt=[]
        # push 2 top elements in stack
        while temp != None :
            count = 0
            while temp != None and count<3:
                print("adding temp {0}".format(temp.val))
                stack.append(temp)
                temp = temp.next
                count= count+1
            print ("stack is {0}".format(stack))
            # pop the 3 and add to newll
            while len(stack)!=0:
                if newll.head is None :
                    newll.head = stack.pop()
                    curr = newll.head
                    print("adding {0}".format(curr.val) )
                    listt.append(curr.val)
                else:
                    print(curr.val)
                    curr.next = stack.pop()
                    curr = curr.next
                    print("1..{0}".format(curr.val))
                    listt.append(curr.val)
                print(" len(stack) :{0}".format( len(stack)))
        curr.next =None
        print("out of loop")
        print(listt)
        return newll
        # newll.printList()










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
    elventh = Node(11)
    ll.head.next = second
    second.next = third
    third.next = fourth
    fourth.next = fifth
    fifth.next = sixth
    sixth.next = seventh
    seventh.next = eight
    eight.next = ninth
    ninth.next = tenth
    tenth.next = elventh

    newll = LinkedList()
    ll.printList()
    print(ll)
    newll = ll.reverse_using_stack()
    # ll.printlist()
    print(newll)

