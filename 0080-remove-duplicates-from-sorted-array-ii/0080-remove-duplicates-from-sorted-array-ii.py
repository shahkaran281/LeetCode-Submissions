class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        for i in range(1,len(nums)):
            if nums[i] != nums[k]:
                k+=1
                nums[k] = nums[i]
            elif k == 0 or nums[k] != nums[k-1]:
                k+=1
                nums[k] = nums[i]
            
        return k+1