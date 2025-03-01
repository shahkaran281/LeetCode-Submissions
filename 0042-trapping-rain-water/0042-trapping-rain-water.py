class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        maxL = [0] * n
        maxR = [0] * n
        mx = 0
        for i in range(n):
            maxL[i] = mx
            mx = max(mx,height[i])
        mx = 0
        for i in range(n-1,-1,-1):
            maxR[i] = mx
            mx = max(mx,height[i])
        ans = 0
        for i in range(n):
            ans += max(min(maxL[i],maxR[i])- height[i],0)
        # print(maxL)
        # print(maxR)
        return ans