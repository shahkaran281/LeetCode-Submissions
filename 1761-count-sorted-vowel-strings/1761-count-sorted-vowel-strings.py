class Solution:
    def countVowelStrings(self, n: int) -> int:
        dp = [[0] * (5) for _ in range(n+1)]
        currSum = 0
        dp[1] = [1] * (5)
        for i in range(2,n+1):
            currSum = sum(dp[i-1])
            for j in range(5):
                dp[i][j] = currSum
                currSum -= dp[i-1][j]
        return sum(dp[-1])
        