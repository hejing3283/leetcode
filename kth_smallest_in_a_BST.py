# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        def inorder( root, path) : 
            if root:
                inorder( root.left, path) 
                path.append( root.val) 
                inorder(root.right, path ) 
                
        path = []
        inorder( root, path) 
        return path[k-1]