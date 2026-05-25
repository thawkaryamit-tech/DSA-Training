import sys

class GetNode:
    def __init__(self) -> None:
        self.data= None 
        self.left= None
        self.right= None

class DoubleLinkedList:
    def __init__(self) -> None:
        self.head=None

    def append(self):
        data=int(input("enter data :"))
        newNode=GetNode()
        newNode.data=data # type: ignore
        if self.head is None:
            self.head=newNode
        else:
            ptr=self.head
            while ptr.right!=None:
                ptr=ptr.right
            ptr.right=newNode # type: ignore
            newNode.left=ptr # type: ignore


    def traverse(self):
        if self.head is None:
            print("list not present")
        else:
            ptr=self.head
            while ptr!=None:
                print(ptr.data,"->",end="")
                ptr=ptr.right
            print("None")

    def AddatBegin(self):
        data = int(input("enter data :"))
        newNode = GetNode()
        newNode.data = data # type: ignore
        if self.head is None:
            self.head = newNode
        else:
            newNode.right = self.head # type: ignore
            self.head.left = newNode # type: ignore
            self.head = newNode

    def AddatEnd(self):
        data = int(input("enter data :"))
        newNode = GetNode()
        newNode.data = data# type: ignore
        if self.head is None:
            self.head = newNode
        else:
            ptr=self.head
            while ptr.right!=None:
                ptr=ptr.right
            ptr.right=newNode# type: ignore
            newNode.left=ptr# type: ignore

    def AddatBetween(self):
        data = int(input("Enter data : "))
        loc = int(input("Enter position : "))
        newNode = GetNode()
        newNode.data = data
        ptr = self.head
        count = 1
        while count<loc-1 and ptr!=None:
            ptr = ptr.right
            count += 1
        if ptr == None:
            print("Position not found")
        else:
            newNode.right = ptr.right
            newNode.left = ptr
            if ptr.right != None:
                ptr.right.left = newNode
            ptr.right = newNode

    def AddatPosition(self):
        data = int(input("Enter data : "))
        loc = int(input("Enter position : "))
        newNode = GetNode()
        newNode.data = data
        if loc == 1:
            newNode.right = self.head
            if self.head != None:
                self.head.left = newNode
            self.head = newNode
        else:
            ptr = self.head
            count = 1
            while count < loc-1 and ptr != None:
                ptr = ptr.right
                count += 1
            if ptr == None:
                print("Position not found")
            else:
                newNode.right = ptr.right
                newNode.left = ptr
                if ptr.right != None:
                    ptr.right.left = newNode
                ptr.right = newNode

    def DeleteatBegin(self):
        if self.head is None:
            print("List not present")
        elif self.head.right is None:
            self.head = None
        else:
            self.head = self.head.right
            self.head.left = None

    def DeleteatEnd(self):
        if self.head is None:
            print("List not present")
        elif self.head.right is None:
            self.head = None
        else:
            ptr = self.head
            while ptr.right != None:
                ptr = ptr.right
            ptr.left.right = None

    def DeleteatBetween(self):
        loc = int(input("Enter position : "))
        if self.head is None:
            print("List not present")
        else:
            ptr = self.head
            count = 1
            while count < loc and ptr != None:
                ptr = ptr.right
                count += 1
            if ptr == None:
                print("Position not found")
            elif ptr.left == None:
                self.head = ptr.right
                if self.head != None:
                    self.head.left = None
            elif ptr.right == None:
                ptr.left.right = None
            else:
                ptr.left.right = ptr.right
                ptr.right.left = ptr.left

    def DeleteatPosition(self):
        loc = int(input("Enter position : "))
        if self.head is None:
            print("List not present")
        elif loc == 1:
            self.head = self.head.right
            if self.head != None:
                self.head.left = None
        else:
            ptr = self.head
            count = 1
            while count < loc and ptr != None:
                ptr = ptr.right
                count += 1
            if ptr == None:
                print("Position not found")
            else:
                if ptr.right != None:
                    ptr.right.left = ptr.left
                if ptr.left != None:
                    ptr.left.right = ptr.right


if __name__ == '__main__':
    obj=DoubleLinkedList()
    while True:
        print("")
        print("1.  Append")
        print("2.  Traverse")
        print("3.  ADD at Begin")
        print("4.  ADD at END")
        print("5.  ADD at between")
        print("6.  ADD at Specific Position")
        print("7.  Delete at Begin")
        print("8.  Delete at End")
        print("9.  Delete at Between")
        print("10. Delete at Specific Position")
        print("0. Exit")

        n=int(input("Selet any choice: "))
        if n==1:
            obj.append()
        elif n==2:
            obj.traverse()
        elif n==3:
            obj.AddatBegin()
        elif n==4:
            obj.AddatEnd()
        elif n==5:
            obj.AddatBetween()
        elif n==6:
            obj.AddatPosition()
        elif n==7:
            obj.DeleteatBegin()
        elif n==8:
            obj.DeleteatEnd()
        elif n==9:
            obj.DeleteatBetween()
        elif n==10:
            obj.DeleteatPosition()
        elif n==0:
            sys.exit(0)
