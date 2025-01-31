# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ans = 0
        def fun(node,currMax):
            nonlocal ans
            if not node:
                return
            if node.val >= currMax:
                ans+=1
            currMax = max(currMax, node.val)
            fun(node.left,currMax)
            fun(node.right,currMax)
        fun(root,float('-inf'))
        return ans
        