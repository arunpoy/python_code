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
def merge_sorted(head1,head2):
    # if one of the lists is empty then other is the merged list
    if head1 == None:
        return head2
    elif head2 == None:
        return head1

    mergedHead = None
    if head1.data <= head2.data:
        mergedHead = head1
        head1 = head1.next
    else:
        mergedHead = head2
        head2 = head2.next

    mergedTail = mergedHead

    while head1 != None and head2 != None:
        temp = None
        if head1.data <= head2.data:
            temp = head1
            head1 = head1.next
        else:
            temp = head2
            head2 = head2.next

        mergedTail.next = temp
        mergedTail = temp

    if head1 != None:
        mergedTail.next = head1
    elif head2 != None:
        mergedTail.next = head2

    return mergedHead


head1 = Node(10)
head1.next = Node(20)
head1.next.next = Node(30)
head2 = Node(11)
head2.next = Node(19)
head2.next.next = Node(45)
new_head = merge_sorted(head1,head2)

printList(new_head)
