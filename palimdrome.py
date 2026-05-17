s="A man , a plan, a canal : Panama"
str="" 

for i in s:
    if i.isalpha():
        str += i.lower()
print(str)

rev=''
for i in s:
    rev=i+rev

if str==rev:
    print("palimdrome")
else:
    print("not palimdrome")