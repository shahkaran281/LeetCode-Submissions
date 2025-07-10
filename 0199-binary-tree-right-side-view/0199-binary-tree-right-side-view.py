# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        q = deque([root])
        ans = []
        while q:
            n = len(q)
            isFirst = True
            for _ in range(n):
                node = q.popleft()
                if isFirst:
                    ans.append(node.val)
                    isFirst = False
                if node.right:
                    q.append(node.right)
                if node.left:
                    q.append(node.left)
        return ans