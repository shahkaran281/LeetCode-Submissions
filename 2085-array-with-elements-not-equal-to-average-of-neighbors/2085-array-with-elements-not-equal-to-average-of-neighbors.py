class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        sortList = sorted(nums)
        low = 0 
        high = len(nums) - 1
        i = 0
        while low <= high:
            nums[i] = sortList[low]
            i+=1
            if i < len(nums):
                nums[i] = sortList[high]
            i+=1
            low+=1
            high-=1
        return nums