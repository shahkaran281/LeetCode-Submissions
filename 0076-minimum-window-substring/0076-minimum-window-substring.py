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
            # print(f"i:{i} j:{j} curr: {curr} word: {s[i+1:j]}")
            # print(tCount.items())
            # print(curr.items())
            # print(tCount.items() <= curr.items())
            if  is_counter_subset(tCount, curr):
                if len(s[i+1:j]) < len(res):
                    res = s[i+1:j]
                # print('Got one: ',s[i+1:j])
                # if 
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

        