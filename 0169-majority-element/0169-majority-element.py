class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        curr = nums[0]
        count = 1
        i = 0
        while i < len(nums):
            if nums[i] == curr:
                count+=1
            else:
                count-=1
                if count == 0:
                    curr = nums[i]
                    count = 1
            i+=1
        return curr