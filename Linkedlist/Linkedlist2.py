class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def printList(head):
    curr = head
    llstr = ' '
    while curr:
        llstr += str(curr.data)+'--->' if curr.next else str(curr.data)
        curr = curr.next

    print(llstr)

def insertAtStart(head,x):
    node = Node(x)
    node.next=head
    head=node
    return node

def insertATEnd(head,x):
    node = Node(x)
    curr = head
    while curr.next:
        curr = curr.next
    curr.next = node


def deletAtEnd(head):
    curr = head
    while curr.next.next:
        curr = curr.next
    curr.next = None

def deleteAtStart(head):
    return head.next



head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
printList(head)
head = insertAtStart(head,5)
printList(head)
insertATEnd(head,50)
printList(head)
deletAtEnd(head)
printList(head)
head = deleteAtStart(head)
printList(head)