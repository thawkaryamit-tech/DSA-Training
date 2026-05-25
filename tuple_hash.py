class Tuple_HashTable:
    def __init__(self,size):
        self.size=size
        self.table=[[] for _ in range(size)]

    def hash_fuction(self,key):
        return key%self.size

    def insert(self,key,value):
        index=self.hash_fuction(key)
        self.table[index].append((key,value))

    def search(self,key):
        index=self.hash_fuction(key)
        for k,v in self.table[index]:
            if k==key:
                return v
        return "not found"
    
    def delete(self,key):
        index=self.hash_fuction(key)
        for i,(k,v) in enumerate(self.table[index]):
            if k==key:
                del self.table[index][i]
                return
            
    def display(self):
         print(self.table)

h=Tuple_HashTable(10)
h.insert(1,"ashish")
h.insert(11,"rahul")
print(h.search(11))
h.display()
h.delete(11)
h.display()
