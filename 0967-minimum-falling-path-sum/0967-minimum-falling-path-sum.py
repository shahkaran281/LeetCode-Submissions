class Solution:
    def minFallingPathSum(self, m: List[List[int]]) -> int:
        n = len(m)
        def isWithin(j):
            return j>=0 and j < n
        for i in range(1,n):
            for j in range(n):
                minVal = float('inf')
                for k in range(-1,2):
                    if isWithin(j+k):
                        minVal = min(minVal,m[i-1][j+k])
                m[i][j] += minVal
        return min(m[-1])