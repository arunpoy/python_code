class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def printList(head):
    curr = head
    while curr!= None:
        print(curr.data,end =" ")
        curr = curr.next

def findMiddle(head):
    slow = head
    fast = head
    while fast and  fast.next:
        slow = slow.next
        fast = fast.next.next


    print("The middle element is ", slow.data)

#driver
head = Node(10)
head.next=Node(20)
head.next.next=Node(30)
head.next.next.next = Node(40)
head.next.next.next.next = Node(50)

printList(head)
findMiddle(head)

