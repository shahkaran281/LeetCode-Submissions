class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        def fun(l,r):
            if l < 0 or r == len(s):
                return 0
            if s[l] == s[r]:
                return 1+ fun(l-1,r+1)
            else:
                return 0
        for i in range(len(s)):
            res += fun(i,i)
            if i+1 < len(s):
                res+= fun(i,i+1)
        return res
        