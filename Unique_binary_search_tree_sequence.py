# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        def dfs( start, end ) :
            if start > end : return [None]
            res = []
            for rootVal in range(start, end + 1):
                leftTree = dfs(start, rootVal - 1 ) 
                rightTree = dfs(rootVal+1, end) 
                for i in leftTree:
                    for j in rightTree:
                        root = TreeNode(rootVal)
                        root.left = i
                        root.right = j
                        res.append(root)
            return res
        return dfs(1, n)