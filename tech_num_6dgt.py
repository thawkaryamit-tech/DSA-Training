# Tech number

num = int(input("Enter a number: "))
sum = 0


num1 = num // 1000
num2 = num % 1000

sum = num1 + num2
if sum ** 2 == num:
    print("Tech number")
else:
    print("Not a Tech number")
