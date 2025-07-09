class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        i = 0
        while i < len(intervals):
            j =i+1
            while j < len(intervals) and intervals[j][0] <= intervals[i][1]:
                intervals[i][1] = max(intervals[j][1],intervals[i][1])
                j+=1
            res.append(intervals[i])
            i = j
        return res