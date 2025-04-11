class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count = 0
        for i in range(low, high + 1):
            word = str(i)
            n = len(word)
            if n % 2 == 0:
                left_half = word[:n//2]
                right_half = word[n//2:]
                if sum(int(ch) for ch in left_half) == sum(int(ch) for ch in right_half):
                    count += 1
        return count
