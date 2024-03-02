class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # Using Binary Search
        # 1. Find the pivot -> first non-negative

        pivot = -1
        if nums[0] >= 0:
            pivot = 0
        elif nums[-1] < 0:
            pivot = len(nums)
        else:
            l, r = 0, len(nums) - 1
            while l <= r:
                mid = int((l+r)/2)
                if nums[mid]>=0 and (mid==0 or nums[mid-1]<0):
                    pivot = mid
                    break
                elif nums[mid]< 0:
                    l = mid+1
                else:
                    r = mid-1
        l = pivot-1
        r = pivot
        res = [0] * len(nums)
        i = 0
        while l >= 0 and r < len(nums):
            if abs(nums[l]) <= abs(nums[r]):
                val = nums[l]*nums[l]
                res[i] = val
                i+=1
                l-=1
            else:
                val = nums[r]*nums[r]
                res[i] = val
                i+=1
                r+=1
        while l >= 0:
            val = nums[l]*nums[l]
            res[i] = val
            i+=1
            l-=1
        while r < len(nums):
            val = nums[r]*nums[r]
            res[i] = val
            i+=1
            r+=1 

        return res 
        