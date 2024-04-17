class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = [root.val]

        def dfs(root):
            if not root:
                return 0

            left = dfs(root.left)
            right = dfs(root.right)
            left = max(left, 0)
            right = max(right, 0)
            res[0] = max(res[0], root.val + left + right)

            return root.val + max(left, right)
        
        dfs(root)
        return res[0]