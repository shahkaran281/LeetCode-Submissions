class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        def fun(k):
            count = 0

            for rank in ranks:
                count += int(sqrt(k/rank))
                if count >= cars:
                    return True
            return count >= cars
        ans = float('inf')
        left = 1
        right = max(ranks) * (cars**2)

        while left <= right:
            mid = (left + right) //2
            if fun(mid):
                ans = min(ans,mid)
                right = mid - 1
            else:
                left = mid + 1
        return ans 