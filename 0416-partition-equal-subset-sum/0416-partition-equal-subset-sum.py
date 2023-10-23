class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        totalSum = sum(nums)
        pSums = {0}
        if totalSum % 2 ==1:
            return False
        target = int(totalSum / 2)
        for i  in nums:
            newSums = set()
            for j in pSums:
                newSums.add(j+i)
            pSums.update(newSums)
            if target in pSums:
                return True
        return False

        