class Solution:
    def minDifference(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 5:
            return 0
        nums.sort()
        ans = float("inf")
        for l in range(4):
            r = n - 4 + l
            ans = min(ans,nums[r] - nums[l])
        return ans
