# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val = val)
        curr = root
        while curr:
            if val >= curr.val:
                if  curr.right == None:
                    curr.right = TreeNode(val = val)
                    return root

                curr = curr.right
            else:
                if curr.left == None:
                    curr.left = TreeNode(val = val)
                    return root
                curr = curr.left
        return root