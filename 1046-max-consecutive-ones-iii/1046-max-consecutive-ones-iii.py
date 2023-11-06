class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        i = -1
        j = 0
        curr = 0
        res = 0
        while j < len(nums):
            if curr <= k:
                if nums[j] == 0:
                    curr+=1
                if curr <= k:
                    res = max(res,j-i)
                j+=1
            else:
                i+=1
                if nums[i] == 0:
                    curr -=1
        return res
        