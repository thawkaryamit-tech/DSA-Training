# accept values from user find sum of list
num=int(input("enter size: "))
print("enter list elements:")
arr=[]
sum=0

for i in range(num):
    ele=int(input("enter elements:"))
    arr.append(ele)
for i in range(len(arr)):
    sum=sum+arr[i]
print("sum of list is:" ,sum)