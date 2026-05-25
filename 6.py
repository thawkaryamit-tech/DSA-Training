import re
str=input("enter any string")
m=re.fullmatch(str,"abcabaabcaa")
if m!=None:
    print("matching is available")
else:
        print("matching is not available")