def targetsum_set(arr,k):
    s =set()

    return_list = []
    for i in range(len(arr)):
        temp = k - arr[i]
        if temp in s:
            return_list.append((arr[i],k-arr[i]))
        s.add(arr[i])
    
    return return_list
def targetsum_sort(arr,k):
    arr =sorted(arr)
    return_list = []
    l = 0
    r = len(arr)-1
    while(l<r):
        if arr[l]+arr[r] == k:
            return_list.append((arr[l],arr[r]))
            l +=1
            r -=1
        elif arr[l]+arr[r] >k:
            r -=1
        else:
            l +=1

    return return_list
if __name__ == "__main__":
    k =15
    arr =[12,3,4,5,5,7,8,9,7]
    print(targetsum_set(arr,k))
    print(targetsum_sort(arr, k))
