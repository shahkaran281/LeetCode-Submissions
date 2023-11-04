class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        i = 0
        currProd = 1
        count = 0
        for j in range(len(nums)):
            currProd *= nums[j]
            while currProd >= k and i<=j:
                currProd /= nums[i]
                i+=1
            count += j - i +1 
        return count
        