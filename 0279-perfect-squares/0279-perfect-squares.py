class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float('inf')] * (n+1)
        sqr = []
        dp[0] = 0
        i = 1
        while i*i <= n:
            sqr.append(i*i)
            dp[i*i] = 1
            i+=1
        for j in range(1, n + 1):
            for i in sqr:
                if i <= j:
                    dp[j] = min(dp[j], dp[j - i] + 1)
        print(dp)
        if dp[-1] == float('inf'):
            return n
        else:
            return dp[-1] 
        