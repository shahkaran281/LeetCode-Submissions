from heapq import heapify, heappop, heappush
class Solution:
    def reorganizeString(self, s: str) -> str:
        counter = Counter(s)
        # print(counter)
        res = ''
        prev = ''
        prevCount = 0
        maxHeap = []
        for num, freq in counter.items():
            heappush(maxHeap,(-freq,num))
        # print(maxHeap)
        for i in range(len(s)):
            if not maxHeap:
                return ''
            (currCount, curr) = heappop(maxHeap)
            currCount = - currCount - 1
            # print(curr,currCount)
            res += curr
            if prev != '' and prevCount != 0:
                heappush(maxHeap,(-prevCount,prev))
            prev,prevCount = curr, currCount
            # print(curr,currCount)
        return res