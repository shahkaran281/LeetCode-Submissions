class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stk = []
        i = 0
        j = 0
        for i in range(len(pushed)):
            stk.append(pushed[i])
            while stk and stk[-1] == popped[j]:
                stk.pop()
                j+=1
        return j == len(pushed)