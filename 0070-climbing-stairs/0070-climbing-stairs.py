class Solution:
    def __init__(self):
        self.res = {}
    def func(self,n:int) -> bool:
        if n < 0:
            return False
        if n == 0:
            return True
        if n-1 not in self.res:
            self.res[n-1] = self.func(n-1)
        if n-2 not in self.res:
            self.res[n-2] = self.func(n-2)
        return self.res[n-1] + self.res[n-2]
    def climbStairs(self, n: int) -> int:
        return self.func(n)