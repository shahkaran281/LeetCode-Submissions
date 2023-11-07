class Solution:
    def minSteps(self, n: int) -> int:
        dp = [float('inf')] * (n+1)
        dp[0] = 0
        dp[1] = 0
        for i in range(2,n+1):
            dp[i] = min(dp[i],i)
            curr = dp[i]+2
            for j in range(2*i,n+1,i):
                dp[j] = min(dp[j],curr)
                curr+=1
        return dp[n]
        