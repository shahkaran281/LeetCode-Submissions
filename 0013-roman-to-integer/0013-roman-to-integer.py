class Solution:
    def romanToInt(self, s: str) -> int:
        mapping = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        ans = 0
        for i in range(len(s)-1,-1,-1):
            if i + 1 < len(s) and mapping[s[i+1]] > mapping[s[i]]:
                ans -= mapping[s[i]]
            else:
                ans += mapping[s[i]]
            # print(i,s[i], ans)
        return ans