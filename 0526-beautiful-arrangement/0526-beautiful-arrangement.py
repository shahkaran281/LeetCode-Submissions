class Solution:
    def countArrangement(self, n: int) -> int:
        def dfs(position):
            nonlocal count, n
            if position == n + 1:
                count += 1
                return
            for number in matches[position]:
                if not visited[number]:
                    visited[number] = True
                    dfs(position + 1)
                    visited[number] = False

        count = 0
        visited = [False] * (n + 1)
        matches = defaultdict(list)
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if j % i == 0 or i % j == 0:
                    matches[i].append(j)
        dfs(1)
        return count