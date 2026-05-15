def linear_search(num,arr,target):
    flag = False
    low = 0
    high = num-1
    while low<=high:
        mid=(low+high)//2
        if target==arr[mid]:
             flag = True
             loc= mid
             break;
        elif target<arr[mid]:
            high = mid+1
        elif target<arr[mid]:
            low = mid-1
        
    if flag == True:
        print("successful")
    else:
        print("unsuccessful")            

if __name__ == '__main__' :
        num = int(input("Enter Size"))
        arr=[]
        for i in range(num):
            arr.append(int(input()))
        target = int(input("Enter target number to be search : "))
        linear_search(num,arr,target)    
