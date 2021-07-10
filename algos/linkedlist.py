class Node:
    def __init__(self,data=None,next=None):
        self.data= data
        self.next= next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self,data):
        node = Node(data,self.head)
        self.head = node
        print("begin",node)

    def print(self):
        if self.head is None:
            print ("linked list is empty")
        itr = self.head
        print(itr)
        llstr = ''
        while itr:
            llstr += str(itr.data) + '-->'
            print(itr)
            itr = itr.next
        print(llstr)
    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data,None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data,None)
        print("end",itr.next
        )



if __name__ == '__main__':
    ll = LinkedList()
    ll.print()
    ll.insert_at_beginning(5)
    ll.insert_at_beginning(89)
    ll.insert_at_end(100)
    ll.print()
