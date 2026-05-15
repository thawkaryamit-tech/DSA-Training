def linear_search(num,arr,target):
    flag = False
    for i in range(num):
        if target!=arr[i]:
            pass
        else:
            flag  = True
            loc=i
    if flag == True:
        print("successful",)
    else:
        print("unsuccessful")            

if __name__ == '__main__' :
        num = int(input("Enter Size"))
        arr=[]
        for i in range(num):
            arr.append(int(input()))
        target = int(input("Enter target number to be search : "))
        linear_search(num,arr,target)    
