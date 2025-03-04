class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        leftSum = 0
        rightSum = 0
        for i in range(1,len(nums)):
            rightSum += nums[i]
        if leftSum == rightSum:
            return 0
        for i in range(1,len(nums)):
            leftSum+= nums[i-1]
            rightSum -= nums[i]
            if leftSum == rightSum:
                return i
        return -1