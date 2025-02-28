class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        counter = Counter(nums)
        ans = 0
        for i in counter.keys():
            if k - i in counter:
                if 2*i == k:
                    n = counter[i]//2
                    counter[i]-=n
                else:
                    n = min(counter[i],counter[k-i])
                    counter[i]-=n
                    counter[k-i]-=n
                ans+=n
        return ans