print("/n --percentage-- ")
rec={}
num= int(input("Enter number of students: "))
for i in range(num):
    name=input("Enter name: ")
    per=float(input("Enter percentage: "))
    rec[name]=per
print(rec)
