from typing import List

class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        if right <= 1:
            return [-1, -1]
        
        isPrime = [True] * (right - left + 1)
        
        for i in range(2, int(right**0.5) + 1):
            start = max(i * i, (left + i - 1) // i * i)
            for j in range(start, right + 1, i):
                isPrime[j - left] = False
        primes = []
        for i in range(left, right + 1):
            if i > 1 and isPrime[i - left]:
                primes.append(i)
        
        if len(primes) < 2:
            return [-1, -1]
        
        closest_pair = [-1, -1]
        min_diff = float('inf')
        
        for i in range(1, len(primes)):
            diff = primes[i] - primes[i - 1]
            if diff < min_diff:
                min_diff = diff
                closest_pair = [primes[i - 1], primes[i]]
        
        return closest_pair
