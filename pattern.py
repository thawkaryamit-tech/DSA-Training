print("\n -- Pattern 1 --")
for i in range(1,5):
    for j in range(1,5):
        print(i,end=" ")
    print()

print("\n -- Pattern 2 --")
n= 1
for x in range(1,5):
    for y in range(1,5):
        print(n,end="\t")
        n+=1
    print()

print("\n -- Pattern 3 --")
num = 65
for a in range(1,5):
    for b in range(1,5):
        print(chr(num),end="\t")
        num+=1
    print()

print("\n -- Pattern 4 --")
for c in range(1,5):
    for d in range(1,c+1):
        print(c,end=" ")
    print()

print("\n -- Pattern 5 --")
for i in range(4,0,-1):
    for j in range(1,i+1):
        print("*",end=" ")  
    print()


print("\n -- Pattern 6 --")
sp = 0
for i in range(4, 0, -1):
    for x in range(sp):
        print(" ", end="")
    for j in range(1, i + 1):
        print("*", end="")
    print()
    sp = sp + 1