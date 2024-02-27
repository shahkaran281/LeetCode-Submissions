# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
        def fun(node):
            nonlocal res
            if not node:
                return 0
            leftLen = 1 + fun(node.left)
            rightLen = 1 + fun(node.right)
            res = max(res,leftLen + rightLen -1)
            return max(leftLen,rightLen)
        fun(root)
        return res-1
        