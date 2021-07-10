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
def reverseLinkedList(head):
    curr = head
    prev = None
    while curr != None:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next

    return prev

head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)
printList(head)
head = reverseLinkedList(head)
printList(head)

# O(N) O(1)