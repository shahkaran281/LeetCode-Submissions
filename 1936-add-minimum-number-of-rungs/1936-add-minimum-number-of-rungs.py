class Solution:
    def addRungs(self, rungs: List[int], dist: int) -> int:
        rungs.insert(0,0)
        count = 0
        for i in range(1,len(rungs)):
            count += ceil((rungs[i] - rungs[i-1])/dist)-1
        return count
        