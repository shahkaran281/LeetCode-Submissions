class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        count = Counter(nums)
        # print(count)
        ans = 0
        for x, freq in count.items():
            if x - k in count:
                if k > 0:
                    ans += 1
                elif k == 0 and freq > 1:
                    ans += 1
            
        return ans
        