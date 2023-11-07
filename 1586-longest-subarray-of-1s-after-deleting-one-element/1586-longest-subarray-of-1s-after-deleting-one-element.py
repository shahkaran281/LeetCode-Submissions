class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        res = 0
        curr = 0
        i = -1
        j = 0
        while j < len(nums):
            if curr <=1:
                if nums[j] == 0:
                    curr +=1
                if curr <= 1:
                    res = max(res, j-i-1)
                j+=1
            else:
                i+=1
                if nums[i] == 0:
                    curr-=1
        return res
        