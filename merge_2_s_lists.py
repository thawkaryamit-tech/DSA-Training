l1=[1,3,5]
l2=[2,4,6]
m=[]
i=0
j=0

while i<len(l1) and j<len(l2):
    if l1[i]<l2[j]:
        m.append(l1[i])
        i+=1
    else:
        m.append(l2[j])
        j+=1

while i < len(l1):
    m.append(l1[i])
    i += 1

while j < len(l2):
    m.append(l2[j])
    j += 1

print(m)