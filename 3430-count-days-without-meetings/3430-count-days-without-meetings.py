class Solution:
    def countDays(self, days: int, nums: List[List[int]]) -> int:
        nums.sort()
        # print(nums)
        i = 0
        j = 0
        ans = nums[i][0] - 1
        while j < len(nums):
            nums[i] = nums[j]
            while j < len(nums) and nums[i][1] >= nums[j][0]:
                nums[i][1] = max(nums[i][1], nums[j][1])
                j += 1
            if i != 0:
                ans += nums[i][0] - nums[i-1][1] - 1
            i += 1
        ans += days - nums[i - 1][1]
        return ans
