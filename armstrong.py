num = int(input("enter number"))

sum = 0
save = num

count = 0
num = save

while num > 0:
    num = num // 10
    count = count + 1
num = save
while num > 0 :
    rem = num % 10
    sum = sum + (rem ** count)
    num = num // 10

if sum == save:
    print("armstrong")
else:
    print("not armstrong") 
    