class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        curr = set()
        left = 0
        ans = 0
        for right in range(len(s)):
            while s[right] in curr:
                    curr.remove(s[left])
                    left+=1
            ans = max(ans,right - left + 1)
            curr.add(s[right])
        return ans