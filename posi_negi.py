arr=[-1,-2,-3,4,5,-6]
res=[]
posi=[]
negi=[]


for i in arr:
    if i>0:
        posi.append(i)
    else:
        negi.append(i)

for i in range(min(len(posi), len(negi))):
    res.append(negi[i])
    res.append(posi[i])
for i in range(min(len(posi), len(negi)), len(negi)):
    res.append(negi[i])
for i in range(min(len(posi), len(negi)), len(posi)):
    res.append(posi[i])

print(res)