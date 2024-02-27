class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        for i in range(len(prices)-1):
            j = i+1
            while j < len(prices) and prices[j] > prices[i]:
                j+=1
            if j != len(prices):
                prices[i]-=prices[j]
        return prices
        