# Sum od even and  odd numbers

num=int(input("enter size: "))
print("enter list elements:")
arr=[]
even=0
odd=0
e1=0
o1=0

for i in range(num):
    ele=int(input("enter elements:"))
    arr.append(ele)

for i in range(len(arr)):

    if arr[i]%2==0:
        even=even+arr[i]
        e1=e1+1
    else:
        odd=odd+arr[i]
        o1=o1+1
        
print("sum of even numbers is:" ,even)
print("sum of odd numbers is:" ,odd)
print("count of even numbers is:" ,e1)
print("count of odd numbers is:" ,o1)
