class Solution:
    def isHappy(self, n: int) -> bool:
        def fun(x):
            summ = 0
            while x:
                summ += (x%10) **2
                x = x // 10
            return summ
        
        visited = set()
        
        while n not in visited:
            visited.add(n)
            n = fun(n)
            if n == 1:
                return True

        return False

        # 1 -> True
        # 2 -> 4 -> 16 -> 37 -> 58 -> 89 -> 