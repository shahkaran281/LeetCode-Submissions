# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def fun(node) :
            if node == None:
                return 0
            left = fun(node.left)
            right = fun(node.right)
            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1
            return max(left,right) + 1
            
        if root == None:
            return True
        res = fun(root)
        return False if res == -1 else res
                
        