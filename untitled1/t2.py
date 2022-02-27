# Head → [] → 	[] → 	[] → 	[] → null
# 	A	D		F
# 	B	E
# 	C
#
#
# Node {
# char[] elements; 		// Max Length = 5
# Int numOfElements;
# Node next;
# }
#
#
# find(head, position) {
#
# }

class Node:
    def __init__(self,data=[],num=0,next=None):
        self.data =data
        self.size=num
        self.next=next



def find(head, position):
    node = head
    if node ==None:
        return
    index = -1
    while node!=None :
        if index<position and index+node.size >=position:
            return node.data[position-index-1]
        else:
            index+=node.size
        node=node.next

    return "Not present"

# Starting point
if  __name__ =="__main__":
    head  = Node(['A','B','C'],3)
    n1= Node(['D','E'],2)
    n2= Node()
    n3= Node(['F'],1)
    n4= Node()
    head.next=n1
    n1.next=n2
    n2.next=n3
    n3.next=n4
    position =5
    k =find(head,position)

    print(k)


