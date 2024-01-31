class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        res = [0] * len(temp)
        stk = [0]
        
        for i in range(1,len(temp)):
            while stk and temp[i] > temp[stk[-1]]:
                popped = stk.pop()
                res[popped] = i - popped
            stk.append(i)
        return res