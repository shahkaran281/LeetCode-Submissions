class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def is_counter_subset(subset, superset):
            return Counter(subset) <= Counter(superset)
        tCount = collections.Counter(t)
        curr = collections.Counter()
        i = -1
        j = 0
        res = "*" * (len(s)+1)
        while j <= len(s):
            if  Counter(tCount) <= Counter(curr):
                if j - i -1 < len(res):
                    res = s[i+1:j]
                i+=1
                curr[s[i]] -=1
                if curr[s[i]] == 0:
                    del curr[s[i]]
            else:
                if j >= len(s):
                    break
                curr[s[j]]+=1
                j+=1
        return res if len(res) != len(s)+1 else ""

        