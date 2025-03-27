class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        dirs = ((0,1),(0,-1),(1,0),(-1,0))
        @cache
        def fun(i,j,prev):
            if i < 0 or i == len(matrix) or j < 0 or j == len(matrix[0]) or matrix[i][j] >= prev:
                return 0
            curr = matrix[i][j]
            matrix[i][j] = float('inf')
            ans = 1
            for dx, dy in dirs:
                x = i + dx
                y = j + dy
                ans = max(ans, 1 + fun(x,y,curr))
            matrix[i][j] = curr
            return ans
        # print(fun(0,0,prev))
        ans = 1
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                ans = max(ans,fun(i,j,float('inf')))
        return ans
                
            
                    