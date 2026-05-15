print()
s="learning python is very easy from Ashish sir"
ls=s.split()
ls.reverse()
s=" ".join(ls)
print(s)
print("----------------------------------------------")

a="learning python is very easy from Ashish sir"
ls=a.split()
ans=" "
for x in range (len(ls)):
    ans=ans+ls[x][::-1]+" "
print(ans)
print("----------------------------------------------")

print("\n-- duplicate remove --")
ls = "ABCDABBCDABBBCCCDDEEEF"
ans = ""
for i in ls:
    if i not in ans:
        ans = ans + i
print(ans)
print("----------------------------------------------")

