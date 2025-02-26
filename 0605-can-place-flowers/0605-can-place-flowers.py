class Solution:
    def canPlaceFlowers(self, nums: List[int], n: int) -> bool:
        count = 0
        i = 0
        while i < len(nums) and n > 0:
            if nums[i] == 0 and ((i == 0) or (nums[i-1] == 0)) and ((i == len(nums)-1) or nums[i+1]== 0):
                count+=1
            else:
                n -= ((count+1) // 2)
                count = 0
            i += 1
        n -= (count+1) // 2
        return n <= 0