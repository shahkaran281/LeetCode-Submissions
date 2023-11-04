class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 1
        i = 0
        j = 0
        count = dict()
        while j < len(s):
            if s[j] in count:
                count[s[j]] +=1
            else:
                count[s[j]] = 1
            while (j-i+1) - count[max(count, key=count.get)] > k:
                count[s[i]]-=1
                if count[s[i]] == 0:
                    del count[s[i]]      
                i+=1
            res = max(res,j - i+1)
            print(count)
            # print(f'j: {j} i:{i}')
            j+=1
        return res