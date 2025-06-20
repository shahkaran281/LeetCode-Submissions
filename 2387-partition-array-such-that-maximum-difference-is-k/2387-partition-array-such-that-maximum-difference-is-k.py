class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        # print(nums)
        ans = 1
        prev = nums[0]
        for x in nums:
            if x - prev > k:
                ans+=1
                prev = x
            
        return ans