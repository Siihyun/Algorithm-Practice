# dfs problem
# find path from root to leaf if exist

class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:        
        if not root: 
            return False
            
        targetSum -= root.val
        if not root.left and not root.right: # check only if leaf node
            return targetSum == 0
            
        return self.hasPathSum(root.left,targetSum) or self.hasPathSum(root.right,targetSum)
        
        