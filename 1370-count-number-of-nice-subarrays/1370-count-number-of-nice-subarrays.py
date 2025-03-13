class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        odds = []
        for i, num in enumerate(nums):
            if num % 2: 
                odds.append(i)
        
        if len(odds) < k:
            return 0
        
        ans = 0
        for i in range(len(odds) - k + 1):
            left = odds[i] - odds[i - 1] if i > 0 else odds[i] + 1  
            right = odds[i + k] - odds[i + k - 1] if i + k < len(odds) else len(nums) - odds[i + k - 1] 
            
            ans += left * right 
        
        return ans
