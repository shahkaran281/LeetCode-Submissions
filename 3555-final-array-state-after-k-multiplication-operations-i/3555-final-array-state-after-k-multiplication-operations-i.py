from heapq import heappop, heappush
class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        heap = []
        for i, val in enumerate(nums):
            heappush(heap,(val,i))

        while k:
            val, i = heappop(heap)
            nums[i] = nums[i] * multiplier
            heappush(heap,(val*multiplier,i))
            k-=1
            # print(k)
        return nums