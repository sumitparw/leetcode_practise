
def logn_approach(arr1,arr2,n):

    if(n==0):
        return -1
    elif(n==1):
        return ((arr1+arr2)/2)
    elif(n==2):
        x =(max(arr1[0],arr2[0])+min(arr1[1],arr2[1]))/2
        return x
    else:
        m1 = median(arr1)
        m2 = median(arr2)
        if(m1 == m2):
            return m1
        elif m1>m2:
            if n%2 ==0:
                return logn_approach(arr1[:int(n/2)+1],arr2[int(n/2)-1:],int(n/2)+1)
            else:
                return logn_approach(arr1[:int(n / 2)+1], arr2[int(n/2):], int(n / 2)+1)
        else:
            if n%2 ==0:
                return logn_approach(arr1[int(n/2)-1:],arr2[:int(n/2)+1],int(n/2)+1)
            else:
                return logn_approach(arr1[int(n / 2):], arr2[:int(n / 2)+1], int(n / 2)+1)
def median(new_arr):
    media = 0
    mid = 0

    if len(new_arr)%2 == 0:
        mid = int(len(new_arr)/2)
        media = (new_arr[mid-1]+new_arr[mid])/2
    else:
        mid = int(len(new_arr)/2)
        media = new_arr[mid]
    return media

if __name__ == "__main__":
    nums1 = [1, 3, 5,7]
    nums2 = [2,4,6,8]
    n =4

    print(logn_approach(nums1, nums2, n))
