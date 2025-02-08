class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxPos = 0
        for i,jump in enumerate(nums):
            if i > maxPos:
                return False
            maxPos = max(maxPos, i + jump)
        return maxPos >= len(nums)-1