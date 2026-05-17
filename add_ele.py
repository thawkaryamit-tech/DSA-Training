#insert elements in array.......... 
arr=[]
n=int(input("enter size :"))
for i in range(n):
    arr.append(int(input("enter numbers :")))
key=int(input("enter key element whice is to be inserted :"))
loc=int(input("enter location :"))

arr.append(0)
for i in range(len(arr)-1,loc,-1):
    arr[i]=arr[i-1]

arr[loc]=key
print(arr)
