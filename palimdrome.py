n = int(input("Enter number: "))
rev = 0
save = n

while n > 0:
    rem = n % 10
    rev = rev * 10 + rem
    n = n // 10

if rev == save:
    print("Palindrome")
else:
    print("Not Palindrome")