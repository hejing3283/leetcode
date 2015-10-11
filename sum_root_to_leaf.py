# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        ### method 2 from web
        def mySum( root, preSum): 
            if not root: return 0
            preSum = preSum * 10 + root.val
            if not root.right and not root.left: return preSum
            return mySum( root.left, preSum ) + mySum( root.right, preSum) 
        
        return mySum(root, 0)
        ### method 1 by self.
        # def dfs( root, curr, res):
        #     if  root.left == None and root.right == None:
        #         res.append( curr) 
        #     else :
        #         curr = curr * 10 
        #         if root.left:
        #             dfs(root.left, curr + root.left.val, res) 
        #         curr = curr - curr % 10 
        #         if root.right:
        #             dfs(root.right, curr + root.right.val, res) 
                    
        # if not root: return 0
        # res = []
        # dfs(root, root.val, res) 
        # ret = 0
        # for i in res: ret +=i 
        # return ret
        