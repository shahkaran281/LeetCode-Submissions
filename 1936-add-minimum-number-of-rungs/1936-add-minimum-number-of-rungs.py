class Solution:
    def addRungs(self, rungs: List[int], dist: int) -> int:
        last = 0
        count = 0
        for i in range(len(rungs)):
            count += ceil((rungs[i] - last)/dist)-1
            last = rungs[i]
        return count
        