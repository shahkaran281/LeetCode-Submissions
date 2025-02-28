class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        pos = dict()
        for i,val in enumerate(arr):
            pos[val] = i
        ans = 2
        for i in range(len(arr)-1):
            for j in range(len(arr)-1,i,-1):
                count = 2
                first = arr[i]
                second = arr[j]
                while first + second in pos:
                    count+=1
                    next = first + second
                    first = second 
                    second = next
                    
                ans = max(ans,count) 
            # print(i,dp)
        return ans if ans != 2 else 0