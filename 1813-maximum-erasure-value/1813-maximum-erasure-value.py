class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        res = 0
        i = -1
        j = 0
        curr = set()
        currSum = 0
        while j < len(nums):
            if nums[j] in curr:
                i+=1
                curr.remove(nums[i])
                currSum -= nums[i] 
            else:
                curr.add(nums[j])
                currSum += nums[j]
                res = max(currSum,res)
                j+=1
        return res

        