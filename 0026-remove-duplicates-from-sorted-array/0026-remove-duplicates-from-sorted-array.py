class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 0
        right = 0
        for right in range(len(nums)):
            if nums[right] != nums[left]:
                left += 1
                nums[left] = nums[right]
        return left+1