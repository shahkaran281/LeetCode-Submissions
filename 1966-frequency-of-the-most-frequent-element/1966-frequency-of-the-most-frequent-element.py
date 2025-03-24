class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        curr = 0
        left = 0
        ans = 0

        for right in range(len(nums)):
            target = nums[right]
            curr += target

            # print(right, left, curr)
            while (right - left + 1) * target - curr > k:
                curr -= nums[left]
                left += 1
            ans = max(ans, right - left + 1)

        return ans
