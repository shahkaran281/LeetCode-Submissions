class Solution:
    def addDigits(self, n: int) -> int:
        res = 0
        while n:
            res += n%10
            if res >= 10:
                res -= 9
            n = n // 10
        return res
        