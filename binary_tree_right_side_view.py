# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root: return []
        stack = [root]; res = [];
        while stack: 
            res.append(stack[-1].val) 
            curr, stack = stack, [] 
            while curr:
                tmp = curr[0]
                if tmp.left: stack.append(tmp.left)
                if tmp.right: stack.append(tmp.right) 
                curr.pop(0)
        return res