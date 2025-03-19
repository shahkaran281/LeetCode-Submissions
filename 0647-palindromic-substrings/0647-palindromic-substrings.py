class Solution:
    def countSubstrings(self, s: str) -> int:
        def fun(i,j):
            if i < 0 or j == len(s):
                return 0
            if s[i] != s[j]:
                return 0
            return 1 + fun(i-1,j+1)
        count = 0
        for i in range(len(s)):
            count += fun(i,i) + fun(i,i+1)
        return count