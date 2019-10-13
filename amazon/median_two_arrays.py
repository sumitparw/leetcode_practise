def findMedianSortedArrays(nums1,nums2):
    nums_new = sorted(nums1 + nums2)
    print(len(nums_new))
    mid = int(len(nums_new) / 2)
    print(mid)
    if (len(nums_new) % 2 == 0):
        return ((nums_new[mid-1] + nums_new[mid])/ 2)
    else:
        return nums_new[mid]


def recursive_median(nums1, nums2, start):
    end = min(len(nums1), len(nums2))
    mid_tot = int((len(nums1) + len(nums2) + 1) / 2)

    mid_x = int((start + end) / 2)
    mid_y = mid_tot - mid_x
    if nums1[mid_x - 1] <= nums2[mid_y] and nums2[mid_y - 1] <= nums1[mid_x]:
        if ((len(nums1) + len(nums2)) % 2 == 0):
            return (max(nums1[mid_x - 1], nums2[mid_y - 1]), min(nums2[mid_y], nums1[mid_x])) / 2
        else:
            return (max(nums1[mid_x - 1], nums2[mid_y - 1]))
    elif nums1[mid_x-1] > nums2[mid_y]:
        start = start - 1
        recursive_median(nums1, nums2, start)
    else:
        start = start + 1
        recursive_median(nums1, nums2, start)




def optimized(nums1, nums2):
    start = 0
    return recursive_median(nums1, nums2, start)

if __name__ == "__main__":
    nums1 = [1, 3]
    nums2 = [2,4,5]
    k = 2
    #print(findMedianSortedArrays(nums1, nums2))
    print(optimized(nums1, nums2))