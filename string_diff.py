s="ycce"
t="ycsce"
count=0

if len(s)<len(t):
    print(len(t)-len(s))
elif len(t)<len(s):
    print(len(s)-len(t))
elif len(s)==len(t):
    for i in range(len(s)):
        if s[i]!=t[i]:
            count=count+1
    print(count)
