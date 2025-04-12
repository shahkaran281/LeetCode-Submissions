class Solution:
    def earliestSecondToMarkIndices(self, nums: List[int], changeIndices: List[int]) -> int:
        def fun(second):
            numMarked = 0
            decrement = 0
            indexToLastSecond = {}

            for i in range(second):
                indexToLastSecond[changeIndices[i] - 1] = i

            for i in range(second):
                index = changeIndices[i] - 1
                if i == indexToLastSecond[index]:
                    if nums[index] > decrement:
                        return False
                    decrement -= nums[index]
                    numMarked += 1
                else:
                    decrement += 1

            return numMarked == len(nums)
        low = 1
        high = len(changeIndices) 
        ans = -1
        while low <= high:
            mid = (low + high) // 2
            # print('Mid:',mid,"Result:",fun(mid))
            if fun(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans