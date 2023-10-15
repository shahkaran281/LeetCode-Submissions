class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        res = 0
        curr = 0
        n = len(arr)
        if n == 1:
            return n
        for i in range(n-1):
            if i % 2 == 1:
                if arr[i] > arr[i+1]:
                    curr+=1
                    res = max(res, curr)
                else:
                    curr = 0
            else:
                if arr[i] < arr[i+1]:
                    curr+=1
                    res = max(curr, res)
                else:
                    curr = 0
        print()
        curr = 0
        for i in range(n-1):
            if i % 2 == 1:
                if arr[i] < arr[i+1]:
                    curr+=1
                    res = max(res, curr)
                else:
                    curr = 0
            else:
                if arr[i] > arr[i+1]:
                    curr+=1
                    res = max(curr, res)
                else:
                    curr = 0
        return res+1
         
        
        