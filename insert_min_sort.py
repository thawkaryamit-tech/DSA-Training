def insert_sort(arr):
    for i in range(1,len(arr)):
        temp=arr[i]
        pos=i

        while temp<arr[pos-1] and pos>0:
            arr[pos]=arr[pos-1]
            pos=pos-1
        arr[pos] = temp


if __name__ == '__main__':
    arr = [6, 23, 2, 4, 1, 8, 56, 3]
    insert_sort(arr)
    print(*arr)
