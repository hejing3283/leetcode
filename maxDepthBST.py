# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.D = 0
        return self.dfs(root, 0)
    def dfs(self, root, curr):
        if not root: return max( curr, self.D - 1)
        return max( self.dfs( root.left, curr+1 ),  self.dfs( root.right, curr+1)) 

        
        