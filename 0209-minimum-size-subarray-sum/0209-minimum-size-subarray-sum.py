class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = 10000001
        i = 0
        j = 0
        n = len(nums)
        currSum = 0
        while j < n:
            while j < n and currSum < target:
                currSum+= nums[j]
                j+=1
            if j < n:
                res = min(res,j-i)
            while i<=j and currSum>= target:
                currSum-= nums[i]
                res = min(res,j-i)
                i+=1
        return res if res != 10000001 else 0
        