arr = [[11,22,33],22,[4,5]]
print(arr)
for a in range(len(arr)):
    print(arr[a])

print("**********************************")

ls=[1,2,3],[4,5,6],[7,8,9]
print(ls)
for x in range(len(ls)):
    print(ls[x])

print("**********************************")

for i in range(len(ls)):
    for j in range(len(ls[i])):
        print(ls[i][j],end=" ")
    print()