class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        res = 0
        for i in range(len(nums)):
            nums[i] = nums[i] % 2 + res
            res = nums[i]
        res = 0
        count = collections.Counter({0:1})
        for i in range(len(nums)):
            if (nums[i] - k) in count:
                res += count[nums[i]-k]
            count[nums[i]] +=1
        return res

