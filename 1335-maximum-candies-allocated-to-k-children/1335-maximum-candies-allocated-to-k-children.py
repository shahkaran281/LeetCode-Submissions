class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        def canDistribute(candies, n, k):
            count = 0
            for candy in candies:
                count += candy // n
                if count >= k:
                    return True
            return count >= k
        
        left, right = 1, max(candies)
        ans = 0
        
        while left <= right:
            mid = (left + right) // 2
            if canDistribute(candies, mid, k):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        
        return ans