# Tech number

num = int(input("Enter a number: "))
sum = 0
count=0

while num>0:
    num=num//10
    count+=1
save=num
if count%2==0:
    mid=count//2
    num1=num//(10**mid)
    num2=num%(10**mid)
    sum=num1+num2
if sum**2==save:
    print("Tech number")
else:
    print("Not a Tech number")



