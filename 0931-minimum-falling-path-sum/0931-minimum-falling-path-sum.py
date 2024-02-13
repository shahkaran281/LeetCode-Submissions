class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        def isWithin(i,j):
            return i>= 0 and i < len(matrix) and j>=0 and j < len(matrix)
        for i in range(1,len(matrix)):
            for j in range(len(matrix)):
                value = matrix[i][j]
                curr = float('inf')
                for k in range(-1,2):
                    if isWithin(i-1,j+k):
                        curr = min(curr,matrix[i-1][j+k]) 
                matrix[i][j] = curr + value
        res = float('inf')
        for i in range(len(matrix)):
            res = min(res, matrix[-1][i])
        return res