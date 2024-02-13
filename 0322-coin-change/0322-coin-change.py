class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # if amount == 0:
        #     return 0
        dp = [math.inf] * (amount+1)
        dp[0] = 0
        for i in range(1,amount+1):
            for coin in coins:
                if (i-coin) >= 0:
                    dp[i] = min(dp[i],dp[i-coin]+1)
        return dp[-1] if dp[-1] != math.inf else -1