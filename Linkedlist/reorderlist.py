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

def reorderList(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    print(slow.data)
    second = slow.next
    prev = slow.next = None
    while second:
        next = second.next
        second.next = prev
        prev = second
        second = next

    #merge two halfs
    first,second = head,prev
    while second:
        tmp1,tmp2 = first.next,second.next
        first.next = second
        second.next = tmp1
        first,second = tmp1,tmp2

head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)
head.next.next.next.next = Node(50)
printList(head)
reorderList(head)
printList(head)

