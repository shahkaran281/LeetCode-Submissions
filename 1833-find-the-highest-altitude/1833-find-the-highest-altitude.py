class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        curr = 0
        res = 0
        for x in gain:
            curr += x
            res = max(res,curr)
        return res