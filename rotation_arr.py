arr=[1,2,3,4,5]
k = int(input("enter 1 or 2 :"))
n= len(arr)

for i in range(k):
    temp = arr[n - 1]
    for j in range(n-1,0,-1):
        arr[j]=arr[j-1] 
    arr[0]=temp
print(arr)
    

