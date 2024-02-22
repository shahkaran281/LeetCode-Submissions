class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        largeSum = nums[0]
        tempSum = nums[0]
        for i in range(1,len(nums)):
            tempSum = max(nums[i], tempSum + nums[i])
            largeSum = max(tempSum,largeSum)
        return largeSum