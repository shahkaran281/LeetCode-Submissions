class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        start = 0
        counter = Counter(nums)
        while len(counter) != (len(nums)- start):
            # print(len(counter), len(nums)- start)
            remove = 3
            while start < len(nums) and remove > 0:
                counter[nums[start]] -= 1
                if counter[nums[start]] == 0:
                    del counter[nums[start]]
                start += 1
                remove -= 1
        return ceil(start / 3)
        