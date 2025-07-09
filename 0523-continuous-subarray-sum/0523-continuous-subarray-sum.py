class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        # mod_map = {0: -1}  
        # total = 0

        # for i, num in enumerate(nums):
        #     total += num
        #     mod = total % k if k != 0 else total 

        #     if mod in mod_map:
        #         if i - mod_map[mod] >= 2:
        #             return True
        #     else:
        #         mod_map[mod] = i

        # return False

        seen = set()
        running = 0
        previous = 0
        for x in nums:
            running +=x 
            running %=k
            if running in seen: 
                return True
            seen.add(previous) 
            previous = running
        return False