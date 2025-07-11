class Solution:
    def customSortString(self, order: str, s: str) -> str:
        counter = Counter(s)
        ans = []
        for ch in order:
            ans.append(ch*counter[ch])
            del counter[ch]
        for ch, freq in counter.items():
            ans.append(ch*freq)
        # print(ans)
        return ''.join(ans)