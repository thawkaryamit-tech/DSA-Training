import sys
class BST:
    def __init__(self,key) -> None:
        self.leftChild=None
        self.data=key
        self.rightChild=None


    def insert(self,key):
        if self.data==None:
            self.data=key
            return
        elif self.data==key:
            return
        else:
            if key < self.data:
                if self.leftChild:
                    self.leftChild.insert(key)
                else:
                    self.leftChild=BST(key)
            elif key>self.data:
                if self.rightChild:
                    self.rightChild.insert(key)
                else:
                    self.rightChild=BST(key)


    def preorder(self):
        print(self.data,end="->")
        if self.leftChild:
            self.leftChild.preorder()
        if self.rightChild:
            self.rightChild.preorder()

    def postorder(self):
        if self.leftChild:
            self.leftChild.postorder()
        if self.rightChild:
            self.rightChild.postorder()
        print(self.data, end=" -> ")

    def inorder(self):
        if self.leftChild:
            self.leftChild.inorder()
        print(self.data, end=" -> ")
        if self.rightChild:
            self.rightChild.inorder()

    
if __name__ == "__main__":
    root=BST(None)
    while True:
        print("")
        print("1. Insert")
        print("2. PostOrder")
        print("3. PreOrder")
        print("4. InOrder")
        print("0. Exit")
        n=int(input("selet any choice:"))
        if n==1:
            arr=[36,26,46,21,31,11,24,41,56,51,66]
            for i in range (len(arr)):
                root.insert(arr[i])
        elif n==2:
            root.postorder()
        elif n==3:
            root.preorder()
        elif n==4:
            root.inorder()
        elif n==0:
            sys.exit(0)
            

