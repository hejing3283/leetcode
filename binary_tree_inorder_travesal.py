# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # def dfs(root, res ) :
        #     if root:
        #         self.dfs(root.left, res)
        #         res.append(root.val)
        #         self.dfs(root.right, res)
        #     return res
        # res = []
        # dfs(root, res)
        # return res
        res = []
        self.iterative_inorder(root, res)
        return res
        
    def iterative_inorder(self, root, res):
        stack = []
        if not root: return []
        while root or stack:
            if root:
                stack.append( root ) 
                root = root.left
            else:
                root = stack.pop()
                res.append(root.val) 
                root = root.right
        return res
    
            
        
        


                