n = int(input("Enter number of semesters: "))

for i in range(n):
    sub = int(input("Enter number of subjects in semester: "))
    max_mark = 0
    for j in range(sub):
        mark = int(input("Enter marks: "))
        if mark < 0 or mark > 100:
            print("You have entered invalid mark.")
            break
        if mark > max_mark:
            max_mark = mark
    else:
        print("Maximum mark in", i+1, "semester:", max_mark)