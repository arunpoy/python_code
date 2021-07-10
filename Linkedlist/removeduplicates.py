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

def removeDuplicates(head):
    curr = head
    while curr != None:
        nextDistinct = curr.next
        while nextDistinct!= None and nextDistinct.data == curr.data:
            nextDistinct = nextDistinct.next
        curr.next = nextDistinct
        curr = nextDistinct
    return head

head = Node(10)
head.next = Node(10)
#head.next.next = Node(20)
#head.next.next.next = Node(30)
#head.next.next.next.next= Node(30)
#head.next.next.next.next.next=Node(40)
printList(head)
head = removeDuplicates(head)
printList(head)