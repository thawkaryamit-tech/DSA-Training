price=[100,80,60,70,60,75,85]
n=7
res=[]

for i in range (1,n):
    if price[i]<price[i-1]:
        res.append(1**3)
    else:
        res.append(2**3)
print(res)