class Solution:

    def __init__(self, w: List[int]):
        self.prob = []
        self.summ = 0
        for x in w:
            self.summ += x
            self.prob.append(self.summ) 

    def pickIndex(self) -> int:
        target = random.randint(1, self.summ)
        low, high = 0, len(self.prob) - 1
        while low < high:
            mid = (low + high) // 2
            if target > self.prob[mid]:
                low = mid + 1
            else:
                high = mid
        return low

        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()