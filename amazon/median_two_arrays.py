def findMedianSortedArrays(nums1,nums2):
    nums_new = sorted(nums1 + nums2)

    mid = int(len(nums_new) / 2)
    if (len(nums_new) % 2 == 0):
        return ((nums_new[mid-1] + nums_new[mid])/ 2)
    else:
        return nums_new[mid]

def lognm_approach(arr1,n , arr2,m):
    i =0
    


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
def anotheroptimized(nums1,nums2):
    new_arr =[]
    i =0
    j = 0
    while(i<len(nums1) and j<len(nums2)):
        if(nums1[i]<=nums2[j] ):
            new_arr.append(nums1[i])
            i +=1
        elif(nums2[j]<=nums1[i]):
            new_arr.append(nums2[j])
            j += 1
    diff = len(nums1)+ len(nums2) - len(new_arr)

    if diff == 0:
        media = median(new_arr)
    else:
        if len(nums1)>len(nums2):
            for i in range(len(nums1)-diff,len(nums1),1):
                new_arr.append(nums1[i])

        else:
            for i in range(len(nums2)-diff,len(nums2),1):
                new_arr.append(nums2[i])
        media = median(new_arr)
    return media
if __name__ == "__main__":
    nums1 = [1, 3, 5,7,8]
    nums2 = [2,4,6,8]
    #print(findMedianSortedArrays(nums1, nums2))
    #print(lognm_approach(nums1,len(nums1), nums2,len(nums2)))
    #print(anotheroptimized(nums1, nums2))
    x = "aaaakjlhaa"
    y = "aa"
    res = [i for i in range(len(x)) if x.startswith(y, i)]
    print(len(res))
