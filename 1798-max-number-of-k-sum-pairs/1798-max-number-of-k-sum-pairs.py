class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        ans = 0
        counter = Counter(nums)
        for val, freq in counter.items():
            if val * 2 == k:
                ans += freq // 2
                freq = freq % 2
            elif k - val in counter:
                pair = min(freq, counter[k - val])
                counter[val] -= pair
                counter[k - val] -= pair
                ans += pair
        return ans