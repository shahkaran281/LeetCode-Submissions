class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = [[0]*len(grid[0]) for _ in range(len(grid))]
        curr = 0
        for i in range(len(dp)):
            curr += grid[i][0]
            dp[i][0] = curr
        curr = 0
        for j in range(len(dp[0])):
            curr += grid[0][j]
            dp[0][j] = curr
        for i in range(1,len(dp)):
            for j in range(1,len(dp[0])):
                dp[i][j] = min(dp[i-1][j],dp[i][j-1]) + grid[i][j]
        # print(dp)
        return dp[-1][-1]
        