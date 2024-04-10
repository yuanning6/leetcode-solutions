class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(root):
            # without the nonlocal keyword, 
            # if try to modify a variable in an outer scope from within an inner function, 
            # Python will create a new local variable with the same name instead of modifying the outer variable.
            # can use res = [0] instead
            nonlocal res

            if not root:
                return 0
            
            left = dfs(root.left)
            right = dfs(root.right)
            res = max(res, left + right)

            # return the height
            return 1 + max(left, right)
        
        dfs(root)
        return res