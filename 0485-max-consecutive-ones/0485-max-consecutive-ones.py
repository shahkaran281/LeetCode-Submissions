class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        curr = 0
        for i in range(len(nums)):
            if  not nums[i]:
                curr = 0
            else:
                curr+=1
                res = max(res,curr)
        return res
        