class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        # if 0, then -1, if 1 then +1
        counter = {0:-1}
        ans = 0
        curr = 0
        for i,val in enumerate(nums):
            if val == 1:
                curr += 1
            else:
                curr -=1
            if curr not in counter:
                counter[curr] = i
            else:
                ans = max(ans, i- counter[curr])
        
        return ans