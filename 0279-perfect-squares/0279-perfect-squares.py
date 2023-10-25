class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float('inf')] * (n+1)
        sqr = []
        dp[0] = 0
        i = 1
        while i*i <= n:
            sqr.append(i*i)
            i+=1
        for j in range(1, n + 1):
            for i in sqr:
                if i <= j:
                    dp[j] = min(dp[j], dp[j - i] + 1)
        return dp[-1] 
        