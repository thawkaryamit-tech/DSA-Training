# delete elements in array.......... 

arr=[]
n=int(input("enter size :"))
for i in range(n):
    arr.append(int(input("enter numbers :")))
loc=int(input("enter location :"))

for i in range(loc+1,len(arr)):
    arr[i-1]=arr[i]
arr.pop()
print(arr)
