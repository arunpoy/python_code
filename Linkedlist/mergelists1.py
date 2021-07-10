class Node:
    def __init__(self,data=None):
        self.data = data
        self.next = None

def printList(head):
    curr = head
    llstr = ' '
    while curr:
        llstr += str(curr.data)+'--->' if curr.next else str(curr.data)
        curr = curr.next

    print(llstr)
def merge_sorted(head1,head2):
    dummy = Node()
    tail = dummy
    while head1 and head2:
        if head1.data < head2.data:
            tail.next = head1
            head1= head1.next
        else:
            tail.next = head2
            head2 = head2.next
        tail = tail.next
    if head1:
       tail.next = head1
    if head2:
       tail.next = head2
    return dummy.next

head1 = Node(10)
head1.next = Node(20)
head1.next.next = Node(30)
head2 = Node(11)
head2.next = Node(19)
head2.next.next = Node(45)
printList(head1)
printList(head2)
new_head = merge_sorted(head1,head2)

printList(new_head)
