class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        res = 0
        curr = 0
        if len(arr) == 1:
            return 1
        for i in range(len(arr)-1):
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
        curr = 0
        for i in range(len(arr)-1):
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
         
        
        