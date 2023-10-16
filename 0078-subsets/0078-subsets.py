class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        def fun(i):
            if i == len(nums):
                res.append(subset.copy())
                return
            subset.append(nums[i])
            fun(i+1)
            subset.pop()
            fun(i+1)
            
        fun(0)
        return res