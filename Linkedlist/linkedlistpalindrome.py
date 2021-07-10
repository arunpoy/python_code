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

def isPalindrome(head):
    arr= []
    while head:
        arr.append(head.data)
        head = head.next

    l = 0
    r = len(arr) -1
    while l <= r:
        if arr[l] != arr[r]:
            return False
        l +=1
        r -=1
    return True


head = Node(10)
head.next = Node(20)
head.next.next = Node(20)
head.next.next.next = Node(20)
printList(head)
print(isPalindrome(head))