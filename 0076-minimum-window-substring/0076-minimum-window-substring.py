class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        tCount = Counter(t)
        count = Counter()
        have = 0
        need = len(t)
        ans = ""
        i = 0
        j = 0
        min_len = float("inf")

        while j < len(s):
            count[s[j]] += 1
            if s[j] in tCount and count[s[j]] <= tCount[s[j]]:
                have += 1

            while have == need:
                if j - i + 1 < min_len:
                    min_len = j - i + 1
                    ans = s[i : j + 1]

                count[s[i]] -= 1
                if s[i] in tCount and count[s[i]] < tCount[s[i]]:
                    have -= 1
                i += 1

            j += 1

        return ans
