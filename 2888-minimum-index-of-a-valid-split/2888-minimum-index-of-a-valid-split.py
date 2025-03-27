class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        counter = Counter(nums)
        mx = nums[0]
        for x, freq in counter.items():
            if counter[x] > counter[mx]:
                mx = x
        # print(x,counter[x])
        first = 0
        for i in range(len(nums)):
            if nums[i] == mx:
                first += 1
                counter[mx] -= 1
            # print(i,first,counter[mx], (i+1), (len(nums) - (i+1)))
            if 2*first > (i+1) and 2*counter[mx] > (len(nums) - (i+1)):
                return i
        return -1