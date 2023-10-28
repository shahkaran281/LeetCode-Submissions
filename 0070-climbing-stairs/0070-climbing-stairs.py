class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            DP = [0] * (n+1)
            DP[1] = 1
            DP[2] = 2
            for i in range(3,n+1):
                DP[i] = DP[i-1]+DP[i-2]
            return DP[-1]
        