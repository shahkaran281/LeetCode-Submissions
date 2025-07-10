from heapq import heappush, heappop
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        topK = []
        for val, freq in counter.items():
            heappush(topK,(freq,val))
            if len(topK) > k:
                heappop(topK)
        ans = []
        while topK:
            ans.append(heappop(topK)[1])
        return ans
