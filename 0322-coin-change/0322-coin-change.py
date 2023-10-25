class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for j in range(1, amount + 1):
            for i in range(len(coins)):
                if coins[i] <= j:
                    dp[j] = min(dp[j], dp[j - coins[i]] + 1)
        if dp[amount]== float('inf'):
            return -1
        else:
            return dp[amount]
        