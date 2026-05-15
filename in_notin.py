arr = [3,2,3,1,2,4]
ans = []

for i in arr:
    if i not in ans:
        ans.append(i)

print("remove duplicates :",ans)