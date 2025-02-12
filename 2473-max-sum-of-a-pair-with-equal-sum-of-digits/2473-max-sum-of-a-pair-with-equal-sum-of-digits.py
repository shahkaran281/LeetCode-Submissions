from heapq import heapify, heappop, heappush

class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        def dSum(x):
            curr = 0
            while x:
                curr += x % 10
                x = x // 10
            # print(x,curr)
            return curr
        ans = -1
        digitSum = defaultdict(list)
        for num in nums:
            heappush(digitSum[dSum(num)],-num)
        # print(digitSum)
        for sumList in digitSum.values():
            # print(sumList)
            if len(sumList) > 1:
                ans = max(ans, -heappop(sumList) - heappop(sumList))
        return ans