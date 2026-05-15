num = int(input("Enter no:"))
fact = 1
sum = 0
save = num

while num > 0:
    rem = num % 10
    fact = 1
    while rem > 0:
        fact = fact * rem
        rem = rem - 1

    sum = sum + fact
    num = num // 10

if sum == save:
    print("Peterson's number")
else:
    print("Not a Peterson's number")