class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        counter = Counter({0:1})
        curr = 0
        ans = 0
        for num in nums:
            curr += num
            if curr - k in counter:
                ans += counter[curr - k]
            counter[curr] +=1
        
        # print(counter)
        # for count in counter:
            

        return ans