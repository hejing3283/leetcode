# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        ### ------- Memory limit exceeded -------------------
        # if not inorder : return None
        # root = TreeNode( preorder[0] ) 
        # rootPos = inorder.index( preorder[0] )
        # root.left = self.buildTree( preorder[1:rootPos+1] , inorder[:rootPos] ) 
        # root.right = self.buildTree( preorder[rootPos+1:], inorder[rootPos+1:] ) 
        # return root
        ### ------- Memory limit exceeded -------------------
        def bfs( preorder, inorder) :
            if not inorder or not preorder: return None
            root = TreeNode( preorder[0] ) 
            idx = inorder.index( preorder[0] ) 
            preorder.pop(0)
            root.left = bfs(preorder, inorder[:idx] ) 
            root.right = bfs(preorder, inorder[idx+1:] )
            return root 
        return bfs(preorder, inorder)
            
                    