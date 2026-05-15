print("\n -- slicing of strings --")
s="HelloWorld!"
print(s[:5])
print(s[::])
print(s[::2])
print(s[::-1])

print("\n -- finding of strings --")
X = "learning python is very easy from Ashish sir"
print(X.find("python"))
print(X.find("Java"))
print(X.find("r"))
print(X.rfind("r"))

print("\n -- counting of strings --")
s="abcabcabcabcadda"
print(s.count('a'))
print(s.count('ab'))
print(s.count('a',3,10))

print("\n -- replacing of strings --")
b="learning python is very difficult from Ashish sir"
s1=b.replace("difficult","easy")
print(s1)

print("\n -- splitting of strings --")
c="learning python is very difficult from Ashish sir"
ls=c.split()
print(ls)
print(len(ls))
s="22-05-2024"
ls=s.split("-")
print(ls)
s="ww.ashish.com"
ls=s.split(".")
print(ls)

print("\n -- joining of strings --")
l=['Nagpur','Pune','Mumbai','Delhi']
s="#".join(l)
s=" ".join(l)
s="-".join(l)
print(s)

print("\n -- reverse of a string --")
s=input("Enter a string: ")
print(s[::-1])

print()
s="learning python is very easy from Ashish sir"
ls=s.split()
ls.reverse()
s=" ".join(ls)
print(ls)

print("\n -- duplicater remove --")
s="ABCDABBCDABBBCCCDDEEEF"