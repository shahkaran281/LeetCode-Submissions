class Solution:
    def minFallingPathSum(self, m: List[List[int]]) -> int:
        n = len(m)

        for i in range(1,n):
            for j in range(n):
                minVal = float('inf')
                for k in range(-1,2):
                    if j+k>=0 and j+k < n:
                        minVal = min(minVal,m[i-1][j+k])
                m[i][j] += minVal
        return min(m[-1])