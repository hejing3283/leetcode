# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, S):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        res = []
        def dfs(root, csum, curr ) :
            if not root.left and not root.right: 
                if csum == 0 and curr:
                    res.append( curr );
            if root.left: 
                dfs( root.left, csum - root.left.val , curr + [root.left.val] ) 
            if root.right: 
                dfs( root.right, csum - root.right.val , curr + [root.right.val] ) 
        if not root: return res 
        dfs( root, S-root.val, [root.val]) 
        return res

        
            
        