class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        count = collections.Counter()
        res = 0
        currSum = 0
        # for i in range(1,len(nums)):
        #     nums[i] += nums[i-1]
        for i in range(len(nums)):
            currSum += nums[i]
            if currSum == goal:
                res+=1
            if currSum - goal in count:
                res += count[currSum - goal]
            count[currSum] +=1
        return res