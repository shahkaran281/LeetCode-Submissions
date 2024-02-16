class Solution:
    def isValid(self, s: str) -> bool:
        close = {")":"(","}":"{","]":"["}
        start = {"(","{","["}
        stk = []
        for val in s:
            if val in start:
                stk.append(val)
            else:
                if stk:
                    if stk[-1] != close[val]:
                        return False
                    else:
                        stk.pop()
                else:
                    return False
        return len(stk) == 0
        