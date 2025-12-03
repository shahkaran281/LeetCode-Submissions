class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        ans = 0
        curr = set() 

        for right in range(len(s)):
            while s[right] in curr:
                curr.discard(s[left])  
                left += 1
            
            curr.add(s[right])
            ans = max(ans, right - left + 1)
            
        return ans