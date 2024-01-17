class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = collections.Counter(arr)
        freq = set()
        for val in count:
            if count[val] in freq:
                return False
            else:
                freq.add(count[val])
        return True
        