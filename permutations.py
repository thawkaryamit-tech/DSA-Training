from itertools import permutations

a,b = 459,500
ans=[]

for i in permutations(str(a)):
    num = int("".join(i))
    if num > b:
        ans.append(num)
if len(ans)==0:
    print(-1)
else:
    print(min(ans))