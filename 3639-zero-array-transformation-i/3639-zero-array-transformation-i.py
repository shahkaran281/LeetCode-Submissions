class Solution:
    def isZeroArray(self, nums: list[int], queries: list[list[int]]) -> bool:
        line = [0] * (len(nums) + 1)
        curr = 0

        for l, r in queries:
            line[l] += 1
            line[r + 1] -= 1

        for i, num in enumerate(nums):
            curr += line[i]
            if curr < num:
                return False

        return True
