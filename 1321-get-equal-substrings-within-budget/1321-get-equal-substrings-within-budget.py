class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        cost = [0] * len(s)
        for i in range(len(cost)):
            cost[i] = abs(ord(s[i])-ord(t[i]))
        i = -1
        j = 0
        res = 0
        curr = 0
        while j < len(cost):
            if curr <= maxCost:
                curr+= cost[j]
                if curr <= maxCost:
                    res = max(res,j-i)
                j+=1
            else:
                i+=1
                curr -= cost[i]
        return res
        