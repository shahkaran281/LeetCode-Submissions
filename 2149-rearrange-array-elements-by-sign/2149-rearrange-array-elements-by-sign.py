class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = [0] * (len(nums) // 2)
        neg = [0] * (len(nums) // 2)
        i = 0
        j = 0
        for num in nums:
            if num > 0:
                pos[i] = num
                i+=1
            else:
                neg[j] = num
                j+=1
        for k in range(len(pos)):
            nums[2*k] = pos[k]
            nums[2*k+1] = neg[k]
        return nums
        