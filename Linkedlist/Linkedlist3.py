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

def insertSorted(head,x):
    node = Node(x)
    if head == None:
        return node
    elif x < head.data:
        node.next = head
        return node
    else:
        curr = head
        while curr.next != None and curr.next.data < x:
            curr = curr.next
        node.next = curr.next
        curr.next = node
    return head






head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)
printList(head)
head = insertSorted(None,3)
printList(head)