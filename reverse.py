n = int(input("Enter 3 digit number: "))

reverse = (n % 10) * 100 + ((n // 10) % 10) * 10 + (n // 100)

print("Reverse =", reverse)