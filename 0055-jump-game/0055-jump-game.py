class Solution:
    def canJump(self, nums: List[int]) -> bool:
        pos = 0
        for i,num in enumerate(nums):
            if i > pos:
                return False
            pos = max(pos,i + num)
        
        return True
