class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        count = Counter(word)
        freq = sorted(count.values())
        total = sum(freq)
        ans = float('inf')
        prefix = 0

        for low in range(len(freq)):
            high = low
            curr = freq[high]
            while high + 1 < len(freq) and freq[high + 1] - freq[low] <= k:
                high += 1
                curr += freq[high]
            num_right = len(freq) - (high + 1)
            over_limit = total - (prefix + curr)
            remove = over_limit - num_right * (freq[low] + k)

            ans = min(ans, prefix + remove)
            prefix += freq[low]

        return ans
