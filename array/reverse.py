def rverseArray(arr, start, end):
    while (start < end):
        temp = arr[start]
        arr[start] = arr[end]
        arr[end] = temp
        start += 1
        end = end - 1

arr = [2,3,4,5,6]
start =0
end = len(arr)-1
rverseArray(arr,start,end)
print(arr)