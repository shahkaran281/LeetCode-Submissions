class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        graph = defaultdict(set)
        
        for i in range(n):
            for j in range(i + 1, n):
                if isConnected[i][j] == 1:
                    graph[i].add(j)
                    graph[j].add(i)
        
        visited = [False] * n
        province_count = 0
        
        def bfs(node):
            q = deque([node])
            visited[node] = True
            while q:
                current = q.popleft()
                for neighbor in graph[current]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        q.append(neighbor)
        
        for i in range(n):
            if not visited[i]:
                bfs(i)
                province_count += 1
        
        return province_count