class Solution:
    def maximumSwap(self, num: int) -> int:
        ans = num
        i = 1
        while i <= num:
            j = i * 10
            while j <= num:
                # print(i,j)
                n = (num % (i*10)) //i
                m = (num % (j*10)) //j
                new = num - (n*i + m*j) + (m*i+n*j)
                j *= 10
                # print(new)
                ans = max(ans,new)
            i = i * 10
        return ans
