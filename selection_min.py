def selection_sort(arr):
    for i in range(len(arr) - 1):
        min=arr[i]
        loc=0
        for j in range(i+1,(len(arr))):
            if min>arr[j]:
                min=arr[j]
                loc=j
                temp=arr[i]
                arr[i]=arr[loc]
                arr[loc]=temp

if __name__ == '__main__':
    arr = [6, 23, 2, 4, 1, 8, 56, 3]
    selection_sort(arr)
    print(*arr)



