class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res = [-1,-1]
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = int((low + high)/2)
            if nums[mid] == target and (mid == 0 or nums[mid-1] < target):
                res[0] = mid
                break
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        if res[0] < 0:
            return res
        else:
            if res[0] == len(nums)-1 or nums[res[0]+1] != target:
                res[1] = res[0]
                return res
            else:
                low = res[0] +1
                high = len(nums) - 1
                while low <= high:
                    mid = int((low+high)/2)
                    if nums[mid] == target and (mid == len(nums)-1 or nums[mid+1] > target):
                        res[1] = mid
                        break
                    elif nums[mid]  > target:
                        high = mid - 1
                    else:
                        low = mid + 1
                if res[1] == -1:
                    res[1] = res[0]
                return res
