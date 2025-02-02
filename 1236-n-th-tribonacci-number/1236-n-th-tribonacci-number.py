class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n < 3:
            return 1
        t0 = 0
        t1 = 1
        t2 = 1
        temp = 0
        for i in range(3,n+1):
            temp = t0+t1+t2
            t0 = t1
            t1 = t2
            t2 = temp
        return t2
        