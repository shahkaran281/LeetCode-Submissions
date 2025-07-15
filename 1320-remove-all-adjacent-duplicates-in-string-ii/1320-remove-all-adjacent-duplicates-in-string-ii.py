class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stk = []
        i = 0
        while i < len(s):
            # print(stk)
            if not stk or stk[-1][0] != s[i]:
                stk.append([s[i],1])
                i+=1
            else:
                _,freq = stk.pop()
                freq = (freq+1) % k
                if freq > 0:
                    stk.append([s[i],freq])
                i+=1
        # print(stk)
        return ''.join(ch[0]*ch[1] for ch in stk)