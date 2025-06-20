class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        n = len(s)
        x = y = 0
        ans = 0

        for i in range(n):
            if s[i] == 'N':
                y += 1
            elif s[i] == 'S':
                y -= 1
            elif s[i] == 'E':
                x += 1
            elif s[i] == 'W':
                x -= 1

            dist = abs(x) + abs(y)
            currRemaining = (i+1) - dist
            totalRemaining = len(s) - dist
            ans = max(ans, dist + min(k,totalRemaining),dist + min(currRemaining//2, k) * 2)
        return ans