# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def dfs( root, minVal, maxVal ) :
            if root == None : return True
            if root.val <= minVal or root.val >=maxVal:
                return False
            return dfs(root.left, minVal, root.val) and dfs(root.right, root.val, maxVal)
            # if root.left == None and root.right ==None : return True
            # if root.left :
            #     if root.val > root.left.val:
            #         dfs(root.left)
            #     else:
            #         return False
            # if root.right :
            #     if root.val < root.right.val:
            #         dfs(root.right) 
            #     else:
            #         return False
            # return True
            
            
        return dfs(root, -10000000000, 10000000000)
            



