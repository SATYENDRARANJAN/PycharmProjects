# / Before changing next of current,
# // store next node
# next = curr->next
# // Now change next of current
# // This is where actual reversing happens
# curr->next = prev
# // Move prev and curr one step forward
# prev = curr
# curr = next

class Node:
    def __init__(self,data):
        self.data=data
        self.next =None

class LinkedList:
    def __init__(self):
        self.head=None


    def reverse(self):
        prev =None
        curr =self.head

        while curr is not None:
            next=curr.next
            curr.next=prev
            prev=curr
            curr=next
        self.head=prev


    def reverse_using_recursion(self, prev, curr):
        if curr.next is None:
            self.head=curr
            curr.next=prev
            return
        next=curr.next
        curr.next=prev

        self.reverse_using_recursion(self, curr, next)

