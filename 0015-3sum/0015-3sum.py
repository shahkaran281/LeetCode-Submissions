class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        # print(nums)
        res = []
        for k in range(2,len(nums)):
            if k < len(nums)-1 and nums[k] == nums[k+1]:
                continue
            i = 0
            j = k-1
            while i < j:
                summ = nums[i] + nums[j]
                if summ == -nums[k]:
                    res.append([nums[i],nums[j],nums[k]])
                    i += 1
                    j -= 1
                    while i < j and nums[i] == nums[i-1]:  
                        i += 1
                    while i < j and nums[j] == nums[j+1]:  
                        j -= 1
                elif summ > -nums[k]:
                    j-=1
                else:
                    i+=1
        return res