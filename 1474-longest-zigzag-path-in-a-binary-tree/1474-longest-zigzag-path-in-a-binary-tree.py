# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        res = 0
        def fun(node,nextLeft):
            nonlocal res
            if not node:
                return 0
            left = fun(node.left,True)
            right = fun(node.right,False)
            res = max(res,left,right)
            if nextLeft:
                return 1 + right
            else:
                return 1 + left
        fun(root,True)
        return res

            