class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        curr = sum(nums[:k]) 
        ans =  curr / k
        for i in range(k,len(nums)):
            curr += nums[i]
            curr -= nums[i-k]
            ans = max(ans,curr / k) 
        return ans
