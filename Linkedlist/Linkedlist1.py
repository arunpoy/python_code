class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


def printList(head):
    curr = head
    llstr =' '
    while curr != None:
        #llstr += str(curr.data)+'---->'
        llstr += str(curr.data) + ' --> ' if curr.next else str(curr.data)
        curr = curr.next
    print(llstr)

def getLength(head):
    curr = head
    count = 0
    while curr != None:
        #print(count)
        count +=1
        curr = curr.next
    return count

def search(head,x):
    curr = head
    pos = 1
    while curr:
        if curr.data == x:
            return pos
        curr = curr.next
        pos +=1
    return -1



head = Node(10)
head.next = Node(20)
head.next.next = Node(30)

printList(head)
print(getLength(head))

print(search(None,3))
