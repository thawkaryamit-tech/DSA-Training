n = int(input("Enter number: "))

count = 0

while n > 0 and count < 3:
    n = n // 10
    count = count + 1

print("Count =", count)