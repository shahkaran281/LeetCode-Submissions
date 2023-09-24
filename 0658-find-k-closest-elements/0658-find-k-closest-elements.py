class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        currSum = 0
        for i in range(k-1):
            currSum += abs(arr[i] - x)
        minSum = 1000000000000
        start = 0
        for i in range(len(arr)-k+1):
            currSum += abs(arr[i+k-1] - x)
            if abs(currSum) < minSum:
                minSum = abs(currSum)
                start =i
            currSum -= abs(arr[i] - x)
            
        return arr[start:start+k]
