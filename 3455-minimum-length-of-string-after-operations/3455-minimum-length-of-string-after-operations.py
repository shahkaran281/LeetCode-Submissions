class Solution:
    def minimumLength(self, s: str) -> int:
        count = Counter(s)
        ans = 0
        for key, freq in count.items():
            if freq % 2 == 1 and freq > 2:
                ans+=1
            elif freq % 2 == 0 and freq >1:
                ans+=2
            else:
                ans+=freq
        return ans