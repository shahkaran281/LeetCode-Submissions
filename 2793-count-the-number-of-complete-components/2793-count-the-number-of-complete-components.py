class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for x,y in edges:
            graph[x].append(y)
            graph[y].append(x)
        # print(graph)
        visited = set()
        group = defaultdict(list)
        edges = Counter()
        count = 0
        for i in range(n):
            if i not in visited:
                q = deque([i])
                # print(q)
                while q:
                    curr = q.popleft()
                    if curr not in visited:
                        group[count].append(curr)
                        edges[count] += 1
                        visited.add(curr)
                        for neighbour in graph[curr]:
                            if neighbour not in visited:
                                q.append(neighbour)
                count +=1
        # print(group)
        # print(edges)
        count = 0
        for grp in group:
            edge_count = 0
            nodes = group[grp]
            for node in nodes:
                edge_count += len([neigh for neigh in graph[node] if neigh in nodes])
            
            edge_count //= 2
            
            if edge_count == len(nodes) * (len(nodes) - 1) // 2:
                count += 1

        return count
