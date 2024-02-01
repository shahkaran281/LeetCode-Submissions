class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        # print(nums)
        res = []
        curr = []
        index = 0
        while index < len(nums):
            while index < len(nums) and len(curr) < 3:
                # print(f'index: {index} curr : {curr} next: {nums[index]}')
                if len(curr) == 0:
                    curr.append(nums[index])
                    index+=1
                else:
                    if nums[index] - curr[0] <= k:
                        curr.append(nums[index])
                        index+=1
                    else:
                        return []
            if len(curr) == 3:
                res.append(curr) 
                curr = []
            else:
                return []
        return res