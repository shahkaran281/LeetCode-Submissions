class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        @cache
        def fun(i,j):
            if i == len(text1) or j == len(text2):
                return 0
            elif text1[i] == text2[j]:
                return 1 + fun(i+1,j+1)
            else:
                return max(fun(i,j+1),fun(i+1,j))

        return fun(0,0)
