class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        def isPam(start,end):
            if start < 0 or end >= len(s):
                return 0
            if s[start] != s[end]:
                return 0
            return 1 + isPam(start-1,end+1)
        for i in range(len(s)):
            count += isPam(i,i) + isPam(i,i+1)
        
        return count
        