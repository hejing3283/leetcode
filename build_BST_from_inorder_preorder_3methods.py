# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        ## method 1
        # ### --------- memory limit exceeced 
        # if not inorder or not postorder: return None
        # val = postorder[-1]
        # idx = inorder.index(val)
        # root = TreeNode( val )
        # root.left = self.buildTree( inorder[:idx], postorder[:idx] ) 
        # root.right = self.buildTree( inorder[idx+1:], postorder[idx:-1]) 
        # postorder.pop()
        # return root
        
        ## method 2 
        # ### --------- memory limit exceeced 

        # if not inorder or not postorder: return None
        # val = postorder[-1]
        # idx = inorder.index(val)
        # root = TreeNode( val )
        # postorder.pop()
        # root.left = self.buildTree( inorder[:idx], postorder[:idx] ) 
        # root.right = self.buildTree( inorder[idx+1:], postorder[idx:]) 
        # return root
        
        ## method 3: AC
        def dfs( inLeft, postLeft, length ) :
            if length <= 0 : return None 
            root = TreeNode( postorder[ postLeft + length -1 ] ) 
            rootPos = inorder.index( postorder[postLeft + length -1]) 
            root.left = dfs( inLeft, postLeft, rootPos - inLeft )
            root.right = dfs( rootPos+1, rootPos - inLeft + postLeft, length - 1 - (rootPos  - inLeft))
            return root
            
        return dfs( 0, 0, len(inorder) ) 


        