class Solution:
    def convert(self, s: str, numRows: int) -> str:
        k = 0
        res = ["" for i in range(numRows)]
        while k < len(s):
            i = 0
            while i < numRows and k < len(s):
                res[i] += str(s[k])
                i += 1
                k += 1
            i = numRows - 2
            while i > 0 and k < len(s):
                res[i] += str(s[k])
                i -= 1
                k += 1
        ans = ""
        for i in res:
            ans += i
        return ans
        