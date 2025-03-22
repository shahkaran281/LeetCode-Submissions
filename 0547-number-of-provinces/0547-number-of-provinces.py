class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        graph = defaultdict(set)
        
        for i in range(n):
            for j in range(i + 1, n):
                if isConnected[i][j] == 1:
                    graph[i].add(j)
                    graph[j].add(i)
        group = set()
        count = 0
        for i in range(n):
            if i not in group:
                count +=1
                q = deque([i])
                # print(q)
                while q:
                    curr = q.popleft()
                    if curr not in group:
                        group.add(curr)
                        for neighbour in graph[curr]:
                            if neighbour not in group:
                                q.append(neighbour)
        
        return count
