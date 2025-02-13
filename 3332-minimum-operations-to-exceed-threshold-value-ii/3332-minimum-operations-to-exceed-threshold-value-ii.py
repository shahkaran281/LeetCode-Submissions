from heapq import heapify,heappop, heappush

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapify(nums)
        count = 0
        while len(nums) > 1 and nums[0] < k:
            first,second = heappop(nums), heappop(nums)
            heappush(nums,min(first,second) * 2 + max(first,second))
            count+=1
        return count 