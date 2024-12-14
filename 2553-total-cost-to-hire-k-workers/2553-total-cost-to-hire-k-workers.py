from heapq import heappop, heappush
class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        ans = 0
        i = 0
        n = len(costs)
        j = n - 1
        heap = []
        while i < n and i < candidates:
            heappush(heap,(costs[i],i))
            i+=1
        while j >= i and (n-j-1) < candidates:
            heappush(heap,(costs[j],j))
            j-=1
        while k > 0:
            val, index = heappop(heap)
            ans += val
            k-=1
            if i > j:
                continue
            elif index < i:
                heappush(heap,(costs[i],i))
                i+=1
            else:
                heappush(heap,(costs[j],j))
                j-=1
        return ans

