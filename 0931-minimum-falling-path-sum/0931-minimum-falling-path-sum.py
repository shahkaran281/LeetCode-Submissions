class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        def isWithin(i,j):
            return i>= 0 and i < len(matrix) and j>=0 and j < len(matrix)
        dp = [[0] * len(matrix) for _ in range(len(matrix))]
        dp[0] = matrix[0]
        for i in range(1,len(matrix)):
            for j in range(len(matrix)):
                curr = float('inf')
                for k in range(-1,2):
                    if isWithin(i-1,j+k):
                        curr = min(curr,dp[i-1][j+k]) 
                dp[i][j] = curr + matrix[i][j]
        print(dp)
        return min(dp[-1])