# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        ## recursive 
        # def dfs( root ):
        #     if not root: return
        #     dfs(root.left)
        #     dfs(root.right)
        #     res.append(root.val)
        # res = []; dfs(root) ;
        
        ## iterative
        res = []
        stack = []; prev = None
        if root:
            stack.append(root)
            while stack: 
                curr = stack[-1]
                if (curr.left == None and curr.right == None) or (prev and (prev == curr.left or prev == curr.right)) : 
                    res.append(curr.val);  prev = stack.pop()
                else:
                    if curr.right: stack.append(curr.right)
                    if curr.left:  stack.append(curr.left) 
        return res 
            