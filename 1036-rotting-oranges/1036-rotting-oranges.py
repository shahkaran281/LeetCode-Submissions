class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        fresh = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.append((i,j))
                elif grid[i][j] == 1:
                    fresh += 1
        if fresh == 0:
            return 0
        # print(q)
        dirs = ((0,1),(1,0),(0,-1),(-1,0))
        count = 0

        while q:
            # print(q)
            for _ in range(len(q)):
                x ,y = q.popleft()
                grid[x][y] = 2
                for dx, dy in dirs:
                    i = x + dx
                    j = y + dy
                    if i >= 0 and i < len(grid) and j >= 0 and j < len(grid[0]) and grid[i][j] == 1:
                        # print(i,j,q)
                        fresh -= 1
                        grid[i][j] = 2
                        q.append((i,j))
            count += 1
        if fresh == 0:
            return count - 1
        else:
            return -1
        