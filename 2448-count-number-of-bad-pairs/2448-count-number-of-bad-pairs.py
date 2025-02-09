class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        n = len(nums)
        goodPairs = 0
        diff = Counter()
        # for j in range(1,len(nums)):
        #     for i in range(j):
        #         ans += ((j-i) != (nums[j]-nums[i]))
        #         print(i,j,nums[i],nums[j], (j-i) != (nums[j]-nums[i]))
        for i in range(len(nums)):
            diff[nums[i]- i] += 1
        for count in diff.values():
            # print(count)
            if count > 1:
                goodPairs += count*(count-1) // 2
        return (n * (n-1)//2) - goodPairs