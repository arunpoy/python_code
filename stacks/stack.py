import math
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class MyStack:
    def __init__(self):
        self.head = None
        self.sz = 0

    def push(self,data):
        tmp = Node(data)
        tmp.next = self.head
        self.head=tmp
        self.sz = self.sz+1

    def peek(self):
        if self.head == None:
            return math.inf
        return self.head.data

    def pop(self):
        if self.head == None:
            return math.inf
        res = self.head.data
        self.head= self.head.next
        self.sz = self.sz - 1
        return res

    def size(self):
        return self.sz

    def printStack(self):
        curr = self.head
        while curr:
            print(curr.data, end = " ")
            curr = curr.next
        print()

# driver code

s = MyStack()
s.push(10)
s.push(20)
s.push(30)
print(s.size())
s.printStack()
s.pop()
print(s.peek())
s.printStack()
print(s.size())










