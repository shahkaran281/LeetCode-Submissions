class Solution:
    def verticalTraversal(self, root: Optional['TreeNode']) -> List[List[int]]:
        visited = defaultdict(list)

        def dfs(node, x, y):
            if not node:
                return
            visited[x].append((y, node.val)) 
            dfs(node.left, x - 1, y + 1)
            dfs(node.right, x + 1, y + 1)

        dfs(root, 0, 0)

        res = []
        for x in sorted(visited.keys()):
            col_nodes = sorted(visited[x], key=lambda p: (p[0], p[1]))
            res.append([val for y, val in col_nodes])
        return res
