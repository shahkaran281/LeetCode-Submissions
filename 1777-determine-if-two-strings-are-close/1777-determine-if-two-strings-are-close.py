class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        c1 = Counter(word1)
        c2 = Counter(word2)
        freq1 = c1.values()
        freq2 = c2.values()
        return c1.keys() == c2.keys() and sorted(freq1) == sorted(freq2)
        