# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
        
    def dfs(self, rootL, rootR  ):
        if (not rootL and not rootR) : return True
        elif (not rootL and rootR) or (rootL and not rootR) : return False
        elif rootL.val == rootR.val: 
            return self.dfs( rootL.left, rootR.right ) and  self.dfs( rootL.right, rootR.left )
        else :
            return False 
        
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        ###------ recursive version 
        return self.dfs( root, root )
      
        
    
        