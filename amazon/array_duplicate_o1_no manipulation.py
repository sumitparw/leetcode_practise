class Solution:
    def findDuplicate_o_n(self, nums):
        # Find the intersection point of the two runners.
        tortoise = nums[0]
        hare = nums[0]
        while True:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            if tortoise == hare:
                break

        # Find the "entrance" to the cycle.
        ptr1 = nums[0]
        ptr2 = tortoise
        while ptr1 != ptr2:
            ptr1 = nums[ptr1]
            ptr2 = nums[ptr2]

        return ptr1

    def findDuplicate_o_nlgn(self, nums):
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                return nums[i]
        return None

    def findDuplicate_o_n2(self, nums):
        for i in range(0,len(nums)-1,1):
            for j in range(i+1,len(nums),1):
                if nums[i] == nums[j]:
                    return nums[i]
        return None

s = Solution()
nums = [2,3,4,5,2]
print(s.findDuplicate_o_n(nums))
print(s.findDuplicate_o_nlgn(nums))
print(s.findDuplicate_o_n2(nums))