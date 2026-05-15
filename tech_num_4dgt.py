# Tech number

num = int(input("Enter a number: "))
sum = 0


first = num // 100
last = num % 100

sum = first + last
if sum ** 2 == num:
    print("Tech number")
else:
    print("Not a Tech number")
