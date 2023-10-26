class Solution:
    def minFallingPathSum(self, m: List[List[int]]) -> int:
        def isWithin(i,j):
            return i>=0 and i < len(m) and j>=0 and j < len(m)
        for i in range(1,len(m)):
            for j in range(len(m)):
                minVal = float('inf')
                for k in range(-1,2):
                    if isWithin(i-1,j+k):
                        minVal = min(minVal,m[i-1][j+k])
                m[i][j] += minVal
        return min(m[-1])