from heapq import heapify, heappush, heappop 

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        counter = collections.Counter(arr)
        heap = [] 
        heapify(heap)
        for key, count in counter.items():
            heappush(heap, count) 
        i = 0
        heap.sort()
        while i < len(heap) and k > 0:
            k -= heap[i]
            i+=1
        if k < 0:
            i-=1
        return len(heap) - i