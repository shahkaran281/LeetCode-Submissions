class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        q = deque()
        q.append(0)
        # visited = set()
        remaining = set()
        for i in range(len(rooms)):
            remaining.add(i)
        while q:
            index = q.popleft()
            if index not in remaining:
                continue
            # visited.add(index)
            remaining.remove(index)
            for key in rooms[index]:
                q.append(key)
        return not remaining

