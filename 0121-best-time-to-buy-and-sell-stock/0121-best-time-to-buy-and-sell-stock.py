class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr = 0
        res = 0
        for i in range(1,len(prices)):
            curr = max(curr+prices[i] - prices[i-1],prices[i] - prices[i-1])
            res = max(curr, res)
        return res
