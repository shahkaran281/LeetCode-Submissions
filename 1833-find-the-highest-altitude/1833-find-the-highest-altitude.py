class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        ans = 0
        curr = 0
        for x in gain:
            curr += x
            ans = max(ans,curr)
        return ans