class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = 0
        for i in range(len(nums)):
            idx = bisect_left(nums[:n+1],nums[i])
            nums[idx] = nums[i]
            n = max(idx,n)
        return n+1
        