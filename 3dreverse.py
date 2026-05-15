n = int(input("enter number"))

n1 = n % 10
n = n // 10
n2 = n % 10
n = n // 10
n3 = n % 10

res = n1*100 + n2*10 + n3*1
print("result is:", res) 
