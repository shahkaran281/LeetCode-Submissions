class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        curr = 0
        for i in range(len(nums)):
            nums[i] = nums[i] % 2 + curr
            curr = nums[i]
        # print(nums)
        res = 0
        count = collections.Counter({0:1})
        for num in nums:
            if (num - k) in count:
                res += count[num-k]
            count[num] +=1
        return res

