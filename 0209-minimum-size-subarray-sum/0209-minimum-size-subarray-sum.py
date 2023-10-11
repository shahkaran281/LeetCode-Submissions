class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = 10000001
        i ,j, currSum = 0, 0, 0
        currSum = 0
        while j < len(nums):
            while j < len(nums) and currSum < target:
                currSum+= nums[j]
                j+=1
            if j < len(nums):
                res = min(res,j-i)
            while i<=j and currSum>= target:
                currSum-= nums[i]
                res = min(res,j-i)
                i+=1
        return res if res != 10000001 else 0
        