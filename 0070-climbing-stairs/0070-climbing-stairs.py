class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 4:
            return n
        dp1 = 1
        dp2 = 2
        for i in range(3,n+1):
            temp = dp1 + dp2
            dp1 = dp2
            dp2 = temp
        return dp2
