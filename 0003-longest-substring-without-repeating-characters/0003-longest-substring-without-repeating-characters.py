class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visited = set()
        i = 0 
        j = 0
        res = 0
        while j < len(s):
            if s[j] in visited:
                visited.remove(s[i])
                i+=1
            else:
                visited.add(s[j])
                res = max(res,j-i+1)
                j+=1
        return res
