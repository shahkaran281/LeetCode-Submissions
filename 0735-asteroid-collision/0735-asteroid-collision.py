class Solution:
    def asteroidCollision(self, a: List[int]) -> List[int]:
        stk = []

        def fun(val):
            while len(stk) != 0 and stk[-1]*val < 0:
                if abs(stk[-1]) > abs(val):
                    return
                elif abs(stk[-1] == abs(val)):
                    stk.pop()
                    return
                else:
                    stk.pop()
            stk.append(val)
        i = 0
        while i < len(a):
            if len(stk) == 0:
                stk.append(a[i])
            else:
                if stk[-1]*a[i] > 0:
                    stk.append(a[i])
                else:
                    if stk[-1] < 0:
                        stk.append(a[i])
                    else:
                        fun(a[i])
            i += 1
        return stk
        