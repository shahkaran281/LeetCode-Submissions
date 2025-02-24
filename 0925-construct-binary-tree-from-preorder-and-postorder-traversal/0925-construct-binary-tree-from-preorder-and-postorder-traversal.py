# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def fun(i1, j1, i2, j2):
            if i1 > j1:
                return None
            
            node = TreeNode(preorder[i1])
            
            if i1 == j1: 
                return node
            
            left_value = preorder[i1 + 1]
            left_index_in_postorder = postorder.index(left_value)
            
            left_length = left_index_in_postorder - i2 + 1
            
            node.left = fun(i1 + 1, i1 + left_length, i2, i2 + left_length - 1)
            node.right = fun(i1 + left_length + 1, j1, i2 + left_length, j2 - 1)
            
            return node

        return fun(0,len(preorder)-1,0,len(preorder)-1)
        