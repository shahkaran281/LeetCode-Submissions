class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        rowSum = [0] * m
        columnSum = [0] * n
        ans = 0
        for i in range(m):
            for j in range(n):
                rowSum[i] += grid[i][j]
                columnSum[j] += grid[i][j]
                
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (rowSum[i] > 1 or columnSum[j] > 1):
                    ans += 1

        return ans