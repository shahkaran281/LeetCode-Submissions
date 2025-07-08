# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        #     3
        #    / \
        #   5   1
        #  /\   /\
        # 6  2 0  8
        #   / \
        #  7   4
        # p,q = 7,4
        # print(p,q)
        # if (p == root or q==  root) and ((root.left and (root.left == p or root.left == q)) or
        #     (root.right and (root.right == p or root.right == q))):
        #     return root

        # def fun(node):
        #     if not node:
        #         return 0
        #     return (node == p) + (node == q) + fun(node.left) + fun(node.right)

        # def lca(node):
        #     leftCount = fun(node.left)
        #     rightCount = fun(node.right)
        #     # print(node.val,leftCount,rightCount)
        #     if (node == p or node == q):
        #         return node
        #     elif leftCount == rightCount:
        #         return node
        #     elif leftCount > rightCount:
        #         return lca(node.left)
        #     else:
        #         return lca(node.right)
        # return lca(root)
        # parentOf = {root: None}

        # que = deque([root])

        # while que:
        #     curr = que.popleft()
        #     if curr.left:
        #         parentOf[curr.left] = curr
        #         que.append(curr.left)
        #     if curr.right:
        #         parentOf[curr.right] = curr
        #         que.append(curr.right)

        # visited = set()
        # curr = p
        # while curr:
        #     visited.add(curr)
        #     curr = parentOf[curr]

        # curr = q
        # while curr:
        #     if curr in visited:
        #         return curr
        #     curr = parentOf[curr]

        # return None
        if not root or root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root
        return left if left else right

