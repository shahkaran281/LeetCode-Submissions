class Solution:
    def searchInsert(self, nums: List[int], x: int,n:int) -> int:

            if x <= nums[0]:
                return 0
            if x > nums[n-1]:
                return n
            l = 0
            r = n-1
            while l <= r:
                mid = int((l+r)/2)
                if nums[mid] == x:
                    return mid
                elif nums[mid] > x:
                    r = mid - 1
                else:
                    l = mid + 1
            if nums[l] > x:
                l-=1
            return l+1
    def lengthOfLIS(self, nums: List[int]) -> int:
        j = 1
        for i in range(1,len(nums)):
            k = self.searchInsert(nums,nums[i],j)
            nums[k] = nums[i]
            if k == j:
                j+=1
        return j



        


        