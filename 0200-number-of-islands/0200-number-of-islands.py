class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dirs = ((0,1),(0,-1),(1,0),(-1,0))
        def bfs(i,j):
            if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == "1":
                grid[i][j] = "-1"
                for dx, dy in dirs:
                    x = i + dx
                    y = j + dy
                    bfs(x,y)
        
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    ans+=1
                    bfs(i,j)
        return ans