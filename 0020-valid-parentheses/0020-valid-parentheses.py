class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        close = {")":"(","}":"{","]":"["}
        start = {"(","{","["}
        stk = []
        for val in s:
            if val in start:
                stk.append(val)
            else:
                if not stk or stk[-1] != close[val]:
                        return False
                else:
                        stk.pop()
        return len(stk) == 0
        