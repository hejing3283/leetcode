# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        ### divide and conquer:
        if not root or p == root or q == root: return root
        
        left = self.lowestCommonAncestor( root.left, p, q) 
        right = self.lowestCommonAncestor( root.right, p, q) 
        if left and right: 
            return root
        if left:
            return left
        if right:
            return right
        else:
            return None
        ### AC from online
        # def dfs_iter( root, target ) :
        #     stack = []; prev = None
        #     while stack or root:
        #         if root: 
        #             stack.append(root)
        #             root = root.left
        #         else:
        #             top = stack[-1]
        #             if top.right and  prev != top.right :
        #                 root = top.right
        #             else:
        #                 if top == target: return stack
        #                 prev = stack.pop()
        #                 root = None
        #     return stack
        
        # pathP, pathQ = dfs_iter(root, p) , dfs_iter(root,q)
        # lenP, lenQ = len(pathP), len(pathQ)
        # ans, x  = None, 0
        # while x < min(lenP, lenQ) and pathP[x] == pathQ[x]:
        #     ans, x = pathP[x], x+1
        # return ans
                    

    # def lowestCommonAncestor(self, root, p, q):
    #     """
    #     :type root: TreeNode
    #     :type p: TreeNode
    #     :type q: TreeNode
    #     :rtype: TreeNode
    #     """
        
    #     ### Memory Limite
    #     def dfs( root, p, prev) :
    #         if root: 
    #             if root == p: 
    #                 return prev
    #             dfs( root.left, p, prev + [root] ) 
    #             dfs( root.right,p, prev + [root]) 
    #     pstack = []
    #     qstack = []
    #     dfs( root, p, pstack) 
    #     dfs( root, q, qstack) 
    #     while pstack:
    #         pp = pstack.pop(0)
    #         while qstack:
    #             qq = qstack.pop(0)
    #             if pp == qq and qstack[0] != pstack[0]:
    #                 return pp
                
                    