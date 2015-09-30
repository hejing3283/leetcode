# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.maxSum = -21474836
        
        def dfs(root) : 
            if not root : return 0
            left = dfs( root.left ) 
            right = dfs( root.right )
            self.maxSum = max( left + right + root.val, self.maxSum) 
            res = root.val + max( left, right) 
            return (res if res > 0 else 0 ) 
        dfs( root ) 
        return self.maxSum
        
  