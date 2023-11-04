class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 1
        i = 0
        j = 0
        count = collections.Counter()
        maxCount = 0
        while j < len(s):
            count[s[j]] +=1
            maxCount = max(maxCount,count[s[j]])
            while (j-i+1) - maxCount > k:
                count[s[i]]-=1
                i+=1
            res = max(res,j-i+1)
            j+=1
        return res