class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res =  []
        counter = collections.Counter(nums)
        for num, count in counter.items():
            if count > len(nums)/3:
                res.append(num)
        return res
        