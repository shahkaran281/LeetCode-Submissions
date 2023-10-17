class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 2:
            return min(nums[0], nums[1])
        l = 0
        h = n - 1
        while l <= h:
            mid = int((l+h)/2)
            if (mid == 0 or nums[mid-1] > nums[mid]) and (mid == n-1 or nums[mid+1] > nums[mid]):
                return nums[mid]
            elif nums[h] > nums[l] or nums[l] > nums[mid]:
                h = mid - 1
            else:
                l = mid + 1
        return -1
        