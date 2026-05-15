#accept values from user and print it
num=int(input("enter size: "))
print("enter element :")
arr=[]

for i in range(num):
    ele=int(input("enter elemenets:"))
    arr.append(ele)
for i in range(len(arr)):
    print(arr[i])