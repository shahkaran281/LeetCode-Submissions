from heapq import heappush, heappop
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        minHeap = []
        for i in range(len(matrix)):
            heappush(minHeap,(matrix[i][0],i,0))
        for _ in range(k-1):
            val, r, c = heappop(minHeap)
            if c + 1 < len(matrix[0]):
                heappush(minHeap, (matrix[r][c + 1], r, c + 1))

        return heappop(minHeap)[0]