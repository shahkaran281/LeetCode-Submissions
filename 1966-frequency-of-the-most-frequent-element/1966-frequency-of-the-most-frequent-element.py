class Solution:
    def maxFrequency(self, A: List[int], k: int) -> int:
        A.sort()
        i, j, N, s = 0, 0, len(A), 0
        for j in range(N):
            s += A[j]
            if (j - i + 1) * A[j] - s > k:
                s -= A[i]
                i += 1
        return j - i +1