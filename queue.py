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
                print(i," ")
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

if __name__ == '__main__':
    obj = Queue()

    while True:
        print("\n1. insert")
        print("2. delete")
        print("3. Peek front")
        print("4. peek rear")
        print("5. Traverse")
        print("0. Exit")

        ch = int(input("\nSelect any choice : "))
        if ch == 1:
            ele=int(input("Enter data :"))
            obj.insert(ele)
        elif ch == 2:
            obj.delete()
        elif ch == 3:
            obj.peek_front()
        elif ch == 4:
            obj.peek_rear()
        elif ch == 5:
            obj.traverse()
        elif ch == 0:
            sys.exit(0)
