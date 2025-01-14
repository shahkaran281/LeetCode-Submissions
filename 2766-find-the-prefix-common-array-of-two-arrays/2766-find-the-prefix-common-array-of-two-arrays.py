class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        first = set()
        second = set()
        res = [0] * len(A)
        for i in range(len(A)):
            first.add(A[i])
            second.add(B[i])
            # print(first.intersection(second))
            res[i] = len(first.intersection(second))
        return res