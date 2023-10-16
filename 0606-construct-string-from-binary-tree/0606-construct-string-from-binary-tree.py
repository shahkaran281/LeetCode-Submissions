# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        def fun(node):
            if node == None:
                return ""
            s = str(node.val)
            # print(node)
            if node.right != None:
                s += "(" + fun(node.left) + ")"
                s += "(" + fun(node.right) + ")"
            elif node.left != None:
                s += "(" + fun(node.left) + ")"
            return s
        return fun(root)
            


        