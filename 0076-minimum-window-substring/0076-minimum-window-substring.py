class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        tCounter = Counter(t)
        window = {}
        have, need = 0, len(tCounter)
        res, resLen = [-1, -1], float("inf")
        left = 0

        for right, ch in enumerate(s):
            window[ch] = window.get(ch, 0) + 1

            if ch in tCounter and window[ch] == tCounter[ch]:
                have += 1

            while have == need:
                if (right - left + 1) < resLen:
                    res = [left, right]
                    resLen = right - left + 1

                window[s[left]] -= 1
                if s[left] in tCounter and window[s[left]] < tCounter[s[left]]:
                    have -= 1
                left += 1

        l, r = res
        return s[l:r+1] if resLen != float("inf") else ""
