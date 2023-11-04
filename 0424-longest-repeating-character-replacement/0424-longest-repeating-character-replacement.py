class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 1
        i = 0
        j = 0
        count = collections.Counter()
        while j < len(s):
            count[s[j]] +=1
            while (j-i+1) - count[max(count, key=count.get)] > k:
                count[s[i]]-=1
                i+=1
            res = max(res,j-i+1)
            j+=1
        return res