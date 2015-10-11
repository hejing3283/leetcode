# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        ### more consice
        if root:
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
            return root 
        ### AC 1
        # if root:
        #     tmp = root.left
        #     root.left = self.invertTree(root.right)
        #     root.right = self.invertTree(tmp)
        #     return root 