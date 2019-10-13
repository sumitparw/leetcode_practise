def distinct(arr,k):
    count =0
    d = {}
    s1 = ''
    s2 = ''
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i]+arr[j]==k:
                s1 =str(arr[i])+','+str(arr[j])
                s2 = str(arr[j]) + ',' + str(arr[i])
                if s1 not in d and s2 not in d:
                    count += 1
            d[s1] =0
            d[s2] = 0
    return count
def optimized(arr,k):

    #arr = sorted(arr)
    n =len (arr)
    m = [0] * 1000

    # Store counts of all elements in map m
    for i in range(0, n):
        m[arr[i]] += 1
    print(m)
    twice_count = 0
    for i in range(0, n):
        if(m[k-arr[i]]>1):
            twice_count += 1
        else:
            twice_count += m[k - arr[i]]

        if (k - arr[i] == arr[i]):
            twice_count -= 1


    # return the half of twice_count
    return int(twice_count / 2)
if __name__ == "__main__":
    arr = [2,5,-51,98,46,1,24,23,46]
    k = 47
    print(distinct(arr,k))
    print(optimized(arr, k))