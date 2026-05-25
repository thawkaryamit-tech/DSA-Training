import sys

class GetNode:
    def __init__(self) -> None:
        self.data=None
        self.link=None

class stack_LinkedList:
    def __init__(self) -> None:
        self.head=None
        self.top=None

    def push(self):
        data=int(input("enter data :"))
        newNode=GetNode()
        newNode.data =data # type: ignore
        if self.top==None:
            self.top=newNode
        else:
            newNode.link=self.top # type: ignore
            self.top=newNode
            print(data,"is pushed..")

    def traverse(self):
        if self.top==None:
            print("stack not present")
        else:
            ptr=self.top
            while ptr!=None:
                print(ptr.data,"->",end=" ")
                ptr=ptr.link

    def pop(self):
        if self.top==None:
            print("stack underflow")

        else:
            temp=self.top
            print(temp.data,"is popped....")
            self.top=self.top.link
            temp.link=None

    def peek(self):
        if self.top is None:
            print("Stack is empty")
        else:
            print("Top element :", self.top.data)

if __name__ == '__main__':
    obj=stack_LinkedList()
    while True:
        print("")
        print("1. push")
        print("2. Traverse")
        print("3. pop")
        print("4. peek")
        print("0. Exit")

        n=int(input("Selet any choice: "))
        if n==1:
            obj.push()
        elif n==2:
            obj.traverse()
        elif n==3:
            obj.pop()
        elif n==4:
            obj.peek()
        elif n==0:
            sys.exit(0)
