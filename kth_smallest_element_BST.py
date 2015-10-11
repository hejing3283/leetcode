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
        #### optimize
        stack = []; p = root; pRank = 0
        while p or stack:
            while p:
                stack.append(p)
                p = p.left
            if stack:
                p = stack[-1]
                pRank += 1

                if pRank == k:
                    return p.val; 
                stack.pop()
                p = p.right
            
        #### AC self 
        # def inorder( root, path) : 
        #     if root:
        #         inorder( root.left, path) 
        #         path.append( root.val) 
        #         inorder(root.right, path ) 
                
        # path = []
        # inorder( root, path) 
        # return path[k-1]
        
        