print("Dictionary in Python")
d={}
d[100]="Ashish"
d[200]="Prashant"
d[300]="Sandip"
print(d)
print(d[100])
print(d[200])

print("/n-----")
di={100:"Ashish",200:"Prashant",300:"Sandip"}
del di[200]
print(di)

# clear()
# get()
# keys()

print("/n ----------------------------------- ")
i = {100:"Ashish",200:"Prashant",300:"Sandip"}
print(i.keys())
for k in i.keys():
    print(k)
print(i.values())
for v in i.values():
    print(v)
for k,v in i.items():
    print(k,"\t",v)