class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        count = collections.Counter()
        res = 0
        for i in range(1,len(nums)):
            nums[i] += nums[i-1]
        # print(nums)
        # print(count)
        for i in range(len(nums)):
            if nums[i] == goal:
                res+=1
            if nums[i] - goal in count:
                res += count[nums[i] - goal]
            count[nums[i]] +=1
        return res