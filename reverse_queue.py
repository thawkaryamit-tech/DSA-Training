import sys

class Queue:

    def __init__(self):
        self.queue = []
        self.rear = -1
        self.front = 0
        self.CAPACITY = 5

    def isFull(self):
        if self.rear == self.CAPACITY - 1:
            return True
        else:
            return False
    def isEmpty(self):
        if self.rear==-1:
            return True
        else:
            return False

    def insert(self, ele):
        if self.isFull():
            print("Queue is Full")
        else:
            self.rear=self.rear+1
            self.queue.append(ele)
            print("Element is inserted...")

    def delete(self):
        if self.isEmpty():
            print("Queue is empty....")
        else:
            ele=self.queue[self.front]
            for i in range(1,self.rear+1):
                self.queue[i-1]=self.queue[i]
            self.rear-=1
            return ele
        print("Element is deleted..")

    def traverse(self):
        if  self.isEmpty():
            print("Queue is full...")
        else:                
            for i in self.queue:
                print("Traversing Queue Elements. :",i)
        print()

    def peek_front(self):
        if self.isEmpty():
            print("Queue is empty....")
        else:
            print("Front....",self.queue)

    def peek_rear(self):
        if self.isEmpty():
            print("Queue is empty....")
        else:
            print("rear...." ,self.queue[self.rear])

CAPACITY = 5
class Stack:

    def __init__(self):
        self.stack = []
        self.top = -1
        self.CAPACITY = 5
    def isFull(self):
        if self.top == self.CAPACITY - 1:
            return True
        else:
            return False
    def push(self, ele):
        if self.isFull():
            print("Stack is Full....")
        else:
            self.top += 1
            self.stack.append(ele)
            print(ele, "Element is pushed....")
    def traverse(self):
        for i in range(self.top,-1,-1):
            print(self.stack[i])
    def isEmpty(self):
        if self.top == -1:
            return True
        else:
            return False
    def pop(self):
        if self.isEmpty():
            print("Stack is Empty..")
        else:
            ele = self.stack[self.top]
            self.stack.pop()
            self.top -= 1
            return ele
    def peek(self):
        print(self.top)
        

if __name__=='__main__':
    obj1 = Queue()
    obj2 = Stack()
    n=int(input("enter number of elements"))
    for i in range(n):
        ele=int(input("enter elements : "))
        obj1.insert(ele)
    
    for x in range(n):
        ele= obj1.delete()
        obj2.push(ele)
    
    for j in range(n):
        ele=obj2.pop()
        obj1.insert(ele)
    
    obj1.traverse()








