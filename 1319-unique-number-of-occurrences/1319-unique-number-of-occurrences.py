class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq = Counter(arr).values()
        visited = set()
        for x in freq:
            if x in visited:
                return False
            visited.add(x)
        return True