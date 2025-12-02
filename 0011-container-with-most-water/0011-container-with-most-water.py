class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        leftMax = 0
        rightMax = 0
        ans = 0
        while left < right:
            leftMax = max(leftMax,height[left])
            rightMax = max(rightMax,height[right])
            ans = max(ans,min(leftMax,rightMax)*(right - left))
            if height[left] < height[right]:
                left+=1
            else:
                right -=1
        return ans