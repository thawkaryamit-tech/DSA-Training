import sys

class Stack:

    def __init__(self):
        self.stack = []
        self.top = -1
        self.CAPACITY = 100

    def isFull(self):
        if self.top == self.CAPACITY - 1:
            return True
        else:
            return False

    def push(self, ele):
        if self.isFull():
            print("Stack is Full")
        else:
            self.top += 1
            self.stack.append(ele)
            print(ele, "is pushed")

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
            print("Stack is Empty")
        else:
            ele = self.stack[self.top]
            self.stack.pop()
            self.top -= 1
            return ele

    def peek(self):
        print(self.top)


if __name__ == '__main__':
    obj = Stack()
    arr=[234235,235,235,5]

    # push
    for i in arr:
        obj.push(i)
    # pop
    for i in arr:
        obj.pop()
    print(arr)

