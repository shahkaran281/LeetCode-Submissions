import bisect

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        for i in range(len(spells)):
            val = success / spells[i]
            spells[i] = len(potions) - bisect_left(potions, val)
        return spells