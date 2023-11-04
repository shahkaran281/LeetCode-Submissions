class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        i , j = 0,0
        currProd = 1
        count = 0
        while j < len(nums):
            currProd *= nums[j]
            while currProd >= k and i<=j:
                currProd /= nums[i]
                i+=1
            # print(j-i+1, f'i: {i} j: {j}, currProd: {currProd}')
            if currProd <= k:
                count += j - i +1 
            j+=1
        return count
        